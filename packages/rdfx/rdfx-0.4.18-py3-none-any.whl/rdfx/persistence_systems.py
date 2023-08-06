from __future__ import annotations

import configparser
import getpass
import io
import json
import os
from abc import ABC, abstractmethod
from datetime import datetime
from http import HTTPStatus
from io import BytesIO, StringIO
from json.decoder import JSONDecodeError
from os import getenv
from pathlib import Path
from typing import List, Optional, Tuple, Union, get_args
from typing import Literal
from urllib.parse import parse_qs

import boto3
import httpx
from botocore.errorfactory import ClientError
from rdflib import Graph, URIRef


RDF_FORMATS = Literal["ttl", "turtle", "xml", "json-ld", "nt", "n3"]
VALID_RDF_FORMATS: Tuple[RDF_FORMATS, ...] = get_args(RDF_FORMATS)

RDF_FILE_ENDINGS = {
    "ttl": "turtle",
    "turtle": "turtle",
    "json": "json-ld",
    "json-ld": "json-ld",
    "jsonld": "json-ld",
    "owl": "xml",
    "xml": "xml",
    "rdf": "xml",
    "nt": "nt",
    "n3": "n3",
}


class PersistenceSystem(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def read(self, graph_name, rdf_format, *args):
        """
        Reads the named graph in the form implemented by this Persistence System

        Args:
            graph_name (Graph): The graph_name to read. Only context-less graphs allowed.
            :param graph_name:
            :param rdf_format:
        """
        pass

    # @abstractmethod
    def write(self, g: Graph, rdf_format, leading_comments, *args):
        """
        Persists the given Graph in the form implemented by this Persistence System

        Args:
            sample_graph (Graph): The RDFlib Graph to persist. Only context-less graphs allowed.
            :param g:
            :param leading_comments:
            :param rdf_format:
        """
        pass

    @staticmethod
    def leading_comment_validator(leading_comments, rdf_format):
        if leading_comments is not None:
            if rdf_format not in ("turtle", "ttl"):
                raise ValueError(
                    f"If leading_comments is provided, rdf_format must be turtle"
                )
            if any(lc.startswith("#") for lc in leading_comments):
                raise ValueError(
                    f"leading_comments may not start with #. It will be added"
                )

    @staticmethod
    def rdf_format_validator(rdf_format):
        if rdf_format not in VALID_RDF_FORMATS:
            raise ValueError(
                f"The RDF format selected must be one of {', '.join(VALID_RDF_FORMATS)}"
            )

    @staticmethod
    def generate_string(g, rdf_format, leading_comments):
        # validate the RDF format - all methods utilise the 'generate_string' static method so this will always be
        # called
        # PersistenceSystem.rdf_format_validator(rdf_format)
        if leading_comments is None:
            return g.serialize(format=rdf_format)
        else:
            PersistenceSystem.leading_comment_validator(leading_comments, rdf_format)
            content = "".join(f"# {comment}\n" for comment in leading_comments)
            # add a new line after the leading comments
            content += "\n"
            content += g.serialize(format=rdf_format)
            return content


class String(PersistenceSystem):
    """
    Persist as a string

    Args:
        rdf_format (str): The RDFlib RDF format to serialise the RDF to
        leading_comments (List[str]): Strings to add as comments to the start of the output.
                                      # will be automatically inserted at the start of each
    """

    def __init__(self):
        self.name = "String"
        super().__init__()

    def read(self, string: str, rdf_format: RDF_FORMATS = "turtle"):
        """
        Reads the given string and returns a Graph

        Args:
            string (str): The string to read
            rdf_format (str): The RDFlib RDF format to parse the string as

        Returns:
            Graph: The parsed Graph
        """
        string_obj = StringIO(string)
        leading_comments = []
        if rdf_format == "turtle":
            while True:
                line = string_obj.readline()
                if line.startswith("#"):
                    leading_comments.append(line.lstrip("# ").rstrip("\n"))
                else:
                    break
        graph = Graph().parse(data=string, format=rdf_format)
        return leading_comments, graph

    def write(
        self,
        g: Graph,
        rdf_format: RDF_FORMATS = "turtle",
        leading_comments: Optional = None,
    ):
        return self.generate_string(g, rdf_format, leading_comments)


class File(PersistenceSystem):
    """
    Persist as a file

    Args:
        directory (Path): The path to the file to serialise to
        rdf_format (str): The RDFlib RDF format to serialise the RDF to, defaults to turtle
        leading_comments (List[str]): Strings to add as comments to the start of the output.
                                      # will be automatically inserted at the start of each
    """

    def __init__(self, directory: Union[Path, str]):
        super().__init__()

        if not isinstance(directory, (Path, str)):
            raise ValueError(f"The file path must be a string or pathlib Path")
        self.directory = Path(directory).resolve()

        if not self.directory.is_dir():
            self.directory.mkdir()

    def asset_exists(self, graph_name: str) -> bool:
        """
        Checks whether an asset exists in a File, returns True or False
        :param graph_name: The key of the object on disk
        :return: boolean
        """
        if Path(self.directory / graph_name).exists():
            return True
        return False

    def read(self, filename: str, rdf_format: RDF_FORMATS = "turtle"):
        leading_comments = []
        file_path = self.directory / filename
        graph = Graph().parse(str(file_path), format=rdf_format)
        if rdf_format == "turtle":
            with open(file_path, "r") as f:
                while True:
                    line = f.readline()
                    if line.startswith("#"):
                        leading_comments.append(line.lstrip("# ").rstrip("\n"))
                    else:
                        break
        return leading_comments, graph

    def write(
        self,
        g: Graph,
        filename: str,
        rdf_format: RDF_FORMATS = "ttl",
        leading_comments: Optional = None,
        output_file_path: Optional = None,
    ):

        if output_file_path:
            file_path = output_file_path / f"{filename}.{rdf_format}"
        else:
            file_path = self.directory / f"{filename}.{rdf_format}"

        s = self.generate_string(g, rdf_format, leading_comments)
        # remove extra line at end of file
        if s[-1] == "\n" and s[-2] == "\n":
            s = s[:-1]

        with file_path.open("w", encoding="utf-8") as f:
            f.write(s)
        return file_path


class S3(PersistenceSystem):
    """
    Persist the graph to S3

    Args:
        bucket (str): The S3 bucket to persist to
        key (str): The name of the object to store in S3
        aws_key: The key part of the credentials to authenticate with AWS for this bucket
        aws_secret: The secret part of the credentials to authenticate with AWS for this bucket
        rdf_format (str): The RDFlib RDF format to serialise the RDF to
        leading_comments (List[str]): Strings to add as comments to the start of the output.
                                      # will be automatically inserted at the start of each
    """

    def __init__(
        self, bucket: str, aws_key: str, aws_secret: str, region: str = "ap-southeast-2"
    ):

        for item in [bucket, aws_key, aws_secret, region]:
            if not isinstance(item, str):
                raise ValueError(
                    f"{item} is of type {type(item)}, but must be a string"
                )

        self.bucket = bucket
        self.aws_key = aws_key
        self.aws_secret = aws_secret
        self.region = region

    def asset_exists(self, graph_name: str) -> bool:
        """
        Checks whether an asset exists in S3, returns True or False
        :param graph_name: The key of the object in S3
        :return: boolean
        """
        args = ["s3"]
        kwargs = {
            "aws_access_key_id": self.aws_key,
            "aws_secret_access_key": self.aws_secret,
            "region_name": self.region,
        }
        client = boto3.client(*args, **kwargs)
        try:
            client.head_object(Bucket=self.bucket, Key=graph_name)
            return True
        except ClientError:
            return False

    def get_files(self, folder: str = ""):
        """
        Gives a list of files in a folder in an S3 bucket
        :param folder: the folder in the S3 bucket to look in, if none is provided defaults to root dir
        :return: list of file names as strings
        """
        args = ["s3"]
        kwargs = {
            "aws_access_key_id": self.aws_key,
            "aws_secret_access_key": self.aws_secret,
            "region_name": self.region,
        }
        client = boto3.client(*args, **kwargs)
        contents = client.list_objects_v2(Bucket=self.bucket, Prefix=folder)["Contents"]
        return [file["Key"] for file in contents]

    def read(self, graph_name, rdf_format: RDF_FORMATS = None):
        args = ["s3"]
        kwargs = {
            "aws_access_key_id": self.aws_key,
            "aws_secret_access_key": self.aws_secret,
            "region_name": self.region,
        }
        client = boto3.client(*args, **kwargs)
        object_bytes = client.get_object(Bucket=self.bucket, Key=graph_name)
        text = StringIO(object_bytes["Body"].read().decode())
        leading_comments = []
        if rdf_format in ("turtle", "ttl"):
            for line in text:
                if line.startswith("#"):
                    leading_comments.append(line.lstrip("# ").rstrip("\n"))
                else:
                    text.seek(0)
                    break
        return leading_comments, Graph().parse(text, format=rdf_format)

    def write(
        self,
        g: Graph,
        filename: str,
        rdf_format: RDF_FORMATS = "ttl",
        leading_comments: Optional = None,
    ):
        filename = f"{filename}.{rdf_format}"
        s = self.generate_string(g, rdf_format, leading_comments)
        bytes_obj = BytesIO(s.encode("utf-8"))
        try:
            import boto3
            import botocore
        except ImportError:
            raise
        args = ["s3"]
        kwargs = {
            "aws_access_key_id": self.aws_key,
            "aws_secret_access_key": self.aws_secret,
            "region_name": self.region,
        }
        client = boto3.client(*args, **kwargs)
        response = client.put_object(Body=bytes_obj, Bucket=self.bucket, Key=filename)
        if response["ResponseMetadata"]["HTTPStatusCode"] == HTTPStatus.OK:
            return filename
        else:
            response.raise_for_status()


class GraphDB(PersistenceSystem):
    """
    Persist to an instance of GraphDB

    Args:
        location (str): The IRI of the GraphDB system. Something like http://localhost:7200 (no training slash)
        repo_id (str): The ID of the repository on this GraphDB system to persist to
        graph_iri (str): The IRI of the graph to write to. Optional. Default is non (default graph)
        username (str): The username of a user on this GraphDB instance. Optional.
        password (str): The password of the user on this GraphDB instance. Optional.
    """

    def __init__(
        self,
        location: str,
        repo_id: str,
        username: Optional[str] = None,
        password: Optional[str] = None,
    ):
        self.name = "GraphDB"

        if location is None or not location.startswith("http"):
            raise ValueError(
                f"The value you supplied for location ({location}) is not valid"
            )

        if repo_id is None:
            raise ValueError(f"The value you supplied for repo_id cannot be None")

        self.location = location
        self.repo_id = repo_id
        self.username = username
        self.password = password

    def __repr__(self):
        return "GraphDB"

    def write(self, g: Graph, graph_iri):
        if graph_iri is not None and not (
            graph_iri.startswith("http") or graph_iri.startswith("urn")
        ):
            raise ValueError(
                f"The value you supplied for graph_iri ({graph_iri}) is not valid"
            )
        raise NotImplemented


class Fuseki(PersistenceSystem):
    """
    Persist to an instance of Fuseki

    Args:
        location (str): The IRI of the GraphDB system. Something like http://localhost:7200 (no training slash)
        repo_id (str): The ID of the repository on this GraphDB system to persist to
        graph_iri (str): The IRI of the graph to write to. Optional. Default is non (default graph)
        username (str): The username of a user on this Fuseki instance. Optional.
        password (str): The password of the user on this Fuseki instance. Optional.
    """

    def __init__(
        self,
        location: str,
        repo_id: str,
        username: Optional[str] = None,
        password: Optional[str] = None,
    ):

        if location is None or not location.startswith("http"):
            raise ValueError(
                f"The value you supplied for location ({location}) is not valid"
            )

        if repo_id is None:
            raise ValueError(f"The value you supplied for repo_id cannot be None")

        self.location = location
        self.repo_id = repo_id
        self.username = username
        self.password = password

    def write(self, g: Graph, graph_iri):
        if graph_iri is not None and not (
            graph_iri.startswith("http") or graph_iri.startswith("urn")
        ):
            raise ValueError(
                f"The value you supplied for graph_iri ({graph_iri}) is not valid"
            )
        raise NotImplemented


class SOPGraph:
    def __init__(
        self,
        graph_type: str,
        uri: Optional[URIRef],
        name: Optional[str],
        parent: URIRef = None,
    ):
        self.graph_type = graph_type
        self.uri = uri
        self.name = name
        self.parent = parent

    # TODO complete


class SOP(PersistenceSystem):
    """
    Persist to an instance of SURROUND Ontology Platform (SOP)

    Args:
        location (str): The IRI of the SOP system. Defaults to http://localhost:8083 (no trailing slash)
        repo_id (str): The ID of the repository on this GraphDB system to persist to
        graph_iri (str): The IRI of the graph to write to. Optional. Default is non (default graph)
        username (str): The username of a user on this SOP instance. Optional.
        password (str): The password of the user on this SOP instance. Optional.
        local (bool): Whether the SOP persistence system is for a local or remote SOP system
    """

    def __init__(
        self,
        location: str = "http://localhost:8083",
        username: Optional[str] = "Administrator",
        password: Optional[str] = None,
        auth_type: Optional[str] = "basic",
        timeout: Optional[int] = 60,
    ):
        if not location.startswith("http"):
            raise ValueError(
                f'The value you supplied for location ({location}) must start with "http" or "https"'
            )

        if auth_type == "oauth":
            if os.getenv("SOP_CREDS_FILE_PATH"):
                creds_path = os.getenv("SOP_CREDS_FILE_PATH")
                self.creds = SopCredentials(
                    source="file", creds_file_path=Path(creds_path)
                )
            else:
                raise Exception(
                    "you need to specify a path to your credentials in the SOP_CREDS_FILE_PATH environment variable"
                )
            self.location = self.creds.endpoint
            self.username = username
            self.password = password
            self.auth_type = auth_type
            self.client = None
            self.local = True if self.location.startswith("http://localhost") else False
            self.timeout = timeout

        elif auth_type == "basic":
            self.location = location
            self.username = username
            self.password = password
            self.auth_type = auth_type
            self.client = None
            self.timeout = timeout
            self.local = True if location.startswith("http://localhost") else False
            self.access_token = None

    def write(self, g: Graph, graph_iri, leading_comments=None):
        if not (graph_iri.startswith("http") or graph_iri.startswith("urn")):
            raise ValueError(
                f"The value you supplied for graph_iri ({graph_iri}) is not valid"
            )
        if not self.client:
            self._create_client()
        content = self.generate_string(g, "ttl", leading_comments)
        headers = {}
        if self.access_token:
            headers["Authorization"] = f"Bearer {self.access_token}"
        if self.local:
            headers["Cookie"] = "username=Administrator"
        if graph_iri.startswith("urn:x-evn-tag"):
            projectGraph = SOP.graph_from_workflow(graph_iri)
        else:
            projectGraph = graph_iri
        form_data = {
            "_viewClass": "http://topbraid.org/teamwork#ImportRDFFileService",
            "projectGraph": projectGraph,
            "_base": graph_iri,
            "format": "turtle",
        }
        if graph_iri.startswith("urn:x-evn-tag"):
            form_data["tag"] = SOP.tag_from_workflow(graph_iri)
        response = self.client.post(
            self.location + "/importFileUpload",
            data=form_data,
            files={"file": io.BytesIO(bytes(content.encode("utf-8")))},
            headers=headers,
            timeout=self.timeout,
        )
        return parse_qs(response.text)["message"][0]

    def read_deprecated(
        self, query, graph_iri, return_format: Optional[str] = "application/rdf+xml"
    ):
        if not self.client:
            self._create_client()
        try:
            response = self.client.post(
                self.location + "/sparql",
                data={
                    "query": query,
                    "with-imports": "false",
                    "default-graph-uri": graph_iri,
                },
                headers={"Accept": return_format},
            )
            g = Graph().parse(StringIO(response.text), format="xml")
            return g
        except Exception:
            raise

    def read(self, graph_iri, rdf_format: str = "turtle", legacy: bool = False):
        if not self.client:
            self._create_client()
        if not legacy:
            if graph_iri.startswith("urn:x-evn-master"):
                response = self.client.get(
                    self.location
                    + f"/service/{graph_iri.split(':')[2]}/tbs/exportRDFFile?format={rdf_format}",
                    headers={"Cookie": f"username=Administrator"},
                )
            elif graph_iri.startswith("urn:x-evn-tag"):
                response = self.client.get(
                    self.location
                    + f"/service/{graph_iri.split(':')[2]}.{graph_iri.split(':')[3]}/tbs/exportRDFFile?format={rdf_format}",
                    headers={"Cookie": f"username=Administrator"},
                )
            else:
                raise NotImplemented(
                    "Only asset and workflow graphs are currently supported"
                )
        else:  # legacy
            if graph_iri.startswith("urn:x-evn-master"):
                params = {
                    "_base": graph_iri,
                    "id": "ExportToRDF",
                    "projectGraph": graph_iri,
                    "serialization": "http://topbraid.org/sparqlmotionlib#Turtle",
                }
            elif graph_iri.startswith("urn:x-evn-tag"):
                params = {
                    "_base": graph_iri,
                    "id": "ExportToRDF",
                    "projectGraph": self.graph_from_workflow(graph_iri),
                    "serialization": "http://topbraid.org/sparqlmotionlib#Turtle",
                    "tag": self.tag_from_workflow(graph_iri),
                }
            response = self.client.get(self.location + "/sparqlmotion", params=params)

        text = StringIO(response.text)
        leading_comments = []
        if rdf_format in ("turtle", "ttl"):
            for line in text:
                if line.startswith("#"):
                    leading_comments.append(line.lstrip("# ").rstrip("\n"))
                else:
                    break
        return leading_comments, Graph().parse(text, format=rdf_format)

    def query(
        self, query, graph_iri, return_format: Optional[str] = "application/json", update: Optional[bool] = False):
        if not self.client:
            self._create_client()
        headers = {"Accept": return_format}
        if self.access_token:
            headers["Authorization"] = f"Bearer {self.access_token}"
        try:
            if update:
                response = self.client.post(
                    self.location + "/sparql",
                    data={
                        "update": query,
                        "with-imports": "false",
                        "default-graph-uri": graph_iri,
                        "using-graph-uri" : graph_iri
                    },
                    headers=headers,
                )
            else:
                response = self.client.post(
                    self.location + "/sparql",
                    data={
                        "query": query,
                        "with-imports": "false",
                        "default-graph-uri": graph_iri,
                    },
                    headers=headers,
                )
            if update:
                if response.status_code == 200:
                    return True
                else:
                    print('status update - failed')
                    return False
            else:
                text_result = json.loads(response.text)
                result = [
                    {str(k): v for k, v in i.items()}
                    for i in text_result["results"]["bindings"]
                ]
                return result
        except Exception:
            raise

    def asset_collection_size(self, asset_iri):
        """
        A wrapper around query to return the size of a given graph
        :param asset_iri:
        :return:
        """
        query = f"""SELECT (COUNT(*) as ?count) WHERE {{GRAPH <{asset_iri}> {{?s ?p ?o}} }}"""
        query_response = self.query(query, asset_iri, "application/sparql-results+json")
        return int(query_response[0]["count"]["value"])

    def create_datagraph(
        self,
        datagraph_name: Optional[str] = None,
        description: Optional[str] = None,
        subjectArea: Optional[str] = None,
        default_namespace: Optional[str] = None,
        headers: Optional[dict] = None,
    ):

        if datagraph_name and datagraph_name.startswith("urn:x-evn-master"):
            datagraph_name = datagraph_name.strip("urn:x-evn-master:")
        if not datagraph_name:
            datagraph_name = f"Python_created_Datagraph_by_{getpass.getuser()}_at_{datetime.now().isoformat()}"
        if not default_namespace:
            default_namespace = (
                f"https://data.surroundaustralia.com/data/{datagraph_name}#".replace(
                    " ", "_"
                )
            )
        if not subjectArea:
            subjectArea = ""
        if not description:
            description = ""
        # prepare the query
        if self.local:
            headers = {"Cookie": f"username=Administrator"}
        form_data = {
            "_viewClass": "http://topbraid.org/teamwork#CreateProjectService",
            "projectType": "http://teamwork.topbraidlive.org/datagraph/datagraphprojects#ProjectType",
            "subjectArea": subjectArea,
            "name": datagraph_name,
            "defaultNamespace": default_namespace,
            "comment": description,
        }

        response_dict = self._create_sop_asset(form_data, headers)
        datagraph_iri = f"urn:x-evn-master:{response_dict['id']}"
        return datagraph_iri

    def create_workflow(
        self,
        graph_iri: str,
        workflow_name: Optional[str] = None,
        headers: Optional[dict] = None,
    ):
        """
        :param headers: headers to add to the request
        :param graph_iri: The graph to add a workflow to
        :param workflow_name: The name of the workflow. If not provided, the current time is used
        :return: graph name
        """

        if not workflow_name:
            workflow_name = f"Python_created_Workflow_by_{getpass.getuser()}_at_{datetime.now().isoformat()}"

        form_data = {
            "_viewClass": "http://topbraid.org/teamwork#AddTagService",
            "projectGraph": graph_iri,
            "workflow": "http://topbraid.org/teamwork#DefaultTagWorkflowTemplate",
            "name": workflow_name,
            "comment": "",
        }

        response_dict = self._create_sop_asset(form_data, headers)

        # use the name SOP returns for the workflow
        workflow_name = response_dict["rootResource"].split(":")[2]
        workflow_graph_iri = f"{graph_iri}:{workflow_name}:{self.username}".replace(
            "urn:x-evn-master", "urn:x-evn-tag"
        )
        return workflow_graph_iri

    def create_manifest(
        self,
        manifest_name: Optional[str] = None,
        description: Optional[str] = None,
        subjectArea: Optional[str] = None,
        default_namespace: Optional[str] = None,
        headers: Optional[dict] = None,
    ):
        """
        :param headers: headers to add to the request
        :param graph_iri: The graph to add a workflow to
        :param manifest_name: The name of the manifest. If not provided, the current time is used
        :return: graph name
        """
        # set defaults
        if manifest_name and manifest_name.startswith("urn:x-evn-master"):
            manifest_name = manifest_name.strip("urn:x-evn-master:")
        if not manifest_name:
            manifest_name = f"Python_created_Manifest_by_{getpass.getuser()}_at_{datetime.now().isoformat()}"
        if not default_namespace:
            default_namespace = (
                f"https://data.surroundaustralia.com/manifest/{manifest_name}#".replace(
                    " ", "_"
                )
            )
        if not subjectArea:
            subjectArea = ""
        if not description:
            description = ""

        form_data = {
            "_viewClass": "http://topbraid.org/teamwork#CreateProjectService",
            "projectType": "http://surroundaustralia.com/ns/platform/OntologyRegister",
            "owlImports": [
                "urn:x-evn-master:sop_ontology_register_model",
                "https://data.surroundaustralia.com/def/standards-baseline",
            ],
            "name": manifest_name,
            "defaultNamespace": default_namespace,
            "subjectArea": subjectArea,
            "comment": description,
        }

        response_dict = self._create_sop_asset(form_data, headers)
        # use the name SOP returns for the workflow
        manifest_iri = f"urn:x-evn-master:{response_dict['id']}"
        return manifest_iri

    def asset_exists(self, graph_name: str) -> bool:
        """
        Checks whether an asset exists in SOP, returns True or False
        :param graph_name: The EDG URN of the asset
        :return: boolean
        """
        if not self.client:
            self._create_client()

        headers = {"Accept": "application/sparql-results+json"}
        if self.access_token:
            headers["Authorization"] = f"Bearer {self.access_token}"
        if graph_name.startswith("urn:x-evn-tag"):
            if not self.asset_exists(self.graph_from_workflow(graph_name)):
                return False
            else:
                return True
        query = f"ASK WHERE {{GRAPH <{graph_name}> {{?s ?p ?o}} }}"
        response = self.client.post(
            self.location + "/sparql",
            data={"query": query},
            headers=headers,
        )
        try:
            return json.loads(response.text)["boolean"]
        except JSONDecodeError:
            # SOP exception
            raise Exception(response.text)

    def _create_sop_asset(self, form_data, headers: Optional[dict]):
        # set defaults
        if not headers:
            headers = {}
        if self.local:
            headers["Cookie"] = "username=Administrator"
        if not self.client:
            self._create_client()
        if self.access_token:
            headers["Authorization"] = f"Bearer {self.access_token}"

        # send to SOP
        response = self.client.post(
            self.location + "/swp",
            data=form_data,
            headers=headers,
            cookies=self.client.cookies,
        )
        response_dict = json.loads(response.text)
        keys = response_dict.keys()
        if "response" in keys:  # datagraph creation success
            if response_dict["response"].startswith("Successfully"):
                return response_dict
        elif "changed" in keys:  # workflkow creation success
            if response_dict["changed"]:
                return response_dict
        elif "error" in keys:
            if (
                response_dict["error"]
                == f"A working copy with the label {form_data['name']} already exists."
            ):
                print(
                    f"Asset {form_data['name']} already exists in SOP instance {self.location}."
                )
                return response_dict
            else:
                raise ValueError(response_dict["error"])
        else:
            raise Exception(f"Failed to create {form_data['name']} graph on SOP")

    def _close(self):
        self.client.get(self.location + "/purgeuser?app=edg")

    def _create_client(self, test_connection=False):
        self.location += "/tbl"
        self.client = httpx.Client()

        self.client.get(self.location)
        if self.location.startswith("http://localhost"):
            return True  # auth is not required

        elif self.auth_type == "oauth":

            request_body = {
                "client_id": self.creds.client_id,
                "client_secret": self.creds.client_secret,
                "grant_type": "client_credentials",
                "scope": self.creds.client_scope,
            }
            try:
                response = self.client.post(
                    url=self.creds.auth_server_url,
                    data=request_body,
                    headers={"Accept": "application/json"},
                )
                tokens = response.json()
                self.access_token = tokens["access_token"]
                self.token_time = datetime.now()

                print(self.access_token)
            except Exception as error:
                print(error.code)
                print(error.reason)

        elif self.auth_type == "basic":
            auth_response = self.client.post(
                self.location + "/j_security_check",
                data={
                    "j_username": self.username,
                    "j_password": self.password,
                    "login": "LOGIN",
                },
                headers={"Accept": "text/html"},
            )
            if auth_response.text:
                if test_connection:
                    return auth_response.text
                else:
                    raise ValueError(auth_response.text)
            return True

    @staticmethod
    def graph_from_workflow(workflow_graph):
        # example input workflow: "urn:x-evn-tag:datagraph_name:workflow_name:Administrator"
        if not workflow_graph.startswith("urn:x-evn-tag"):
            raise ValueError(
                "The workflow graph passed does not start with 'x-evn-tag' - it does not look like a SOP "
                "Workflow"
            )
        intermediate = workflow_graph.split(":")
        intermediate[1] = "x-evn-master"
        return ":".join(intermediate[:3])

    @staticmethod
    def tag_from_workflow(workflow_graph):
        # example input workflow: "urn:x-evn-tag:datagraph_name:workflow_name:Administrator"
        if not workflow_graph.startswith("urn:x-evn-tag"):
            raise ValueError(
                "The workflow graph passed does not start with 'x-evn-tag' - it does not look like a SOP "
                "Workflow"
            )
        workflow_name = workflow_graph.split(":")[3]
        return "urn:x-tags:" + workflow_name


def prepare_files_list(files: Union[str, list, Path]) -> list:
    if isinstance(files, (str, Path)):
        files = [files]
    elif isinstance(files, (list)):
        pass
    else:
        raise ValueError("You must pass a string, pathlib Path, or list of these")
    files_list = (
        []
    )  # [Path(file) if Path(file).is_file() else file.glob('*') for file in args.data ]
    for file in files:
        fp = Path(file)
        if fp.is_dir():
            for file_type in RDF_FILE_ENDINGS.keys():
                files_list.extend([file for file in fp.glob("*" + file_type)])
        elif fp.is_file():
            files_list.append(fp)
    return files_list


########################################################################
#
#   Class SopCredentials - controls the oauth etc for connecting to the SOP Instance
#
########################################################################


class SopCredentials:
    """A small class to hold SOP credentials"""

    def __init__(
        self,
        source: Literal["file", "env", "given"] = "given",
        endpoint="http://localhost:8083",
        access_token="",
        token_time="",
        token_interval=3600,
        sendgraph="urn:x-evn-master:load_processing_graph",
        sendont="urn:x-evn-master:bdr_data_datatype_ontology",
        creds_file_path: Path = None,
        creds_file_section: str = "default",
        env_endpoint_name: str = "SOP_ENDPOINT",
        env_auth_server_url_name: str = "SOP_auth_server_url_name",
        env_client_id_name: str = "SOP_client_id_name",
        env_client_secret_name: str = "SOP_client_secret_name",
        env_client_scope_name: str = "SOP_client_scope_name",
        env_client_sop_graph: str = "SOP_client_sop_graph",
        env_client_sop_ont: str = "SOP_client_sop_ont",
    ):
        # validation
        if source == "file":
            if not Path(creds_file_path).is_file():
                raise ValueError(
                    "If you select 'file' as source, you must provide a valid file for creds_file_path"
                    f"You supplied: {creds_file_path}"
                )
        else:
            if creds_file_path is not None:
                raise ValueError(
                    "You have supplied a value for creds_file_path that is not a file, "
                    f"or a file that cannot be accessed: {creds_file_path}"
                )

        # use
        if source == "given":
            self.endpoint = endpoint
            self.send_graph = sendgraph
            self.send_ont = sendont
        elif source == "file":
            config = configparser.ConfigParser()
            config.read(creds_file_path)
            self.endpoint = config[creds_file_section]["sop_endpoint"]
            self.auth_server_url = config[creds_file_section]["auth_server_url"]
            self.client_id = config[creds_file_section]["client_id"]
            self.client_secret = config[creds_file_section]["client_secret"]
            self.client_scope = config[creds_file_section]["client_scope"]
            self.send_graph = config[creds_file_section]["sop_graph"]
            self.send_ont = config[creds_file_section]["sop_ont"]
        elif source == "env":
            self.endpoint = getenv(env_endpoint_name)
            self.auth_server_url = getenv(env_auth_server_url_name)
            self.client_id = getenv(env_client_id_name)
            self.client_secret = getenv(env_client_secret_name)
            self.client_scope = getenv(env_client_scope_name)
            self.send_graph = getenv(env_client_sop_graph)
            self.send_ont = getenv(env_client_sop_ont)

        if self.endpoint is None:
            raise ValueError(
                "Invalid SOP credentials. No value for self.endpoint has been obtained"
            )

        # get a access_token
        self.token_interval = token_interval


PERSISTENCE_SYSTEMS = {k.__name__: k for k in [String, File, SOP, GraphDB, Fuseki, S3]}

"""
Competitor Knowledge Graph Builder (Task 2)
Typed input and output declarations using nanoagent.plugin.contract standards.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Annotated, Optional
from slimconfig import Output


class Tool(Enum):
    EXTRACT_ENTITIES = "extract_entities"
    BUILD_GRAPH = "build_graph"


class Task(Enum):
    GRAPH_BUILDER = "graph-builder"


# ---- Metadata Annotations ----
ENTITY_ID = "Unique identifier for node, e.g., 'company:doordash', 'industry:consumer'"
REL_TYPE = "Edge relation type, e.g., 'BELONGS_TO_INDUSTRY', 'OPERATES_IN_LOCATION', 'COMPETES_WITH'"


@dataclass
class Node(Output):
    id: Annotated[str, ENTITY_ID]
    label: Annotated[str, "Entity class: Company, Industry, Location, or Batch"]
    name: str
    properties: Annotated[dict[str, str], "Additional attributes such as tagline or website"]


@dataclass
class Edge(Output):
    source_id: Annotated[str, "Source node ID"]
    target_id: Annotated[str, "Target node ID"]
    relation: Annotated[str, REL_TYPE]


@dataclass
class ScrapedCompanyInput(Output):
    company_name: str
    tagline: str
    batch: str
    location: str
    website: str
    tags: list[str]


@dataclass
class GraphBuilderInput(Output):
    companies: list[ScrapedCompanyInput]


@dataclass
class GraphBuilderOutput(Output):
    nodes: list[Node]
    edges: list[Edge]
    node_count: int
    edge_count: int


TOOLS = {
    Tool.EXTRACT_ENTITIES: (GraphBuilderInput, GraphBuilderOutput),
}

TASKS = {
    Task.GRAPH_BUILDER: (GraphBuilderInput, GraphBuilderOutput),
}
"""
Knowledge Graph Construction Tools (Task 2)
"""

from contract import (
    GraphBuilderInput,
    GraphBuilderOutput,
    Node,
    Edge,
)


def build_knowledge_graph_tool(input_data: GraphBuilderInput) -> GraphBuilderOutput:
    nodes_map: dict[str, Node] = {}
    edges: list[Edge] = []

    for co in input_data.companies:
        # 1. Create a Company node
        co_id = f"company:{co.company_name.lower().replace(' ', '_')}"
        if co_id not in nodes_map:
            nodes_map[co_id] = Node(
                id=co_id,
                label="Company",
                name=co.company_name,
                properties={"tagline": co.tagline, "website": co.website}
            )

        # 2. Create Batch Nodes and Edges
        if co.batch:
            batch_id = f"batch:{co.batch.lower().replace(' ', '_')}"
            if batch_id not in nodes_map:
                nodes_map[batch_id] = Node(
                    id=batch_id,
                    label="Batch",
                    name=co.batch,
                    properties={}
                )
            edges.append(Edge(source_id=co_id, target_id=batch_id, relation="BELONGS_TO_BATCH"))

        # 3. Create Location Nodes and Edges
        if co.location:
            loc_id = f"location:{co.location.lower().replace(' ', '_')}"
            if loc_id not in nodes_map:
                nodes_map[loc_id] = Node(
                    id=loc_id,
                    label="Location",
                    name=co.location,
                    properties={}
                )
            edges.append(Edge(source_id=co_id, target_id=loc_id, relation="LOCATED_IN"))

        # 4. Create Industry nodes and edges
        for tag in co.tags:
            tag_id = f"industry:{tag.lower().replace(' ', '_')}"
            if tag_id not in nodes_map:
                nodes_map[tag_id] = Node(
                    id=tag_id,
                    label="Industry",
                    name=tag,
                    properties={}
                )
            edges.append(Edge(source_id=co_id, target_id=tag_id, relation="BELONGS_TO_INDUSTRY"))

    node_list = list(nodes_map.values())
    return GraphBuilderOutput(
        nodes=node_list,
        edges=edges,
        node_count=len(node_list),
        edge_count=len(edges)
    )

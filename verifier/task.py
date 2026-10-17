"""
Knowledge Graph Builder Verifier (Task 2)
"""

from typing import Any


def verify_task(task_input: Any, agent_output: Any, workspace_path: str) -> dict:
    constraints = []

    # 1. Verification of Output Structure Existence
    has_graph = hasattr(agent_output, "nodes") and hasattr(agent_output, "edges")
    if not has_graph:
        return {
            "score": 0.0,
            "constraints": [{
                "id": "shape-check",
                "ok": False,
                "message": "agent_output missing 'nodes' or 'edges'"
            }]
        }

    nodes = agent_output.nodes
    edges = agent_output.edges

    # ---- Constraint 1: Nodes and edges are non-empty, and their counts match. ----
    ok_count = len(nodes) > 0 and len(edges) > 0 and getattr(agent_output, "node_count", 0) == len(nodes)
    constraints.append({
        "id": "graph-non-empty",
        "ok": ok_count,
        "message": "" if ok_count else "Nodes or edges are empty, or count mismatch"
    })

    # ---- Constraint 2: Validation of Node Label Conformity ----
    valid_labels = {"Company", "Industry", "Location", "Batch"}
    ok_labels = all(getattr(n, "label", None) in valid_labels for n in nodes)
    constraints.append({
        "id": "valid-node-labels",
        "ok": ok_labels,
        "message": "" if ok_labels else "Invalid node label detected"
    })

    # ---- Constraint 3: Validation of Edge Relation Compliance ----
    valid_relations = {"BELONGS_TO_BATCH", "LOCATED_IN", "BELONGS_TO_INDUSTRY", "COMPETES_WITH"}
    ok_relations = all(getattr(e, "relation", None) in valid_relations for e in edges)
    constraints.append({
        "id": "valid-edge-relations",
        "ok": ok_relations,
        "message": "" if ok_relations else "Invalid edge relation type detected"
    })

    score = 1.0 if all(c["ok"] for c in constraints) else 0.0
    return {
        "score": score,
        "constraints": constraints
    }

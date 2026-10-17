from types import SimpleNamespace
from verifier.task import verify_task


def test_verify_graph_gold():
    mock_agent_output = SimpleNamespace(
        nodes=[
            SimpleNamespace(id="company:doordash", label="Company", name="DoorDash", properties={}),
            SimpleNamespace(id="industry:consumer", label="Industry", name="CONSUMER", properties={}),
            SimpleNamespace(id="location:sf", label="Location", name="San Francisco", properties={}),
        ],
        edges=[
            SimpleNamespace(source_id="company:doordash", target_id="industry:consumer", relation="BELONGS_TO_INDUSTRY"),
            SimpleNamespace(source_id="company:doordash", target_id="location:sf", relation="LOCATED_IN"),
        ],
        node_count=3,
        edge_count=2,
    )

    result = verify_task(task_input={}, agent_output=mock_agent_output, workspace_path=".")
    assert result["score"] == 1.0


def test_verify_graph_broken():
    mock_broken_output = SimpleNamespace(
        nodes=[
            SimpleNamespace(id="n1", label="InvalidLabel", name="Wrong", properties={})
        ],
        edges=[],
        node_count=1,
        edge_count=0,
    )

    result = verify_task(task_input={}, agent_output=mock_broken_output, workspace_path=".")
    assert result["score"] == 0.0

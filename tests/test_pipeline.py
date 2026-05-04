from engine.orchestrator import run_pipeline

def test_pipeline():
    events = [
        {"message": "timeout error", "metrics": {"latency": 1000}},
        {"message": "retry failed", "metrics": {"retries": 2}}
    ]

    result = run_pipeline(events)
    assert isinstance(result, list)
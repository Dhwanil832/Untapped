import pytest
from agents.decision import decide_profile

def test_decision_pass():
    scores = {'Market': 5.0, 'Team': 6.0, 'Traction': 4.5, 'Product Clarity': 5.0}
    decision, rationale, cot = decide_profile({}, scores)
    assert decision == 'PASS'
    assert 'recommend PASS' in rationale
    assert any('Threshold' in step for step in cot)

def test_decision_invest():
    scores = {'Market': 8.0, 'Team': 9.0, 'Traction': 7.5, 'Product Clarity': 8.5}
    decision, rationale, cot = decide_profile({}, scores)
    assert decision == 'INVEST'
    assert 'recommend INVEST' in rationale
    assert any('Threshold' in step for step in cot)

if __name__ == "__main__":
    pytest.main()

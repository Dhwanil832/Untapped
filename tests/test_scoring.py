import pytest
from agents.scoring import score_profile

def test_score_market_high():
    profile = {"TAM": "2000000000"}
    scores, details = score_profile(profile)
    assert scores["Market"] == 8.5

def test_score_market_low():
    profile = {"TAM": "100000"}
    scores, details = score_profile(profile)
    assert scores["Market"] == 6.0

if __name__ == "__main__":
    pytest.main()
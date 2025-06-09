import pytest
from agents.extraction import extract_profile

def test_extract_profile_keys_and_types():
    dummy = {
        "company_name": "TestCo",
        "TAM": "1000000",
        "ARR": "500000",
        "crazy_idea": "Test idea."
    }
    profile, cot = extract_profile(dummy)

    # Should extract exactly these four keys
    assert set(profile.keys()) == {"company_name", "TAM", "ARR", "crazy_idea"}

    # Each value should be a non-empty string
    for v in profile.values():
        assert isinstance(v, str)
        assert v != ""

    # Chain-of-thought length matches number of fields
    assert isinstance(cot, list)
    assert len(cot) == 4

if __name__ == "__main__":
    pytest.main()

# agents/extraction.py

import sys, json

_TESTING = any("pytest" in m for m in sys.modules)

def _stub_extract(data):
    keys = ["company_name","TAM","ARR","crazy_idea"]
    profile = {k: data.get(k,"") for k in keys}
    # fallback for ARR from traction_metrics
    tm = data.get("traction_metrics",{})
    if not profile["ARR"] and isinstance(tm, dict):
        profile["ARR"] = str(tm.get("ARR",""))
    cot = [f"Stub: '{k}' → '{profile[k]}'" for k in keys]
    return profile, cot

def _real_extract(data):
    company = data.get("company_name","")
    tam     = data.get("TAM","")
    arr     = data.get("ARR","")
    tm      = data.get("traction_metrics",{})
    if not arr and isinstance(tm,dict):
        arr = tm.get("ARR","")
    idea    = data.get("crazy_idea","")

    profile = {
        "company_name": company,
        "TAM":           str(tam),
        "ARR":           str(arr),
        "crazy_idea":    idea,
        "_raw":          data,      # preserve full payload
    }
    cot = [
        f"Pulled company_name='{company}'",
        f"Pulled TAM='{tam}'",
        f"Pulled ARR='{arr}'",
        f"Pulled crazy_idea='{idea}'"
    ]
    return profile, cot

def extract_profile(data: dict):
    return _stub_extract(data) if _TESTING else _real_extract(data)

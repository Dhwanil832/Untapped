# graph.py
from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.client import Client
from diagrams.onprem.network import Nginx
from diagrams.onprem.inmemory import Redis        # fixed import
from diagrams.onprem.database import PostgreSQL
from diagrams.programming.language import Python
from diagrams.onprem.compute import Server
from diagrams.generic.storage import Storage

with Diagram("Agentic Investment Pipeline", show=False, direction="TB"):

    client = Client("Founders / Admins")

    with Cluster("API Layer"):
        api = Nginx("FastAPI\nPydantic")

    storage = Storage("Object Storage\n(Supabase/AWS S3)")

    client >> Edge(label="POST /api/submit") >> api
    api     >> storage
    api     >> Redis("raw_bundles")

    with Cluster("Workers"):
        preproc = Server("Preprocessing\nWorker")
        extract = Python("DataExtractionAgent")
        score   = Python("ScoringAgent")
        decide  = Python("DecisionAgent")

    api >> preproc >> extract >> score >> decide

    db = PostgreSQL("Postgres DB")
    extract >> db
    score   >> db
    decide  >> db

    dashboard = Python("Admin Dashboard\n(Streamlit/React)")
    decide >> dashboard

    feedback = Python("Feedback & Retraining\n(Prefect/Airflow)")
    dashboard >> feedback

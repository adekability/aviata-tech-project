from flask import Blueprint
from uuid import uuid4
import requests


airflow_bp = Blueprint(
    "airflow", __name__
)


@airflow_bp.route("/search", methods=["POST"])
def search_by_airflow():
    search_id = str(uuid4())
    provider_a_data = requests.post("http://localhost:8000/provider_a/search")
    provider_b_data = requests.post("http://localhost:8000/provider_b/search")
    return {"search_id": search_id}

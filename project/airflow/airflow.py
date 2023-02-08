from flask import Blueprint

airflow_bp = Blueprint(
    "airflow", __name__
)


@airflow_bp.route("/search", methods=["POST"])
def search_by_airflow():
    return {"status": "airflow"}

from flask import Blueprint
import time

provider_a_bp = Blueprint(
    "provider_a", __name__
)


@provider_a_bp.route("/search", methods=["POST"])
def search_by_provider_a():
    time.sleep(30)
    return {"status": "provider_a"}

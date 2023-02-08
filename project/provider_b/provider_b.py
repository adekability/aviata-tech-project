from flask import Blueprint
import time

provider_b_bp = Blueprint(
    "provider_b", __name__
)


@provider_b_bp.route("/search", methods=["POST"])
def search_by_provider_b():
    time.sleep(60)
    return {"status": "provider_b"}

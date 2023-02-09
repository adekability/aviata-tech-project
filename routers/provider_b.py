from flask import Blueprint
import time
import json

provider_b_bp = Blueprint(
    "provider_b", __name__
)


@provider_b_bp.route("/search", methods=["POST"])
def search_by_provider_b():
    time.sleep(60)
    provider_b_text = open("./files/response_b.json")
    provider_b_data = json.load(provider_b_text)
    return provider_b_data

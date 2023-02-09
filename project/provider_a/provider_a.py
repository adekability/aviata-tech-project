from flask import Blueprint
import time
import json

provider_a_bp = Blueprint(
    "provider_a", __name__
)


@provider_a_bp.route("/search", methods=["POST"])
def search_by_provider_a():
    time.sleep(30)
    provider_a_text = open("./files/response_a.json")
    provider_a_data = json.load(provider_a_text)
    return provider_a_data

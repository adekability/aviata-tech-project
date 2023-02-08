from flask import Blueprint

provider_a_bp = Blueprint(
    "provider_a", __name__
)


@provider_a_bp.route("/search", methods=["POST"])
def search_by_provider_a():
    return {"status": "provider_a"}

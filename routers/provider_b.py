from fastapi import APIRouter
import json
import time


router = APIRouter(
    prefix="/provider_b",
    tags=["provider_b"],
    responses={404: {"description": "Not found"}},
)


@router.post("/search")
async def search_by_provider_b():
    time.sleep(60)
    provider_b_text = open("./files/response_a.json")
    provider_b_data = json.load(provider_b_text)

    return provider_b_data

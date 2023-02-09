from fastapi import APIRouter
import json
import time

router = APIRouter(
    prefix="/provider_a",
    tags=["provider_a"],
    responses={404: {"description": "Not found"}},
)


@router.post("/search")
async def search_by_provider_a():
    time.sleep(30)
    provider_a_text = open("./files/response_a.json")
    provider_a_data = json.load(provider_a_text)

    return provider_a_data

from fastapi import APIRouter, BackgroundTasks
from models import SearchResult
from sqlalchemy.orm.attributes import flag_modified
from extensions import db_session
import aiohttp


router = APIRouter(
    prefix="/airflow",
    tags=["airflow"],
    responses={404: {"description": "Not found"}},
)


@router.post("/search")
async def search_by_airflow(background_tasks: BackgroundTasks):
    search_result = SearchResult(status='pending', items=[])
    background_tasks.add_task(update_search_result, search_result.search_id)
    db_session.add(search_result)
    db_session.commit()
    return {"search_id": search_result.search_id}


async def update_search_result(search_id):
    search_result = SearchResult.query.filter_by(search_id=search_id).first()
    async with aiohttp.ClientSession() as session:
        async with session.post('http://localhost:9000/provider_a/search') as provider_a_resp:
            provider_a_data = await provider_a_resp.json()
            search_result.items.append(provider_a_data)
            flag_modified(search_result, "items")
            db_session.commit()
        async with session.post('http://localhost:9000/provider_b/search') as provider_b_resp:
            provider_b_data = await provider_b_resp.json()
            search_result.items.append(provider_b_data)
            flag_modified(search_result, "items")
            db_session.commit()
    search_result.status = 'completed'
    db_session.commit()

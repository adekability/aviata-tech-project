from fastapi import FastAPI
from routers import provider_a, provider_b, airflow


app = FastAPI()


app.include_router(provider_a.router)
app.include_router(provider_b.router)
app.include_router(airflow.router)

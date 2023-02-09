from fastapi import FastAPI
from routers import provider_a, provider_b, airflow
import uvicorn

app = FastAPI()


app.include_router(provider_a.router)
app.include_router(provider_b.router)
app.include_router(airflow.router)

if __name__ == '__main__':
    uvicorn.run(app, port=9000)

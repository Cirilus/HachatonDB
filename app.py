import sys

from fastapi import FastAPI
from loguru import logger
from starlette.middleware.cors import CORSMiddleware

from configs.Environment import get_environment_variables

from routing.v1.Rating import router as rating_router
from routing.v1.ML import router as ml_router

app = FastAPI(openapi_url="/core/openapi.json", docs_url="/core/docs")

app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


env = get_environment_variables()

if not env.DEBUG:
    logger.remove()
    logger.add(sys.stdout, level="INFO")

app.include_router(rating_router)
app.include_router(ml_router)
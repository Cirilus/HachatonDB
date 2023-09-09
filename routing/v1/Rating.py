from fastapi import APIRouter

from schemas.Rating import RatingChoice

router = APIRouter(prefix="/api/v1/rating", tags=["rating"])


@router.get(
    "/",
    description="dict of the enum"
)
async def get():
    return {e.name: e.value for e in RatingChoice}


@router.get(
    "/reverse",
    description="reverse dict of the enum"
)
async def get():
    return {e.value: e.name for e in RatingChoice}
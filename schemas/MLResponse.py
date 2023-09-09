from pydantic import BaseModel

from schemas.Rating import RatingChoice


class MlResponse(BaseModel):
    rating: RatingChoice
    negative: list[str]
    positive: list[str]


class MLTextRequest(BaseModel):
    text: str
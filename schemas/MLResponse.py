from pydantic import BaseModel

from schemas.Rating import RatingChoice


class MlResponse(BaseModel):
    rating: RatingChoice
    rating_name: str
    company_name: str
    negative: list[str]
    positive: list[str]


class MLTextRequest(BaseModel):
    text: str
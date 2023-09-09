import os
import io
import random

from fastapi import APIRouter, UploadFile, HTTPException
from starlette import status

from schemas.Rating import RatingChoice
from schemas.MLResponse import MLTextRequest, MlResponse
from docx import Document

from utils.utils import get_main_words

router = APIRouter(prefix="/api/v1/ml", tags=["ml"])


@router.post(
    "/file",
    response_model=MlResponse,
 )
async def get_file(file: UploadFile):
    file_extension = os.path.splitext(file.filename)[1]
    if file_extension not in {".txt", ".docx"}:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="File must be a .txt or .docx file")

    text = ""

    if file_extension == ".txt":
        text = await file.read()
        text = text.decode("utf-8")

    if file_extension == ".docx":
        docx_content = await file.read()
        docx_document = Document(io.BytesIO(docx_content))
        text = "\n".join([para.text for para in docx_document.paragraphs])

    if text == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="the file must not to be empty")

    positive, negative = get_main_words(text)
    rating = random.choice(list(RatingChoice))
    return {
        "positive": positive,
        "negative": negative,
        "rating": rating,
        "rating_name": rating.name,
    }


@router.post(
    "/text",
    response_model=MlResponse,
)
async def get_text(req: MLTextRequest):

    if req.text == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="the file must not to be empty")

    positive, negative = get_main_words(req.text)
    rating = random.choice(list(RatingChoice))
    return {
        "positive": positive,
        "negative": negative,
        "rating": rating,
        "rating_name": rating.name,
    }
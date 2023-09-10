import os
import io
import random

from fastapi import APIRouter, UploadFile, HTTPException
from starlette import status

from schemas.Rating import RatingChoice
from schemas.MLResponse import MLTextRequest, MlResponse
from docx import Document

from MLModel.main import tokenizer, model, get_main_words, predict_text

router = APIRouter(prefix="/api/v1/ml", tags=["ml"])


@router.post(
    "/file",
    response_model=MlResponse,
 )
async def get_file(file: UploadFile):
    file_extension = os.path.splitext(file.filename)[1].lower()
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

    positive, negative = get_main_words(text, model, tokenizer)
    rating = predict_text(text, model, tokenizer)
    enum = [el.value for el in RatingChoice]
    enum_dict = {el.value: el.name for el in RatingChoice}
    rating = enum[rating]
    rating_name = enum_dict[rating]
    return {
        "positive": positive,
        "negative": negative,
        "rating": rating,
        "rating_name": rating_name,
        "company_name": "Central Bank",
    }


@router.post(
    "/text",
    response_model=MlResponse,
)
async def get_text(req: MLTextRequest):

    if req.text == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="the file must not to be empty")

    positive, negative = get_main_words(req.text, model, tokenizer)
    rating = predict_text(req.text, model, tokenizer)
    enum = [el.value for el in RatingChoice]
    enum_dict = {el.value: el.name for el in RatingChoice}
    rating = enum[rating]
    rating_name = enum_dict[rating]
    return {
        "positive": positive,
        "negative": negative,
        "rating": rating,
        "rating_name": rating_name,
        "company_name": "Central Bank",
    }
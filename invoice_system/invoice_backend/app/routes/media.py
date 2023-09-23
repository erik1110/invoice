from io import BytesIO
from bson import ObjectId
from fastapi import APIRouter, Body, Request, Query, HTTPException, UploadFile, File
from fastapi.responses import StreamingResponse
from app.models.media import Media
from app.utils.responseHandler import success_response
from datetime import datetime
from rich.console import Console
import mimetypes
import pytz

console = Console()
router = APIRouter()


tz = pytz.timezone('Asia/Taipei')

@router.post("/upload", summary="上傳媒體檔案")
async def upload_file(request: Request,
                      file: UploadFile = File(...)):
    file_extension = file.filename.split(".")[-1]
    if file_extension not in ["jpg", "jpeg", "png", "gif"]:
        raise HTTPException(400, "File Type occurred error.")
    mime_type, _ = mimetypes.guess_type(file.filename)
    content_type = mime_type if mime_type else "application/octet-stream"
    file_content = await file.read()

    media = Media(
        stream=file_content,
        content_type=content_type,
        created_timestamp=datetime.now(tz)
    )
    await media.save()

    return success_response(message="媒體上傳成功", data=media.id)

@router.get("", summary="查詢檔案")
async def get_media(request: Request,
                    mediaId: str = Query(..., description="mediaId")):
    if not ObjectId.is_valid(mediaId):
        raise HTTPException(400, f"Invalid field type in {mediaId}. Expected: ObjectId")
    media = await Media.get(mediaId)
    if media is None:
        raise HTTPException(400, f"Invalid metadataId: {mediaId}.")
    return StreamingResponse(BytesIO(media.stream), media_type=media.content_type)
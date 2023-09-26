from fastapi import APIRouter, Body, Request
from app.schema.invoice import SaveData
from app.utils.responseHandler import success_response
from app.utils.save import perform_save_data
from rich.console import Console
import pytz

console = Console()
router = APIRouter()


tz = pytz.timezone('Asia/Taipei')

@router.post("", summary="儲存資料")
async def save_invoice(request: Request, save_data: SaveData = Body(..., examples=SaveData.Config.examples)):
    data = await perform_save_data(save_data)
    return success_response(message="儲存資料成功", data=data)

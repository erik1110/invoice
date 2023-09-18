from fastapi import APIRouter

router = APIRouter()

@router.get("", summary="Hello World!")
async def hello_world():
    """Hello World"""
    return "Hello World"
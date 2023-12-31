from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.utils import get_openapi
from app.routes import docs, test, media, invoice
from app.database import initiate_database

# 自訂 Swagger 文件
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="My Invoice Sysyem",
        version="1.0.0",
        description="我的發票系統",
        routes=app.routes,
    )

    app.openapi_schema = openapi_schema
    return app.openapi_schema

def get_application():
    app = FastAPI()
    app.openapi = custom_openapi

    origins = ["*"]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(docs.router)
    app.include_router(test.router, tags=["測試"], prefix="/hello")
    app.include_router(media.router, tags=["圖片"], prefix="/media")
    app.include_router(invoice.router, tags=["發票"], prefix="/invoice")
    app.mount("/static", StaticFiles(directory="static"), name="static")

    return app

app = get_application()

@app.on_event("startup")
async def start_database():
    await initiate_database()

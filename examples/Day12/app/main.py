from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.utils import get_openapi
from app.routes import docs, test

# 自訂 Swagger 文件
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="FastAPI範例",
        version="1.0.0",
        description="這是好吃的範例",
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
    app.mount("/static", StaticFiles(directory="static"), name="static")

    return app

app = get_application()

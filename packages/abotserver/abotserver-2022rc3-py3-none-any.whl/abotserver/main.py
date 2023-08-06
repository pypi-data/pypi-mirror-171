from fastapi import FastAPI
from .routers import index, aliyun, hikvision


app = FastAPI(title="ABOT API Docs", version="v1.0")

app.include_router(index.router, tags=["index"])
app.include_router(aliyun.router, tags=["aliyun"])
app.include_router(hikvision.router, tags=["hikvision"])

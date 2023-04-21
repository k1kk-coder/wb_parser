from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import allow_credentials, allow_headers, allow_methods, origins
from goods.router import router as goods_router

app = FastAPI(title='WB_PARSER')

'''Configure CORS'''
app.add_middleware(
    CORSMiddleware,
    allow_origins=[origins],
    allow_credentials=allow_credentials,
    allow_methods=allow_methods,
    allow_headers=allow_headers,
)

app.include_router(goods_router, prefix='/api')

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from goods.router import router as goods_router
from config import origins, allow_methods, allow_headers, allow_credentials


app = FastAPI(title='WB_PARSER')

'''Configure CORS'''
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=allow_credentials,
    allow_methods=allow_methods,
    allow_headers=allow_headers,
)

app.include_router(goods_router, prefix='/api')

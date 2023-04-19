from fastapi import FastAPI
from goods.router import router as goods_router


app = FastAPI(title='WB_PARSER')


app.include_router(goods_router, prefix='/api')

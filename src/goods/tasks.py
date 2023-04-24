import asyncio
from datetime import datetime, timedelta

from celery import Celery
from sqlalchemy import select, update
from sqlalchemy.exc import IntegrityError

from config import redis_host
from database import async_session_maker

from .models import product
from .parser import parse_data

celery = Celery(
    'tasks',
    broker=f'redis://{redis_host}:6379',
    backend=f'redis://{redis_host}:6379'
)


async def update_product_data() -> None:
    async with async_session_maker() as session:
        try:
            query = select(product)
            result = await session.execute(query)
            products = result.all()
            for p in products:
                data = await parse_data(p.nm_id)
                colors = None if not data['colors'] else ', '.join(
                    [s.get('name') for s in data['colors']])
                stmt = update(product).where(
                    product.c.nm_id == p.nm_id).values(
                    name=data['name'],
                    brand=data['brand'],
                    brand_id=data['brandId'],
                    site_brand_id=data['siteBrandId'],
                    supplier_id=data['supplierId'],
                    sale=data['sale'],
                    price=data['priceU'],
                    sale_price=data['salePriceU'],
                    rating=data['rating'],
                    feedbacks=data['feedbacks'],
                    colors=colors,
                    last_upd=datetime.now()
                )
                await session.execute(stmt)
            await session.commit()
        except IntegrityError:
            await session.rollback()


@celery.task
def update_product_data_task():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(update_product_data())
    return 'success'


"""Information update every 12 hours"""
celery.conf.beat_schedule = {
    'update_product_data': {
        'task': 'goods.tasks.update_product_data_task',
        'schedule': timedelta(hours=12)
    },
}

celery.conf.timezone = 'UTC'

from datetime import datetime

from sqlalchemy import (BIGINT, Column, DateTime, Integer, MetaData, Numeric,
                        String, Table)

metadata: MetaData = MetaData()


product: Table = Table(
    'product',
    metadata,
    Column('nm_id', BIGINT, nullable=False, primary_key=True),
    Column('name', String, nullable=False),
    Column('brand', String, nullable=False),
    Column('brand_id', Integer, nullable=False),
    Column('site_brand_id', Integer, nullable=False),
    Column('supplier_id', Integer, nullable=False),
    Column('sale', Integer, nullable=False),
    Column('price', Numeric, nullable=False),
    Column('sale_price', Numeric, nullable=False),
    Column('rating', Integer, nullable=False),
    Column('feedbacks', Integer, nullable=False),
    Column('colors', String, nullable=True),
    Column('last_upd', DateTime, default=datetime.now)
)

from uuid import uuid4
from sqlalchemy import String, Integer, Table, Column, Numeric, MetaData, UUID


metadata: MetaData = MetaData()


product: Table = Table(
    'product',
    metadata,
    Column(
        'id', UUID(as_uuid=True), primary_key=True, default=uuid4, index=True),
    Column('nm_id', Integer, nullable=False),
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
    Column('colors', String, nullable=False)
)

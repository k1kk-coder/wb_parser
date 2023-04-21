from database import get_async_session
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse, Response
from sqlalchemy import delete, insert, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from goods.models import product

from .parser import parse_data
from .schemas import Product, RequestIdSchema, example_200_response

router: APIRouter = APIRouter(
    tags=['goods']
)


@router.post(
    '/product',
    responses={
        200: {
            'description': 'Successful Response',
            'content': {
                'application/json': {
                    "example": example_200_response
                }
            }
        },
        400: {
            'description': 'Bad Request',
            'content': {
                'application/json': {
                    'example': {
                        'detail': 'THIS_PRODUCT_IS_ALREADY_IN_THE_DATABASE'}
                }
            }
        },
        403: {
            'description': 'Forbidden',
            'content': {
                'application/json': {
                    'example': {
                        'detail': 'INVALID_PRODUCT_ID'}
                }
            }
        }
    })
async def add_product(
    entity: RequestIdSchema,
    session: AsyncSession = Depends(get_async_session)
) -> Response:
    data = await parse_data(entity.product_id)
    if data == 'INVALID_PRODUCT_ID':
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='INVALID_PRODUCT_ID'
        )
    else:
        try:
            data = await parse_data(entity.product_id)
            colors = None if not data['colors'] else ', '.join(
                [s.get('name') for s in data['colors']])
            stmt = insert(product).values(
                nm_id=data['id'],
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
                colors=colors
            )
            await session.execute(stmt)
            await session.commit()
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={
                    'nm_id': data['id'],
                    'name': data['name'],
                    'brand': data['brand'],
                    'brand_id': data['brandId'],
                    'site_brand_id': data['siteBrandId'],
                    'supplier_id': data['supplierId'],
                    'sale': data['sale'],
                    'price': data['priceU'],
                    'sale_price': data['salePriceU'],
                    'rating': data['rating'],
                    'feedbacks': data['feedbacks'],
                    'colors': colors
                }
            )
        except IntegrityError:
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={'detail': 'THIS_PRODUCT_IS_ALREADY_IN_THE_DATABASE'}
            )


@router.get('/products', response_model=list[Product])
async def get_products(
    session: AsyncSession = Depends(get_async_session)
) -> list[Product]:
    query = select(product)
    result = await session.execute(query)
    return result.all()


@router.get(
    '/product/{product_id}',
    response_model=Product,
    responses={
        400: {
            "description": "Bad Request",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "PRODUCT_WITH_THIS_ID_WAS_NOT_FOUND"}
                }
            }
        }
    })
async def get_product_by_id(
    product_id: int,
    session: AsyncSession = Depends(get_async_session)
) -> Product:
    query = select(product).where(product.c.nm_id == product_id)
    result = await session.execute(query)
    value = result.one_or_none()
    if value is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='PRODUCT_WITH_THIS_ID_WAS_NOT_FOUND')
    return value


@router.delete(
    '/product/{product_id}',
    response_model=Product,
    responses={
        400: {
            "description": "Bad Request",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "PRODUCT_WITH_THIS_ID_WAS_NOT_FOUND"}
                }
            }
        }
    })
async def delete_product(
    product_id: int,
    session: AsyncSession = Depends(get_async_session)
) -> Product:
    stmt = delete(product).where(
        product.c.nm_id == product_id).returning(product)
    result = await session.execute(stmt)
    value = result.one_or_none()
    if value is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='PRODUCT_WITH_THIS_ID_WAS_NOT_FOUND'
        )
    await session.commit()
    return value

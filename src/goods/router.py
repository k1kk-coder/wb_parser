from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse, Response
from sqlalchemy import delete, insert, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from goods.models import product

from .parser import parse_data
from .schemas import (Product, RequestIdSchema, already_exists_response_409,
                      forbidden_response_400, product_not_found_response_404,
                      successful_response_200)

router: APIRouter = APIRouter(
    tags=['goods']
)


@router.post(
    '/product',
    response_model=Product,
    responses={
        200: successful_response_200,
        400: forbidden_response_400,
        409: already_exists_response_409,
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
            status_code=status.HTTP_409_CONFLICT,
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
        404: product_not_found_response_404
    })
async def get_product_by_id(
    product_id: int,
    session: AsyncSession = Depends(get_async_session)
) -> Product:
    query = select(product).where(product.c.nm_id == product_id)
    result = await session.execute(query)
    value = result.one_or_none()
    if value is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='PRODUCT_WITH_THIS_ID_WAS_NOT_FOUND')
    return value


@router.delete(
    '/product/{product_id}',
    response_model=Product,
    responses={
        404: product_not_found_response_404
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
            status_code=status.HTTP_404_NOT_FOUND,
            detail='PRODUCT_WITH_THIS_ID_WAS_NOT_FOUND'
        )
    await session.commit()
    return value

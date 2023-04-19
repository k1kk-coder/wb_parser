import requests


url: str = ('https://card.wb.ru/cards/detail?curr=rub&dest=-1257786&'
            'regions=80,64,38,4,115,83,33,68,70,69,30,86,75,40,'
            '1,66,48,110,31,22,71,114&spp=0&nm=')


async def parse_data(id: int) -> dict:
    '''Main func for parse data from wb'''
    response = requests.get(f"{url}{id}").json()
    result: dict = {}
    list_of_fields: list = [
        'id', 'name', 'brand', 'brandId', 'siteBrandId', 'supplierId',
        'sale', 'priceU', 'salePriceU', 'rating', 'feedbacks', 'colors']
    for field in list_of_fields:
        data = response.get('data').get('products')[0].get(field)
        if field == 'priceU' or field == 'salePriceU':
            result[field] = data // 100
        else:
            result[field] = data
    return result

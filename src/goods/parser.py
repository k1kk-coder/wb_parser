import requests
from random import choice


desktop_agents: list[str] = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '
    '(KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
    '(KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
    '(KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) '
    'AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
    ]


def random_headers() -> dict[str, str]:
    return {
        'User-Agent': choice(desktop_agents),
        'Accept': ('text/html,application/xhtml+xml,application/xml;q=0.9,'
                   'image/webp,*/*;q=0.8')
    }


url: str = ('https://card.wb.ru/cards/detail?curr=rub&dest=-1257786&'
            'regions=80,64,38,4,115,83,33,68,70,69,30,86,75,40,'
            '1,66,48,110,31,22,71,114&spp=0&nm=')


async def parse_data(id: int) -> dict | str:
    '''Main func for parse data from wb'''
    try:
        response = requests.get(f"{url}{id}", headers=random_headers()).json()
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
    except IndexError:
        return 'INVALID_PRODUCT_ID'

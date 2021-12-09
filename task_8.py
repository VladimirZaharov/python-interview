import asyncio
from urllib.request import urlopen

urls = ['127.0.0.1/wear', '127.0.0.1/electric']

async def get_data(url):
    print(f'Getting {url}')
    data = urlopen(url).read()


loop = asyncio.get_event_loop()
loop.run_until_complete(
    asyncio.wait([
        get_data(url)
        for url in urls
    ])
)
loop.close()
# AIOHTTP > Asyncing programming
# Tutorial from John Watson Rooney YouTube channel

# Useful for getting data from a list of URLs all at the same time. 

import asyncio
import aiohttp
import requests
from bs4 import BeautifulSoup


# DEMO from Docs: 
'''
async def main(): 

    async with aiohttp.ClientSession() as session: 
        async with session.get('http://python.org') as response:
            print('Status Code:', response.status)
            print('Content-type:', response.headers['content-type'])

            html = await response.text()
            print('Body:', html[:15], '...')

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

'''

# MAIN: 
async def get_page(session, url):
    async with session.get(url) as response: 
        return await response.text()

async def get_all(session, urls):
    tasks = []
    for url in urls: 
        task = asyncio.create_task(get_page(session, url))
        tasks.append(task)
    results = await asyncio.gather(*tasks)
    return results

async def main(urls):
    async with aiohttp.ClientSession() as session: 
        data = await get_all(session, urls)
        return data

def parse(results):
    for html in results: 
        soup = BeautifulSoup(html, 'html.parser')
        print(soup.find('form', {'class': 'form-horizontal'}).text.strip())
    return

if __name__ == '__main__':
    urls = [
        'http://books.toscrape.com/catalogue/page-1.html',
        'http://books.toscrape.com/catalogue/page-2.html',
        'http://books.toscrape.com/catalogue/page-3.html',
    ]

    results = asyncio.run(main(urls))
    parse(results)
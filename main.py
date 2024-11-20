from typing import Optional
from fastapi import Depends, FastAPI
from scrapper.main import Scrapper
from authentication.main import Authenticator
import logging
import uuid
from scrapper.interface import ScrapeRequest, GetDataFromCacheRequest
import asyncio 

scrapper_client = Scrapper()

logging.basicConfig(
    filename='logs',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

app = FastAPI()

@app.get("/scrape_pages")
async def scrape_pages(pg_no: int= 2, proxy: Optional[str] = None, token: str = Depends(Authenticator.authenticate)):
    transaction_id = uuid.uuid1()
    logging.info({'transaction_id': transaction_id, 'pg_no': pg_no, 'proxy': proxy, 'methodName': 'scrapePage'})
    return await scrapper_client.scrape_pages(pg_no=pg_no, proxy=proxy, transaction_id=transaction_id)

@app.post("/get_scraped_data_from_cache_by_id")
async def get_data_from_cache(request: GetDataFromCacheRequest):
    transaction_id = uuid.uuid1()
    logging.info({'transaction_id': transaction_id, 'methodName': 'get_data_from_cache'})
    return await scrapper_client.get_data_from_cache(request=request)

@app.get("/get_all_items_from_database")
async def get_all_items_from_database():
    transaction_id = uuid.uuid1()
    logging.info({'transaction_id': transaction_id, 'methodName': 'get_all_items_from_database'})
    return await scrapper_client.get_all_items_from_database()


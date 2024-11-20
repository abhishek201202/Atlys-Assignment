from typing import Dict, Optional, List
from .dm.main import scrapper_dml
from .cache.main import cache_dml
from slack import SlackClient
from scrapper.utils import Product, retryFailedPages, scrapePageTask
from scrapper.interface import GetDataFromCacheRequest, NotificationRequest
import asyncio

class Scrapper:
    def __init__(self, proxy: Optional[str] = None):
        self.proxy = proxy
    
    async def scrape_pages(self, pg_no: int, proxy: Optional[str], transaction_id: str = 'default') -> Dict[str, List[Product]]:
        all_products: List[Product] = []
        failed_pages: List[int] = []
        proxies = {}
        if proxy:
            proxies = {
                "http": f'http://{proxy}',
                "https": f'http://{proxy}',
            }
        tasks = []
        for page in range(1, pg_no + 1):
            tasks.append(scrapePageTask(page, proxies, failed_pages, all_products))

        await asyncio.gather(*tasks)

        await cache_dml.upsert(data=all_products)
        await scrapper_dml.insert(data=all_products, transaction_id=transaction_id)

        if failed_pages:
            asyncio.create_task(retryFailedPages(failed_pages=failed_pages, proxies=proxies))

        asyncio.create_task(SlackClient.sendMessage(NotificationRequest(pagesToBeScraped=pg_no, transaction_id=transaction_id, pagesScrapedSuccessfully=pg_no-len(failed_pages), productsScraped=len(all_products))))

        return {'data': all_products}
    
    async def get_data_from_cache(self, request: GetDataFromCacheRequest)-> Dict[str, List[Product]]:
        return {'data': await cache_dml.get(request.item_name)}
    
    async def get_all_items_from_database(self) -> Dict[str, List[Product]]:
        return {'data': await scrapper_dml.get()}

from scrapper.interface import NotificationRequest

class SlackClient:
    async def sendMessage(data: NotificationRequest):
        print(f"Parsing status of transaction_id :: {data.transaction_id}")
        print(f"Total pages requested :: {data.pagesToBeScraped}")
        print(f"Pages scraped successfully :: {data.pagesScrapedSuccessfully}")
        print(f"Pages up for retry :: {data.pagesToBeScraped-data.pagesScrapedSuccessfully}")
        print(f"Total products scraped :: {data.productsScraped}")
from cachetools import TTLCache
cache = TTLCache(maxsize=10000, ttl=3000)

class cache_dml:
    async def upsert(data):
        for item in data:
            cacheData = cache.get(item['product_title'])
            if cacheData is None:
                cache[item['product_title']] = item
            else:
                if cacheData['product_price'] != item['product_price']:
                    cache[item['product_title']] = item
        print('cache update successfully')

    async def get(data):
        objects_list = []
        for item in data:
            objects_list.append(cache.get(item))
        return objects_list

## Steps To Run The Code: 
# 1. Run the following command
```bash
python3 --version
pip3 --version
pip3 install --upgrade pip
pip3 install virtualenv
python3 -m venv .venv
source .venv/bin/activate
pip3 install "fastapi[standard]"
pip3 install cachetools
pip3 install aiohttp
pip3 install requests_html
pip3 install lxml_html_clean
pip3 install proxy.py
```

# 2. After installation run this command to start the server
```bash
fastapi dev main.py
```

# 3. Open another terminal and start proxy
```bash
proxy --hostname 127.0.0.1 --port 8765
```

# 4. Curls to test the Apis

## 4.1 Scrape Data
```bash
curl --location 'http://localhost:8000/scrape_pages?proxy=127.0.0.1%3A8765&pg_no=12' \
--header 'X-Token: atlys-token'
```

## 4.2 Fetch data from cache
```bash
curl --location 'http://localhost:8000/get_scraped_data_from_cache_by_id' \
--header 'X-Token: testing-token' \
--header 'Content-Type: application/json' \
--data '{
    "item_name": ["1 x GDC Extraction Forceps Lo..."]
}'
```

## 4.2 Fetch data from local database
```bash
curl --location 'http://localhost:8000/get_all_items_from_database' \
--header 'X-Token: atlys-token'
```

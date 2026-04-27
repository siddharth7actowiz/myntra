#
# import scrapy
# from ..pipelines import MyntraPipeline
# from urllib.parse import urlencode,urljoin
# import json
# import gzip
# import os
# from ..cookies_extract import get_cookies
# #to store saved response in a folder
# BACKUP=r"D:\Scrapy\myntra\myntra\backup_pages\product_links"
#
# def load_cookies():
#     with open("cookies.json", "r") as f:
#         return json.load(f)
#
# #spider Class
# class Product_link(scrapy.Spider):
#     name = "prodlinks"
#
#     headers = {
#         'accept': 'application/json',
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
#         'referer': 'https://www.myntra.com/',
#     }
#     # multiprocessing - taking start and end args to run multiple processes
#     def __init__(self, start=None, end=None, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.start_index = int(start) if start is not None else 0
#         self.end_index = int(end) if end is not None else None
#         self.cookies=load_cookies()
#
#     # creating pipeline instance (keeping as you used)
#     pipeline = MyntraPipeline()
#
#     def start_requests(self):
#         all_items = list(self.pipeline.fetch_from_db())
#         total = len(all_items)
#         print(f"Total items in DB: {total}")
#
#         end = min(self.end_index, total) if self.end_index is not None else total
#         start = min(self.start_index, total)
#
#         print(f"Processing chunk: {start} to {end}")
#         chunk = all_items[start:end]
#
#         if not chunk:
#             print("No items in this range..!")
#             return
#
#         for category, subcategory, link in chunk:
#             print(f"Processing: {category} > {subcategory} > {link}")
#
#             demolink = link.rstrip('/').split('?')[0].split('/')[-1]
#
#             page_number = 1
#             params = {
#                 'rows': '50',
#                 'o': '249',
#                 'plaEnabled': 'true',
#                 'xdEnabled': 'false',
#                 'isFacet': 'true',
#                 'p': str(page_number),
#                 'pincode': '380008',
#             }
#
#             api = f"https://www.myntra.com/gateway/v4/search/{demolink}?{urlencode(params)}"
#
#             yield scrapy.Request(
#                 url=api,
#                 callback=self.parse,
#                 headers=self.headers,
#                 cookies=self.cookies,
#                 meta={
#                     "category": category,
#                     "subcategory": subcategory,
#                     "link": link,
#                     "demolink": demolink,
#                     "page_number": page_number,
#                 }
#             )
#
#     def parse(self, response):
#         print(f"Parsing: {response.status} - {response.url}")
#
#         category = response.meta["category"]
#         subcategory = response.meta["subcategory"]
#         link = response.meta["link"]
#         page_number = response.meta["page_number"]
#         demolink = response.meta["demolink"]
#
#         cat_hi = {
#             "l1": category,
#             "l2": subcategory
#         }
#
#         data = response.json()
#
#         # safe filenames
#         safe_cat = category.replace("/", "_").replace(" ", "_")
#         safe_sub = subcategory.replace("/", "_").replace(" ", "_")
#
#         # save each page separately
#
#         folder_name = f"{safe_cat}_{safe_sub}"
#
#         # Create full folder path
#         folder_path = os.path.join(BACKUP, folder_name)
#
#         # Ensure folder exists
#         os.makedirs(folder_path, exist_ok=True)
#
#         # Create file path
#         file_path = os.path.join(folder_path, f"{safe_cat}_{safe_sub}_{page_number}.json.gz")
#
#         # Write file
#         with gzip.open(file_path, "wt", encoding="utf-8") as f:
#             json.dump(data, f, indent=4)
#         # extract products
#         all_products = (data.get("products") or []) + (data.get("plaProducts") or [])
#         for product in all_products:
#             print(
#                 f"Found product: {product.get('productName')} (ID: {product.get('productId')}) {product.get('landingPageUrl')}")
#
#             yield {
#                 "product_name": product.get("productName"),
#                 "product_id": product.get("productId"),
#                 "category_hierarchy": json.dumps(cat_hi),
#                 "product_link": urljoin("https://www.myntra.com/", product.get("landingPageUrl", "")),
#                 "status": "pending"
#             }
#
#         # pagination
#         if data.get("hasNextPage") and all_products:
#             page_number += 1
#
#             params = {
#                 'rows': '50',
#                 'o': '249',
#                 'plaEnabled': 'true',
#                 'xdEnabled': 'false',
#                 'isFacet': 'true',
#                 'p': str(page_number),
#                 'pincode': '380008',
#             }
#
#             api = f"https://www.myntra.com/gateway/v4/search/{demolink}?{urlencode(params)}"
#
#             yield scrapy.Request(
#                 url=api,
#                 callback=self.parse,
#                 headers=self.headers,
#                 cookies=self.cookies,
#                 meta={
#                     "category": category,
#                     "subcategory": subcategory,
#                     "link": link,
#                     "demolink": demolink,
#                     "page_number": page_number,
#                 }
#              )
#         else:
#             # update status only after full pagination
#             self.pipeline.update_status(link)
#

import scrapy
import json
import os
import gzip
from urllib.parse import urlencode, urljoin
from datetime import datetime

from ..pipelines import MyntraPipeline

BACKUP = r"D:\Scrapy\myntra\myntra\backup_pages2\product_links"


def load_cookies():
    with open("cookies.json", "r") as f:
        return json.load(f)


class Product_link(scrapy.Spider):
    name = "prodlinks"

    headers = {
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9',
        'app': 'web',
        'content-type': 'application/json',
        'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjMwNjIwNzEiLCJhcCI6IjcxODQwNzY0MyIsImlkIjoiZTYwYTZkMjk0MjI1YTg1ZiIsInRyIjoiODY4NjRlOTMwNGE2NTE0N2NiNWRhNTA4ZWMyNjlmZmUiLCJ0aSI6MTc3NzI4MTA1ODkyOSwidGsiOiI2Mjk1Mjg2In19',
        'pagination-context': '{"productRack":{"dsCnsdrd":0,"tp":"nonDS","cntCnsdrd":0,"slrCnsdrd":0,"cncrnCnsdrd":0},"scImgVideoOffset":"0_0","v":1.0,"productsRowsShown":25,"paginationCacheKey":"8cd0647f-10e6-4fe0-bec3-30daf196af2d","inorganicRowsShown":3,"plaContext":"eyJvcmdhbmljQ3Vyc29yTWFyayI6IkFva0lRRUFBQUVFRlAvQUFBQUFBQUFCUWtvQU5YNmNIWGV3Y2NNRGRoNjJaQTFLSmxvMEJNREJmYzNSNWJHVmZNemN3TURjMU1EWVx1MDAzZCIsInBsYU9mZnNldCI6MCwib3JnYW5pY09mZnNldCI6MzgsImV4cGxvcmVPZmZzZXQiOjAsImZjY1BsYU9mZnNldCI6MTMsInNlYXJjaFBpYW5vUGxhT2Zmc2V0IjoxMiwiaW5maW5pdGVTY3JvbGxQaWFub1BsYU9mZnNldCI6MCwidG9zUGlhbm9QbGFPZmZzZXQiOjEsIm9yZ2FuaWNDb25zdW1lZENvdW50IjozOCwiYWRzQ29uc3VtZWRDb3VudCI6MTIsImV4cGxvcmVDb25zdW1lZENvdW50IjowLCJjdXJzb3IiOnsiVE9QX09GX1NFQVJDSCI6InNyYzpNWU5UUkFfUExBfGlkeDoxfGZlYTp0b3N+ZmVhOmt3dHxpZHg6MHxzcmM6RkNDfmZlYTpua3d0fGlkeDowfHNyYzpGQ0MiLCJTRUFSQ0giOiJzcmM6TVlOVFJBX1BMQXxpZHg6MTJ8ZmVhOnJvc35mZWE6a3d0fGlkeDowfHNyYzpGQ0N+ZmVhOm5rd3R8aWR4OjB8c3JjOkZDQyJ9LCJwbGFzQ29uc3VtZWQiOltdLCJhZHNDb25zdW1lZCI6W10sIm9yZ2FuaWNDb25zdW1lZCI6W10sImV4cGxvcmVDb25zdW1lZCI6W10sImxleGljYWxPZmZzZXQiOjAsInZlY3Rvck9mZnNldCI6MH0\\u003d","refresh":false,"inorganicWidgetsOffset":{"bannerAdsOffset":0,"missionsOffset":0,"inlineFiltersGroupOffset":2,"relatedSearchesOffset":0,"productRacksOffset":0,"recSearchOffset":0,"trOffset":{"trendsRackOffset":1,"atsaOffset":0,"socialOffset":11}},"scOffset":0,"reqId":"8cd0647f-10e6-4fe0-bec3-30daf196af2d"}',
        'priority': 'u=1, i',
        'referer': f'https://www.myntra.com/',
        'sec-ch-ua': '"Google Chrome";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
        'x-location-context': 'pincode=110001;source=USER',
        'x-meta-app': 'channel=web',
        'x-myntra-app': 'deviceID=9f47d35d-001c-4211-8221-c758f47bb004;customerID=;reqChannel=web;appFamily=MyntraRetailWeb;',
        'x-myntraweb': 'Yes',
        'x-requested-with': 'browser',
    }

    def __init__(self, start=0, end=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_index = int(start)
        self.end_index = int(end) if end else None

        self.cookies = load_cookies()
        self.pipeline = MyntraPipeline()

        # pagination state (from reference logic)
        self.page = 1
        self.offset = 0
        self.pageadd = 0
        self.rowshow = 2
        self.row = 50
        self.count=0
    def start_requests(self):
        all_items = list(self.pipeline.fetch_from_db())
        total = len(all_items)

        start = min(self.start_index, total)
        end = min(self.end_index, total) if self.end_index else total

        chunk = all_items[start:end]

        self.logger.info(f"DB items: {total} | processing {start} → {end}")

        for category, subcategory, link in chunk:

            demolink = link.rstrip('/').split('?')[0].split('/')[-1]

            yield self.make_request(
                demolink=demolink,
                category=category,
                subcategory=subcategory,
                link=link
            )

    def make_request(self, demolink, category, subcategory, link):

        params = {
            'rawQuery': demolink,   # 👈 keyword = demolink
            'rows': str(self.row),
            'o': str(self.offset),
            'plaEnabled': 'true',
            'xdEnabled': 'false',
            'isFacet': 'true',
            'p': str(self.page),
            'pincode': '400006',
        }

        headers = self.headers.copy()

        # pagination-context logic (your reference)
        if self.page == 1:
            headers['pagination-context'] = '{"refresh":true,"v":1}'
        else:
            raw = headers.get('pagination-context', '{}')
            try:
                pagination_context = json.loads(raw.encode().decode('unicode_escape'))
            except:
                pagination_context = {}

            pagination_context['productsRowsShown'] = self.pageadd
            pagination_context['inorganicRowsShown'] = self.rowshow
            pagination_context['inorganicWidgetsOffset'] = {
                "inlineFiltersGroupOffset": self.rowshow
            }

            headers['pagination-context'] = json.dumps(pagination_context)

        url = f"https://www.myntra.com/gateway/v4/search/{demolink}?{urlencode(params)}"

        return scrapy.Request(
            url=url,
            headers=headers,
            cookies=self.cookies,
            callback=self.parse,
            meta={
                "demolink": demolink,
                "category": category,
                "subcategory": subcategory,
                "link": link,
            }
        )

    def parse(self, response):
        data = response.json()

        category = response.meta["category"]
        subcategory = response.meta["subcategory"]
        link = response.meta["link"]
        demolink = response.meta["demolink"]

        cat_hi = {"l1": category, "l2": subcategory}

        products = (data.get("products") or []) + (data.get("plaProducts") or [])



        for p in products:
            yield {
                "product_name": p.get("productName"),
                "product_id": p.get("productId"),
                "category_hierarchy": json.dumps(cat_hi),
                "product_link": urljoin("https://www.myntra.com/", p.get("landingPageUrl", "")),
                "status": "pending"
            }
            self.count+=1

        # ---------------- SAVE ----------------
        folder_name = f"{demolink}"

        # Create full folder path
        folder_path = os.path.join(BACKUP, folder_name)

        # Ensure folder exists
        os.makedirs(folder_path, exist_ok=True)

        # Create file path
        file_path = os.path.join(folder_path, f"{demolink}_{self.page}.json.gz")

        # Write file
        with gzip.open(file_path, "wt", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        # extract products



        self.logger.info(f"{demolink} page {self.page} saved | {self.count} products")

        # ---------------- PIPELINE UPDATE ----------------
        if not data.get("hasNextPage"):
            self.pipeline.update_status(link)
            return

        # ---------------- UPDATE STATE (reference logic) ----------------
        self.page += 1

        if self.page >= 2:
            self.rowshow = 4
            self.pageadd += 25
        else:
            self.rowshow = 2
            self.pageadd += 25

        if self.page == 2:
            self.offset += 49
        else:
            self.offset += self.row

        yield self.make_request(
            demolink=demolink,
            category=category,
            subcategory=subcategory,
            link=link
        )
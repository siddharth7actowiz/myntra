 
import scrapy
from ..pipelines import MyntraPipeline
from urllib.parse import urlencode,urljoin
import json
import gzip
from ..cookies_extract import get_cookies
#to store saved response in a folder
BACKUP=r"D:\Scrapy\myntra\myntra\backup_pages\product_links2"

def load_cookies():
    with open("cookies.json", "r") as f:
        return json.load(f)

#Spider Class 

class Product_link(scrapy.Spider):
    name = "prodlinks"
    

    headers = {
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'app': 'web',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjMwNjIwNzEiLCJhcCI6IjcxODQwNzY0MyIsImlkIjoiNmEwZDQyYzExYTkxNTEyMiIsInRyIjoiNDdjMWVjZDc5NDhlMzhlNzA4ZWVmZDU1MTQ4MDQ4YjkiLCJ0aSI6MTc3Njg0MDYzNzg5NSwidGsiOiI2Mjk1Mjg2In19',
    'pagination-context': '{"productRack":{"dsCnsdrd":0,"tp":"nonDS","cntCnsdrd":0,"slrCnsdrd":0},"scImgVideoOffset":"0_0","v":1.0,"productsRowsShown":25,"paginationCacheKey":"7df3389a-1efd-470d-89f3-3eb83f44b8cd","inorganicRowsShown":6,"plaContext":"eyJvcmdhbmljQ3Vyc29yTWFyayI6IkFva0lRRUFBQUVFRlAvQUFBQUFBQUFCVmdKUTlWUHNCWDUwRWNNRGFyTCtQQTF6WGgzRXdNRjl6ZEhsc1pWOHlPVFl6T0RBeE1nXHUwMDNkXHUwMDNkIiwicGxhT2Zmc2V0IjowLCJvcmdhbmljT2Zmc2V0IjoyNCwiZXhwbG9yZU9mZnNldCI6OCwiZmNjUGxhT2Zmc2V0IjoyMSwic2VhcmNoUGlhbm9QbGFPZmZzZXQiOjE4LCJpbmZpbml0ZVNjcm9sbFBpYW5vUGxhT2Zmc2V0IjowLCJ0b3NQaWFub1BsYU9mZnNldCI6Mywib3JnYW5pY0NvbnN1bWVkQ291bnQiOjI0LCJhZHNDb25zdW1lZENvdW50IjoxOCwiZXhwbG9yZUNvbnN1bWVkQ291bnQiOjgsImN1cnNvciI6eyJUT1BfT0ZfU0VBUkNIIjoic3JjOk1ZTlRSQV9QTEF8aWR4OjN8ZmVhOnRvc35mZWE6a3d0fGlkeDowfHNyYzpGQ0N+ZmVhOm5rd3R8aWR4OjB8c3JjOkZDQyIsIlNFQVJDSCI6InNyYzpNWU5UUkFfUExBfGlkeDoxOHxmZWE6cm9zfmZlYTprd3R8aWR4OjB8c3JjOkZDQ35mZWE6bmt3dHxpZHg6MHxzcmM6RkNDIn0sInBsYXNDb25zdW1lZCI6W10sImFkc0NvbnN1bWVkIjpbXSwib3JnYW5pY0NvbnN1bWVkIjpbXSwiZXhwbG9yZUNvbnN1bWVkIjpbXX0\\u003d","refresh":false,"inorganicWidgetsOffset":{"bannerAdsOffset":3,"missionsOffset":0,"inlineFiltersGroupOffset":2,"relatedSearchesOffset":0,"productRacksOffset":0,"recSearchOffset":0,"trOffset":{"trendsRackOffset":1,"atsaOffset":1,"socialOffset":10}},"scOffset":0,"reqId":"7df3389a-1efd-470d-89f3-3eb83f44b8cd"}',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.myntra.com/men-tshirts',
    'sec-ch-ua': '"Google Chrome";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'traceparent': '00-47c1ecd7948e38e708eefd55148048b9-6a0d42c11a915122-01',
    'tracestate': '6295286@nr=0-1-3062071-718407643-6a0d42c11a915122----1776840637895',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
    'x-location-context': 'pincode=380008;source=IP',
    'x-meta-app': 'channel=web',
    'x-myntra-app': 'deviceID=0131b128-0606-49b0-a2eb-ebce6823fe30;customerID=;reqChannel=web;appFamily=MyntraRetailWeb;',
    'x-myntraweb': 'Yes',
    'x-requested-with': 'browser',
    # 'cookie': 'at=ZXlKaGJHY2lPaUpJVXpJMU5pSXNJbXRwWkNJNklqRWlMQ0owZVhBaU9pSktWMVFpZlEuZXlKdWFXUjRJam9pWW1aa1lUYzVOVGN0TTJRMU9DMHhNV1l4TFRobU1tWXRZakptTVdRM1pHSTVOR1k0SWl3aVkybGtlQ0k2SW0xNWJuUnlZUzB3TW1RM1pHVmpOUzA0WVRBd0xUUmpOelF0T1dObU55MDVaRFl5WkdKbFlUVmxOakVpTENKaGNIQk9ZVzFsSWpvaWJYbHVkSEpoSWl3aWMzUnZjbVZKWkNJNklqSXlPVGNpTENKbGVIQWlPakUzT1RJek1UQTJPREVzSW1semN5STZJa2xFUlVFaWZRLnRJYXQzZnd0U3RNY19pZkZsX1k1SnlzYVRIMEk2WnBZR0haV3VPcjgtUnM=; _d_id=0131b128-0606-49b0-a2eb-ebce6823fe30; mynt-eupv=1; mynt-ulc-api=pincode%3A380008; x-mynt-pca=X6OBk4bFIeybx0-nSr6DH4ooQphl7u878h_mNd0MwASqOyoR9iUkJbjYlCFyDW1fhA5o0Ud3_5TVFOLbuBQXF8TrJdgQJUGp_dAEJrahUpIknKsIFAvbwsBR-Ui9WZwVgPNvl3W1AT30xhY2gvAl0bkumlC5ucoXJ0FM_UzMU2OZPDS3c3nOfg%3D%3D; _gcl_au=1.1.1416392668.1776758682; _cs_ex=1; _cs_c=1; _fbp=fb.1.1776758682757.354532818192485209; tvc_VID=1; _scid=9LVd1yPd6f1KSk8K_0gppcjKGVzfLCFX; _sctr=1%7C1776709800000; G_ENABLED_IDPS=google; __insp_wid=617845923; __insp_slim=1776764660518; __insp_nv=true; __insp_targlpu=aHR0cHM6Ly93d3cubXludHJhLmNvbS9sb2dpbj9yZWZlcmVyPWh0dHBzOi8vd3d3Lm15bnRyYS5jb20vbWVuLXRzaGlydHM%3D; __insp_targlpt=TXludHJh; __insp_norec_sess=true; _ma_session=%7B%22id%22%3A%22e4e5022b-d89a-4d88-83fd-bf4037c8cdd4-0131b128-0606-49b0-a2eb-ebce6823fe30%22%2C%22referrer_url%22%3A%22%22%2C%22utm_medium%22%3A%22%22%2C%22utm_source%22%3A%22%22%2C%22utm_channel%22%3A%22direct%22%7D; _mxab_=config.bucket%3Dregular%3Bcoupon.cart.channelAware%3DchannelAware_Enabled; _pv=default; dp=d; lt_timeout=1; lt_session=1; bm_mi=DEC626BAB3EA8F69E2887BECB9141212~YAAQx18yuJKJgKudAQAAgfHzsx/nv0BqhMbpDlpc3Y/AJ3yiwnvNTzJY6kZ4wmoyS4Fux5A/Jef7vZwnJP6IhE3TooNw9Lk5tu2ZXidk8bq/QzTYPfHmDzskeWT2k3s5pO2r8ZQVrF4yHTfM5Fdy5DE06zLi5+ACwC54TU2jaA5U/m1DqATVBCWJ0R0ylZfhgWO7KaLyaETSwuBvVJthhzMSz9Sn28n1K2yvaVwiDHzeTLrGiyg3n40MtJNr8wdLNWnm4gflnhgNIBvZqgVyklW0hfba84khAdcuCMdhqxE/Tuc6XWt002adkr63xihLHGGo5Zp7MZ9x2w79d0c0dCy5LPuMB10yM35y9FujBRz1~1; microsessid=418; _xsrf=UD5PlddWhPKj4YdDQMWyMgPRXk03Q70k; mynt-loc-src=expiry%3A1776842043781%7Csource%3AIP; ak_bmsc=D89D327544CE715FB86C6C27E52E5980~000000000000000000000000000000~YAAQx18yuOqRgKudAQAAo0T0sx8dYpd6XB7x7EzUdtkw6FRmjYm13/NZDFv19QMnMixXCHNiEHIiUh/yHy3xPBmuksvme9Ee3a0vt+mcXiNItuERq6Ee9MiZzYhhf8A86Kso/gtqPIRqssWGd6KDMfumRg0bdqvqb7NohKzdn7TX/7eTfPgVuYK4hsKfMUj8ZgyG77SwFjQj4EsXCybQ+UKcbWXXUJghMvw97biWyU+tmX1KR0c3IvFI6jcRmLtGodjZ61FFLNJsFkm1g3OuPLtYghPE2EMq4xJ5Z23b8/dTqJc7CEUOH31hDluOBpPXOBfoQY4d4500TS3zwHolb+byb8ycYi/bhY1/kh59ug3kLeyyB/m5pkmRcF+MZbvFwnY7fVVQVOeh8ty2R1w3Zy4wectiUFf49bH1BdnbSFni/PQ0eiY5+/6vDLLTuOuH4sz10mWzyN52JZO5mRR8E3X/Pr9gL+JX2i8aAqmLpxVib/xH/o5IcUugO0XsDD3P9s+e/qskMKk=; bm_sz=C2B14A58DBE1845F94F51C5D2D8372B6~YAAQx18yuOyRgKudAQAAo0T0sx+wixskwI1oV2S+9OMtg+3FDo0MowL1/LuQ694ZLJ3KFgFV9l7KGh328hwpwqNT2Lserh+mj+3vlX+UtdqJNG+5KgUyVT7XbPf8f7vq/HBARS7/vUUlTgjNmAt3evAFxJ6Usc+AMLKb/3B8FBe9ElwDN8MmCCMWbZAAgQ/9zkdIY/xhG8fTF2Rm+7ReR9B6jKKx+kyRBnDLApzGxuOK9/QCSrh02dsbiG7PzqsyS7RVu5Iz1V7Si1SEilpX5hnXrFS/iM9iU0/RDs769/GJnjpXHO1yhMvbaAHm0oPGsZGMg7l+OCoyE8xZ2rR2y2c035z7inUVfNVw23hJ8H1wSZdACkE8ifupAnfPPGXoSgyrMNd8oF6Pdnp21enKv6YTW72Bke1VNymnPrimP3sVzlh+URXaUFhyYjJD0G1pAguJmVSq7aZZO9XQxB4/JylOCzSiBTOi4HX/rqjBhpTt0iHLpV2njMlzcVEMfG5KPMVfdyjMHi5yZI8Hww4VjFFFaVQZwpWqwhGAFPlZ0SWviJk=~4277815~3291193; ak_RT="z=1&dm=myntra.com&si=686120a8-81b4-4caa-98f7-91dcb6d74821&ss=mo9juzzz&sl=a&tt=5lh&obo=7&rl=1"; _abck=55E024A098E2E9A035A7612A7A1EBD0A~0~YAAQx18yuEGSgKudAQAAyEf0sw91yxPVvb2daZ2Tc/7ZQNUGZFp0Mj68Cp7OQlPwhCksISlQX2CmRaEk+rDph2GN5mSM2pSglw2QcxyomtywH0QU2uq/yhzXJcEsWc7A+kyuRs+ppd9sQZiBF5h4YsHWbfSzqo5UVUqEvpymSTx50qhXCq+NOgcAq2cVD9fOI7eKkIEmfWqwHxFtm6opIu0FyXb354jJrV12J//rhEAoUUonJVl/RAJlTOE1c91orSYkdYARKN1RF+dkw91pUo77kxCGTCFfdN4AzahdeY+71IXnmKD5CkW+gu/m4bhs64QjGigpTTo68ld5zvLBgFMilEquNyMlFWHBqMtgHNDkKJTmdSe+2fc3Hf0H3IWz5/aVOsWBPeaockKMwk3r6CD2YFfVTvgA11kZa0M/VFROyYIVsoKpsMW9yxmpq0zgJROWTBlI2SHg+QnPcSIcawyUQFnvdH45yMVQkFmAfdqdSOdfrjfgrGfvKGMbyyMALWhSKesLKSQD7Z/2swfbYbE7Qr3kzeN+jMTHTjmQjCQ5/PuUOHNzOz44vs0K+JBlzSmjPbgTUWbnPuDi5rLrqvfcAdCErdPl6b4oWP0a41s0U2V9yi+uIJ1NshO249Valis2UXhpZk142Xf97VlPQBo8x7XLsrAABTakOpKKpYTh/OWX48aiIRMZa79Nlz+IDDds6znP0BtsIFpTXmlOKkyS/yU9OQFp/1zgIlL+R6koidW1spCWGfRmoZlesKgZmS4BcuntwTe1whyWHwzuDh6h9I7kaKnY6dWkyzaKbZ+pJDyhhktBtpjDsNeroJcXhzbkiCgL0NNqalcTYxRRkns43nmHHxs3YB3kk20E52J9QxnrDOMKxGkjME4Xm/lF36G9I1fR/bWuLwaUVlTzeklqduw7oHTSXuV8IXVzcsp46KqBQ3phs2OYLeZOVlUKQ6UY4v/LyPc9L7UqLKdfrJJ1mZeQF6IDid7dIa+tHsXzpTUTk51snz8koF4QL3fYyvm4/WZoztetYhxVtIOuF1bd/d05vWXq1XgeK2KYRh3mkkFmKyunrs/JJZKcRL9OhJYBZ/5sOznqz17kQqYL+e+0W9MgRWyT7FuhI4/lmWjuri5AVtK4eZiRVtsDnfas~-1~-1~-1~AAQAAAAF%2f%2f%2f%2f%2f3XFnGSL%2fJMhJ9a7ONcpQawbAy79CJhA2QPrLIez3zWjH9TCjUh5GBfZZhxg1ht6xf6IDZ4Afv5YWdTlSWbGOuDJCCOqe0RWmuI7U1RrpYWlJIox5QURuU3EBAhPKkGFllyUTqgZJpeYdQlSw5%2fFWvl6F1r8p7L1isBp7LEuPaHYcnhTmE4cMIPlvm+nGmeVwGyPGE3csdSM~-1; utm_track_v1=%7B%22utm_source%22%3A%22direct%22%2C%22utm_medium%22%3A%22direct%22%2C%22trackstart%22%3A1776840624%2C%22trackend%22%3A1776840684%7D; utrid=SA9jdk0WWXBxTFQAaGZAMCMzNjQxNzI4NzM0JDI%3D.a43a8b8bf9c3648ffe28cb80457834dc; user_session=K3GypmTLn7azKiTVTCVGvg.SffQDEHcHZf7i0GcqjnMdvC9Es631_OGfdBy9UX7lCoJCPp0yG9NExMKap9r0S-79AQgA8nKRw24IG2dzn84azarfcOaUwoid2gVs3ZR1bq1ISvveuiZ3kZ-Zjfv3N-atyhjkix96aMF0o4tmkWsPQ.1776840603058.86400000.4CIBzayYP3H_17wyaG38AUskBIhRxhYCyIiWJ4jPcYU; bm_sv=D710EFB0FA84F8E7CFEDF543A02FE775~YAAQx18yuJWTgKudAQAA/FH0sx/0H/P7JaM+EkaTlB+72Q76raDGrrmIoKRHnivmie8Z+qYgMH+XpJItQWYD9JUqxsFtL8vTNuOiogxmoMvURljxRAHFVMRN7qpbCVETi65gFqJdnjqRQ9+bOWFBmDBtwRA7XpRvTN8Fjle8L3fP/eLiy4fb86bfjB1+TwRoZxbFIg0e8cgr6iYZzYvPGf7MEx8vdMDOV2gWpTlAyqvwUGctktSwAUO7SGUuGWsdNw==~1; _scid_r=BDVd1yPd6f1KSk8K_0gppcjKGVzfLCFXujA2GA',
}    
    
    # multiprocessing - taking start and end args to run multiple processes 
    def __init__(self, start=None, end=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_index = int(start) if start is not None else 0
        self.end_index = int(end) if end is not None else None

    # creating pipeline instance (keeping as you used)
    pipeline = MyntraPipeline()

    def start_requests(self):
        all_items = list(self.pipeline.fetch_from_db())
        total = len(all_items)
        print(f"Total items in DB: {total}")

        end = min(self.end_index, total) if self.end_index is not None else total
        start = min(self.start_index, total)

        print(f"Processing chunk: {start} to {end}")
        chunk = all_items[start:end]

        if not chunk:
            print("No items in this range..!")
            return

        for category, subcategory, link in chunk:
            print(f"Processing: {category} > {subcategory} > {link}")

            demolink = link.rstrip('/').split('?')[0].split('/')[-1]

            page_number = 1
            params = {
                'rows': '50',
                'o': '249',
                'plaEnabled': 'true',
                'xdEnabled': 'false',
                'isFacet': 'true',
                'p': str(page_number),
                'pincode': '380008',
            }

            api = f"https://www.myntra.com/gateway/v4/search/{demolink}?{urlencode(params)}"

            yield scrapy.Request(
                url=api,
                callback=self.parse,
                headers=self.headers,
                cookies=load_cookies(),
                meta={
                    "category": category,
                    "subcategory": subcategory,
                    "link": link,
                    "demolink": demolink,
                    "page_number": page_number,
                }
            )

    def parse(self, response):
        print(f"Parsing: {response.status} - {response.url}")

        category = response.meta["category"]
        subcategory = response.meta["subcategory"]
        link = response.meta["link"]
        page_number = response.meta["page_number"]
        demolink = response.meta["demolink"]

        cat_hi = {
            "l1": category,
            "l2": subcategory
        }

        data = response.json()

        # safe filenames
        safe_cat = category.replace("/", "_").replace(" ", "_")
        safe_sub = subcategory.replace("/", "_").replace(" ", "_")

        # save each page separately
        with gzip.open(f"{BACKUP}/{safe_cat}_{safe_sub}_{page_number}.json.gz", "wt", encoding="utf-8") as f:
          json.dump(data, f, indent=4)

        # extract products
        for product in data.get("products") or []:
            print(f"Found product: {product.get('productName')} (ID: {product.get('productId')}) {product.get('landingPageUrl')}")

            yield {
                "product_name": product.get("productName"),
                "product_id": product.get("productId"),
                "category_hierarchy": json.dumps(cat_hi),
                "product_link": urljoin("https://www.myntra.com/", product.get("landingPageUrl", "")),
                "status": "pending"
            }

        # pagination
        if data.get("hasNextPage") and data.get("products"):
            page_number += 1

            params = {
                'rows': '50',
                'o': '249',
                'plaEnabled': 'true',
                'xdEnabled': 'false',
                'isFacet': 'true',
                'p': str(page_number),
                'pincode': '380008',
            }

            api = f"https://www.myntra.com/gateway/v4/search/{demolink}?{urlencode(params)}"

            yield scrapy.Request(
                url=api,
                callback=self.parse,
                headers=self.headers,
                cookies=load_cookies(),
                meta={
                    "category": category,
                    "subcategory": subcategory,
                    "link": link,
                    "demolink": demolink,
                    "page_number": page_number,
                }
            )
        else:
            #update status only after full pagination
            self.pipeline.update_status(link)
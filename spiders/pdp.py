# from typing import Iterable
#
# import scrapy
# import re
#
# import json
# from parsel import Selector
# from scrapy import Request
# from pipelines import MyntraPipeline
#
# def load_cookies():
#     with open("cookies.json", "r") as f:
#         return json.load(f)
#
# class pdp(scrapy.Spider):
#     name="pdp"
#     def __init__(self, start=None, end=None, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.start_index = int(start) if start is not None else 0
#         self.end_index = int(end) if end is not None else None
#
#     # creating pipeline instance (keeping as you used)
#     pipeline = MyntraPipeline()
#
#
#     def start_requests(self) -> Iterable[Request]:
#         # cate_hierchry,product_name_,p_id,url
#         headers = {
#             'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#             'accept-language': 'en-US,en;q=0.9',
#             'cache-control': 'no-cache',
#             'pragma': 'no-cache',
#             'priority': 'u=0, i',
#             'referer': 'https://www.myntra.com/men-tshirts',
#             'sec-ch-ua': '"Google Chrome";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
#             'sec-ch-ua-mobile': '?0',
#             'sec-ch-ua-platform': '"Windows"',
#             'sec-fetch-dest': 'document',
#             'sec-fetch-mode': 'navigate',
#             'sec-fetch-site': 'same-origin',
#             'sec-fetch-user': '?1',
#             'upgrade-insecure-requests': '1',
#             'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
#             # 'cookie': 'at=ZXlKaGJHY2lPaUpJVXpJMU5pSXNJbXRwWkNJNklqRWlMQ0owZVhBaU9pSktWMVFpZlEuZXlKdWFXUjRJam9pWW1aa1lUYzVOVGN0TTJRMU9DMHhNV1l4TFRobU1tWXRZakptTVdRM1pHSTVOR1k0SWl3aVkybGtlQ0k2SW0xNWJuUnlZUzB3TW1RM1pHVmpOUzA0WVRBd0xUUmpOelF0T1dObU55MDVaRFl5WkdKbFlUVmxOakVpTENKaGNIQk9ZVzFsSWpvaWJYbHVkSEpoSWl3aWMzUnZjbVZKWkNJNklqSXlPVGNpTENKbGVIQWlPakUzT1RJek1UQTJPREVzSW1semN5STZJa2xFUlVFaWZRLnRJYXQzZnd0U3RNY19pZkZsX1k1SnlzYVRIMEk2WnBZR0haV3VPcjgtUnM=; _d_id=0131b128-0606-49b0-a2eb-ebce6823fe30; mynt-eupv=1; _gcl_au=1.1.1416392668.1776758682; _cs_ex=1; _cs_c=1; _fbp=fb.1.1776758682757.354532818192485209; tvc_VID=1; _scid=9LVd1yPd6f1KSk8K_0gppcjKGVzfLCFX; _sctr=1%7C1776709800000; G_ENABLED_IDPS=google; __insp_wid=617845923; __insp_slim=1776764660518; __insp_nv=true; __insp_targlpu=aHR0cHM6Ly93d3cubXludHJhLmNvbS9sb2dpbj9yZWZlcmVyPWh0dHBzOi8vd3d3Lm15bnRyYS5jb20vbWVuLXRzaGlydHM%3D; __insp_targlpt=TXludHJh; __insp_norec_sess=true; mynt-ulc-api=pincode%3A413101; x-mynt-pca=4PVIyZoypjBcTHJqDea5tnE-sNw94GhozBAdK3ERjWykK7tmNqb_dZyi3kK2nreHQ92AvfZgLfdI9tBfZWGX42NQjg9NW7aU-mINCrPTbE-rNC2v9cGsxpp9npR2WhMvm2UY6ge_l_-awHS1QWFsHteWnCaWb_IVwBvWLtSiUbju_PbVvLE3Dw%3D%3D; mynt-loc-src=expiry%3A1776934445527%7Csource%3AUSER; _abck=55E024A098E2E9A035A7612A7A1EBD0A~0~YAAQFxzFF3afF3qdAQAA8uoyug9Kyty+M7vdl5cxsbU8lxkoHBG9cGh5jJjZ0WBDgO483X2zxLAE3c5RQNIeJvsV78GzBE4VA7V8685e4OD5svfWElBv4xdGiN4OI+TJq2l+eMSOyBHJWxKnaro5r0EidrclxoBXNrsHlu/0P2UhFuF+doYsGshmu1l8DrV97c3BJ6KwAKOS9Spb4iR5HTPFpjiwlaBTAxES4CvjrxI+O5uc0trTycC4hnGiRzUMhF+x0kbERgmSaK6fJj5PYSYywvqxsFtnFwHC0ioSebLG0Azd4dvCA9aUzgcREuhrs6uVmxIxL5AzezcJKk2NLPPupNsXUUocy1N8Zcs9npY7e1tzDmlZG2vBVXoroe5JyubR67im552g50c9OWD/qnnT6fEMT9Rwyzy7BWXbdhjycomEipPrNd34F16bgUcpvlV/gaxgdCoZRV/3RqdgEVPI9JqnxNHRdAkSVzmml5RxKk796eUrGrrj4X58QX6//GUrdnMouNHy1PidCFReG4xHZtfuXQO+w9Iuuce3hY0eBzzklicnZXI48ukfvlh4eLZT8HDowaa1u5UVzEV/GsE3Ja/RKECY6vNHR69+zzhIEM5va61Q2jrDHUkU5kOrNnIFvuU3Bt2l+JsFAQUOSZ/iR1B/Y6AD1w6s1dxG1pamg/CpVQBVFA48x+3Asd+YAs+eABs93s38LBvuQL8qD9OXFNlU6H5Op9wxeHUsiIjbeYvT2m4TiKBFqnHYWxYf/H72khAh1y4LCqeXIGmKsXJ+dKuGIrYD6+2x19hB4Au9MbH0vlWhbb9or3ScTfbdwopxM/IfOyuX29hX9WH/eioGmr1+6ntWCQprCt++tC37bFOtou9ZfacgbFc24GioSi3P7+n5/f4VM8Dtly0Ne7vNQlWjBVcRTvT/f0dcRPHzWZ6ce1+V4g==~-1~-1~-1~AAQAAAAF%2f%2f%2f%2f%2fx24g5GcAfMnLZVxbLoxRJU4XtCWdCZGexAo6kKe7Oe2bnS3DJdFi4M4Epy4lPBH0xPIlFa9I0qB1vlHpeCo%2fT0ywmYTttNzm5LBbCLQYvGwYEDP5RmXnRQtUU4UrH%2fpPuuIuL2vj2sbUr5HvgRWxZQTIi2ydv95s%2fTOf+ONP+krEB3r6DwaoLBG5K1H0DWMb8aONWhNGRyf%2f%2fcmG3Kpsv8froQHV1H0n8vXR9KgrIvqEpY%3d~-1; _mxab_=config.bucket%3Dregular%3Bcoupon.cart.channelAware%3DchannelAware_Enabled; _pv=default; dp=d; utm_track_v1=%7B%22utm_source%22%3A%22direct%22%2C%22utm_medium%22%3A%22direct%22%2C%22trackstart%22%3A1776948460%2C%22trackend%22%3A1776948520%7D; lt_timeout=1; lt_session=1; bm_sz=58F7173824344E9036117A56DAFB5B00~YAAQExzFF4za2bGdAQAAKLthuh+J01MCOPbVOijoejDBSQJ6EhyF8Vx6g3lJHREeupg0Z4CPrZc0K/sI8p0EfTwobJ32kF8mzyAudEEKn7IwWcs+1N5+ZJ0XICzlRSG3RFJ/ozCUwmJ1qL5OTMP4al6nH06COIizUyCkqd22ZiB2fqY/h5UU5K8BYhGxjd5orB2ibmwXfhkA+gIURXbufF924aocYi0VV92gKLOfNJcRa5CFaCSH3SYWutsO/9jOwUgWnISLReh4aCHk0znchi9H715FULzelAuhSP3bovqtuBGCop9cTHFEmyaCwCy6zMirN9837CwkN/T9VcZPWTMW8+s9b2PpcNcsiPohp5YkgjYmWd2nTLLaazn/n0MNdXsZSsv3QYDip/gy4YbhORiXthKTBW6TR+vxyWNX~4273202~4538690; _ma_session=%7B%22id%22%3A%227d91dd89-0261-4c29-9c55-3e86f8f15a52-0131b128-0606-49b0-a2eb-ebce6823fe30%22%2C%22referrer_url%22%3A%22%22%2C%22utm_medium%22%3A%22%22%2C%22utm_source%22%3A%22%22%2C%22utm_channel%22%3A%22direct%22%7D; microsessid=942; _xsrf=LV6jKvTNuoKGzwXiOkBuhRIw41mPWyHI; user_session=tunEuyBrBPozehyBymzpRw.td-dG5DX5J78Unt94RrofT6JA68-P5lrIkWq-2OJXo_BrJl4dDBjbqYnIaHhfKhszw52RiaBNrwKDsXbcwjwCWx9ThX-ENd9mKxGYcBNvPfUElvzmNinFYJ8Y4xnWsnzpirdDsYy2z7c8XWzljrtzQ.1776948461818.86400000.rh9-uO75KG5-C6nR_hBqVZLrL4a5_hGYz7mtM5vLAIU; ak_bmsc=5037D6FA769C7BBF8468FE5BC5A2F82A~000000000000000000000000000000~YAAQExzFFzHi2bGdAQAAwMJhuh+v2Yl1hsouoJHb0KBRkFmhNXj8vOzYCj9MqH8sQ30KX0RX4BkX4//Rq3ruuQrHJFkmPCF++0WDM0bTqxXt5JpFl7OUknTgWfZaH6/V/69cHhTF2UmjCIN3gH3hDtIv3OZiSd/gPSWkYhW52/SvERIPkuO4bjxsOta408ZK4MBno8EqZUJgZmQAJSy/1K3AkU6Sqmv0fRz1NO5LhwR5xNPM5xuBjPQRL83fJfY0CDl+xx5R49j8HZbVEfjIZUZq97qnkwoditUKEEhxH4Pp8AXAsE/Thj9+ayAFjsEwFiRRVyIwOUJYxsk4VArpmTRBEd13iNzRZ4hUftfEPL+TUPHwDsrdY/E695xewMFKAE0HYfb9VGepsTcfpTGYUL8B0CmCBerLAJBXvBvByAOxai66zKv/1GNwHaUZmMO1ih1izi1WhxY1Dz8lNeA=; _scid_r=DDVd1yPd6f1KSk8K_0gppcjKGVzfLCFXujA2TQ; utrid=SmZVUxEGZkABBXJOUElAMCMzNTQ4NDkwNTg5JDI%3D.71d0ded7a0dece977f4ba5a856731aaf; bm_sv=034DF36575C9DC907D4FD03C94D8B24E~YAAQExzFFzsz2rGdAQAAuBliuh8UjB5QmeufBIpMKesC2ZWPquvXlLWO611Tx+mjhXdJLp2pjYqFL54czlpxPUUPGdIBPYLjH0t6Cp+kOTWIdVP2Ho8tSgHv4LsuFouJ5w1bWfsbd0KM4rIeAey0QGFd91eMWLCrrmbY6qMMIfw9viqafWr8Jk0YbCx0MXdPVXVFYJhbP00E3n7fRr5A2oo7CNbui010V2YNaLmQUgxoBN01wSfvPk8l6+rES+g4~1; ak_RT="z=1&dm=myntra.com&si=686120a8-81b4-4caa-98f7-91dcb6d74821&ss=mobh89is&sl=0&tt=0&ld=68c77&ul=1e0l"',
#         }
#         yield scrapy.Request(url=url,cookies=load_cookies(),headers=self.headers,callback=self.parse(),meta={})
#         pass
#
#     def parse(self, response):
#         # data = response.text
#         #
#         #
#         # with open("pdp2.html", "w", encoding="utf-8") as f:
#         #     f.write(data)
#         # json_dict = data.xpath('string(//script[contains(text(), "pdpData")])').replace("window.__myx = ", "").get().strip()
#         #
#         # j_data = json.loads(json_dict)
#         #
#         # # saving response json for backup
#         # with gzip.open("_sample_tshirt.json.gz", "wt") as j:
#         #     json.dump(j_data, j, indent=4)
#         #
#         # product_data = []
#         # base_path = j_data.get("pdpData", {})
#         # temp = {}
#         #
#         # # basic info
#         # temp["product_name"] = base_path.get("name")
#         # temp["product_code"] = base_path.get("id")
#         #
#         # brand = base_path.get("brand", {}).get("name") or ""
#         # temp["brand"] = brand.strip()
#         #
#         # # description
#         # product_details = base_path.get("productDetails", [])
#         # raw_desc = product_details[0].get("description", "") if product_details else ""
#         #
#         # desc = Selector(text=raw_desc).xpath("string()").get() or ""
#         # temp["description"] = desc.strip()
#         #
#         # # images
#         # albums = base_path.get("media", {}).get("albums", [])
#         # images = albums[0].get("images", []) if albums else []
#         #
#         # temp["images"] = [img.get("imageURL", "") for img in images]
#         #
#         # # colours
#         # colours = base_path.get("colours", [])
#         # temp["colours"] = [
#         #     {
#         #         "colour": col.get("label"),
#         #         "image_url": col.get("image")
#         #     }
#         #     for col in colours
#         # ]
#         #
#         # # ratings
#         # ratings = base_path.get("ratings", {})
#         # rating_scale = [
#         #     {"rating": rt.get("rating"), "count": rt.get("count")}
#         #     for rt in ratings.get("ratingInfo", [])
#         # ]
#         #
#         # temp["ratings"] = {
#         #     "average_rating": ratings.get("averageRating"),
#         #     "total_ratings": ratings.get("totalCount"),
#         #     "rating_scale": rating_scale
#         # }
#         #
#         # # reviews
#         # reviews = ratings.get("reviewInfo", {})
#         # temp["reviews_count"] = reviews.get("reviewsCount")
#         # temp["customer_photos"] = reviews.get("reviewsImageCount")
#         #
#         # # specifications (generic)
#         # temp["specification"] = base_path.get("articleAttributes", {})
#         #
#         # # offers
#         # offers = base_path.get("offers", [])
#         # temp["offers"] = [
#         #     {
#         #         "type": offer.get("type"),
#         #         "title": offer.get("title"),
#         #         "description": (offer.get("description") or "").replace("\u20b9", "").strip()
#         #     }
#         #     for offer in offers
#         # ]
#         #
#         # size_list = []
#         # sizes = base_path.get("sizes", [])
#         #
#         # for size in sizes:
#         #     seller_data = size.get("sizeSellerData", [])
#         #
#         #     size_info = {
#         #         "size": size.get("label"),
#         #         "available": size.get("available")
#         #     }
#         #
#         #     if seller_data:
#         #         seller = seller_data[0]
#         #         size_info.update({
#         #             "mrp": seller.get("mrp"),
#         #             "discounted_price": seller.get("discountedPrice")
#         #         })
#         #     else:
#         #         size_info.update({
#         #             "mrp": None,
#         #             "discounted_price": None
#         #         })
#         #
#         #     size_list.append(size_info)
#         #
#         # temp["sizes"] = size_list
#         # pprint(temp)
#         #
#         pass
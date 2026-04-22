import scrapy

#backup folder
backup_folder=r"D:\Scrapy\myntra\myntra\backup_pages"

#Spider Class 
class CategoriesSpider(scrapy.Spider):
    name="cate"
    start_urls=["https://www.myntra.com/"]
    def start_requests(self):
        
        cookies = {
            'at': 'ZXlKaGJHY2lPaUpJVXpJMU5pSXNJbXRwWkNJNklqRWlMQ0owZVhBaU9pSktWMVFpZlEuZXlKdWFXUjRJam9pWW1aa1lUYzVOVGN0TTJRMU9DMHhNV1l4TFRobU1tWXRZakptTVdRM1pHSTVOR1k0SWl3aVkybGtlQ0k2SW0xNWJuUnlZUzB3TW1RM1pHVmpOUzA0WVRBd0xUUmpOelF0T1dObU55MDVaRFl5WkdKbFlUVmxOakVpTENKaGNIQk9ZVzFsSWpvaWJYbHVkSEpoSWl3aWMzUnZjbVZKWkNJNklqSXlPVGNpTENKbGVIQWlPakUzT1RJek1UQTJPREVzSW1semN5STZJa2xFUlVFaWZRLnRJYXQzZnd0U3RNY19pZkZsX1k1SnlzYVRIMEk2WnBZR0haV3VPcjgtUnM=',
            'lt_timeout': '1',
            'lt_session': '1',
            '_d_id': '0131b128-0606-49b0-a2eb-ebce6823fe30',
            'mynt-eupv': '1',
            '_mxab_': 'config.bucket%3Dregular%3Bcoupon.cart.channelAware%3DchannelAware_Enabled',
            'microsessid': '909',
            '_ma_session': '%7B%22id%22%3A%2243d10c57-1557-4cb5-9a30-ae80fad9c498-0131b128-0606-49b0-a2eb-ebce6823fe30%22%2C%22referrer_url%22%3A%22%22%2C%22utm_medium%22%3A%22%22%2C%22utm_source%22%3A%22%22%2C%22utm_channel%22%3A%22direct%22%7D',
            'mynt-ulc-api': 'pincode%3A380008',
            'mynt-loc-src': 'expiry%3A1776760122294%7Csource%3AIP',
            'x-mynt-pca': 'X6OBk4bFIeybx0-nSr6DH4ooQphl7u878h_mNd0MwASqOyoR9iUkJbjYlCFyDW1fhA5o0Ud3_5TVFOLbuBQXF8TrJdgQJUGp_dAEJrahUpIknKsIFAvbwsBR-Ui9WZwVgPNvl3W1AT30xhY2gvAl0bkumlC5ucoXJ0FM_UzMU2OZPDS3c3nOfg%3D%3D',
            'ak_bmsc': '70A62C498BDDF5DACBBCAEBEC42231F0~000000000000000000000000000000~YAAQChzFF3ndL4GdAQAARPMRrx9oafOt8b3Vbi5RKaYrYzsHz5hqri6oRXNb5fRNRa7mY348tc1ox4thT/HAMov9jbGSHPxTOuj4s493z3ysZwPL+M/DMJVPrdkBAzqk7fiGZQ9QqSXW9HfO1Tyst4V+nCPITS57nM99W+AtYUJarlr+K/8Oi1T0y0OrwGMyPnOI77x3qXbuO2P+SGhK6Mezb1+q1qmTIRBnvQStY9MKiGZ9jOTWAkCw35hAn8WA9lQhMfTM36wGz3gEUFySCKUMBmPfXtZTFbwXr+ppPhTGitLXE9NFFoG68TFErf1WL48tOSlghgqKcmE86AOHXIof0x68zmXOr7tuHHXlvDqENsCaNCii2saOYpjJb6K8O9H+izEYm+PeNx1e6c1LcRDha7LLRf1pMiQPVLGWLNiHh9sIUytrn22Hv/UjmQdutTU4WdgEjy8edz08rn8=',
            '_gcl_au': '1.1.1416392668.1776758682',
            '_cs_ex': '1',
            '_cs_c': '1',
            '_fbp': 'fb.1.1776758682757.354532818192485209',
            'tvc_VID': '1',
            '_scid': '9LVd1yPd6f1KSk8K_0gppcjKGVzfLCFX',
            '_sctr': '1%7C1776709800000',
            '_pv': 'default',
            'dp': 'd',
            '_xsrf': 'M9uNKD1I2BVpcaPEb7hPZjKf6AEfwLnF',
            'bm_sz': '389841066650DBE804125BC9A812520A~YAAQVqXBF1O91n2dAQAAZUUnrx/PLNY11JThWsBFyoOCHpdSRZusNWszRTeqk0vJg13b2hvBx0/B7qsQY6D2TCDcqmTdL189j7m6ypUUhtX0g0r1T1hGwvSj67j52W3YndA+1hWhDfc8W+qka5qPOdlSGf7X96Lm7UM8PHPmYlMcHHN6meVH/RGheZE4OtjlIX/ylzMi2EXY6yKhRmQtOTTGPaC1fLWZei3eHgPGT1sPe3wTQnSNw3eXXlPJgr/7rwc5uq9tTITwzrOLwHc4z3N7lCq9bwQAvqHvhx6IbPu6RB6OzVJWJkLigNsSKqv2FQyZh/TFdQRD3lLaHBgfzblZoZxFR202W5SkZZpjCAhH7elFn7oAqBhFqTuwtEkRkhkxRvZvBFS7SsLuvbjrbohjCoaGgqIGsBG4xgKQclZW5ZXp1ylhqKSNMpB8GOeqVQ+tACSUHE98GAn+nKcjWA3ACVqoDY3ZJbkP5X8MeWKt~4343351~3486259',
            '_abck': '55E024A098E2E9A035A7612A7A1EBD0A~0~YAAQVqXBF5O+1n2dAQAAzEcnrw+ql4cfDbIk8KOzCir1kFqfiDVv6SUzq7C39554AK8LPf8xSn70u3Utso6GBosem92X6xEJMiFx3sHqrvbqtMj7AJ3hux4L0pKjDmJ4pKb10UPMHEdyF2QKsNbmfwEqHvX2DmtOK6v2nl+tL4X5ZvW0qMf1Pda6cHB1R4jvQ0zoZZGouifsYcfq7zd8CUICdBQ3RFm3vdDGNVG2urkeLK+MJcaKerM3WgQ0Nsg1Yee55LHE3+XI71Bf1fHf388vUIuFMSHI5IiJ5v6+/beyZmZsFY778lEJ/NhiD9evibcKEESw+FCPYHNk5UViK3Hg7jhBTmrR4bwKoWp80N69q+AwLwLtLM+P91gykOP2M1N/WznolXwVCyeGqzHYzlHg+M8yZwP334EvdgBZHtknmzxXBDwWph8/JJRJ7NtxAJk+8ZUcgwO4dIrVlN6Vo5asmPujDRwNpiKdDZpgighl9+v2V0kTy4pgxWmAXtfpi3KPSgLqxgq90hNOA2OYrFePyeiMREilxy5tZu/I931YzvWyldJbXyj3DZMyBO9p+/jnybTp6FI0ZOvx3+t/nJKrAJrQKphCcyhV40kAVNmUipzvJlT3VwYA+LpE/FnEML1v4C+1BGsSAAsSMWkWRUak/AjrEgW+FJkAoA==~-1~-1~-1~AAQAAAAF%2f%2f%2f%2f%2f9eWWtEtZczy7CYPZFTXaCAwkBMNFqo+TTO%2fHCGsVs8pA50wtDWtDz5B+CL%2fpH3k7ioq0OT8qBKKEI82at53SURSn6vkOPUeyNjgGv4aeYn%2fXJgp8tO9i4rRQdZxyDU2ckQEIeo%3d~-1',
            'utm_track_v1': '%7B%22utm_source%22%3A%22direct%22%2C%22utm_medium%22%3A%22direct%22%2C%22trackstart%22%3A1776760080%2C%22trackend%22%3A1776760140%7D',
            'user_session': 't1iAxhdjGUI0EnOFb0vXBg.G-8KFE10yxljLOIf1c3aTI8EOo-efqQ0NOKR1o9su04J3iWG46E5R3zkyo1s6V5Gx4pdrGNkAO-H114gAzSZLhVPAvdLct_pj-NU8AVvjYyOgFCqh4fOKlwROrcbRAYTUYlpkdlY3H5GzeBexvn5eA.1776760066090.86400000.CH3eBMvm26F6aLQTA6GLrSzs0uOstHOcTAqRcwWjq_k',
            '_scid_r': 'AzVd1yPd6f1KSk8K_0gppcjKGVzfLCFXujA26g',
            'utrid': 'AGFWQ3xAYkYDYHB7fBhAMCM0Mjg5MDc1MDUxJDI%3D.b119ff0dd4ebbc2873e3b1911a1fef00',
            'bm_sv': '34959C7E6EAA36D8AE294679463E8F25~YAAQVqXBFwvN1n2dAQAAR2Enrx9dAeEPHT329QR6pDFVfiHIiq/1xV3X6T+/t3dxMi67Oat4ujW87ixuab3igiMgJuTRaQSZqSGOCTlDkJlTMxh8q+nIOvQpnia+KlRWm00bqHbLULQAV0ZpFdEji+GHxTDjDWWu2+sKKmHoXsiMX2LSQwg5Zy2gYcSU9DGEnfjKSRWEvCxDdy0EvvzRmYdoFMipyTkdUVVktqnXyU1/PY2ZwSEAFZluWm6EO2zfIQ==~1',
            'ak_RT': '"z=1&dm=myntra.com&si=686120a8-81b4-4caa-98f7-91dcb6d74821&ss=mo8c8saa&sl=2&tt=2c4&rl=1&nu=4bkc2l3d&cl=tnk4&obo=1&ld=tnlz&r=21mcuug3&ul=ue38&hd=tnvv"',
        }
        headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html",
    "Connection": "keep-alive",
}
    
        yield scrapy.Request(url=self.start_urls[0],headers=headers,cookies=cookies,callback=self.parse)
    
    #parse fuctionto scrape all categories urls
    def parse(self, response):
        categories = response.xpath("//div[contains(@class,'desktop-navContent')]")

        for cat in categories:

            main_category = cat.xpath(
                ".//a[contains(@class,'desktop-main')]/text()"
            ).get()

            subcategories = cat.xpath(
                ".//ul[contains(@class,'desktop-navBlock')]//a"
            )

            for sub in subcategories:
                subcategory = sub.xpath("text()").get()
                link = sub.xpath("@href").get()
                if link .startswith("http"):
                    final_link= link
                final_link= "https://www.myntra.com"+link
               
                yield {
                    "category": main_category,
                    "subcategory": subcategory,
                    "link": final_link,
                    "status": "pending"
                }
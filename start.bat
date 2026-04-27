@echo off

start "Terminal 1" cmd /k "scrapy crawl prodlinks -a start=0 -a end=50"
start "Terminal 2" cmd /k "scrapy crawl prodlinks -a start=50 -a end=100"
start "Terminal 3" cmd /k "scrapy crawl prodlinks -a start=100 -a end=150"
start "Terminal 4" cmd /k "scrapy crawl prodlinks -a start=150 -a end=200"
start "Terminal 5" cmd /k "scrapy crawl prodlinks -a start=250 -a end=300"
start "Terminal 6" cmd /k "scrapy crawl prodlinks -a start=300 -a end=350"
start "Terminal 7" cmd /k "scrapy crawl prodlinks -a start=350 -a end=400"

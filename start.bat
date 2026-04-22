@echo off

start "Terminal 1" cmd /k "scrapy crawl prodlinks -a start=0 -a end=100"
start "Terminal 2" cmd /k "scrapy crawl prodlinks -a start=100 -a end=200"
start "Terminal 3" cmd /k "scrapy crawl prodlinks -a start=200 -a end=300"
start "Terminal 4" cmd /k "scrapy crawl prodlinks -a start=300 -a end=400"
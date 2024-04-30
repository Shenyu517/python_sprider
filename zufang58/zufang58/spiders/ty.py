import sys
import scrapy
from zufang58.items import Zufang58Item
from itertools import zip_longest
class TySpider(scrapy.Spider):
    name = "ty"
    allowed_domains = ["ty.58.com"]
    def start_requests(self):
        for page in range(1,71):
            yield scrapy.Request(url=f'https://ty.58.com/chuzu/pn{page}/')
            
    def parse(self, response):
        titles = response.xpath('//div[@class="des"]//a[@class="strongbox"]/text()').getall()
        moneys = [value + unit for value, unit in zip([money.strip() for money in response.xpath('//div[@class="money"]//text()').getall() if money.strip()][::2], [money.strip() for money in response.xpath('//div[@class="money"]//text()').getall() if money.strip()][1::2])if value.strip() and unit.strip()]
        areas = response.xpath('//div[@class="des"]/p[@class="room"]/text()').getall()
        addresss = response.xpath('//p[@class="infor"]/a[1]/text()').getall()
        address_details = response.xpath('//p[@class="infor"]/a[2]/text()').getall()
        for title, money, area, address, address_detail in zip(titles, moneys, areas, addresss, address_details):
            item = Zufang58Item()
            item['title'] = title.strip() 
            item['money'] = money.strip()
            item['area'] = area.replace('\xa0', '').strip()
            item['address'] = address.strip() 
            item['address_detail'] = address_detail.strip()
            yield item
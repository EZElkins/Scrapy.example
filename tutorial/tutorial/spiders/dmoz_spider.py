import scrapy
from scrapy.http import Request
from tutorial.items import DmozItem

class DmozSpider(scrapy.Spider):
	name = 'dmoz'
	allowed_domains = 'dmoztools.net'
	start_urls = [
		'http://dmoztools.net/Computers/Programming/Languages/Python/Books/',
        'http://dmoztools.net/Computers/Programming/Languages/Python/Resources/'
	]

	def start_requests(self):
		headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'}
		for url in self.start_urls: 
			yield Request(url, headers = headers)

	def parse(self, response):
		# filename = response.url.split("/")[-2]
		# with open(filename, "wb") as f:
		# 	f.write(response.body)
		for sel in response.xpath('//div[@class="results browse-content"]//div[@class="site-item "]/div[@class="title-and-desc"]'):
			item = DmozItem()
			item['title'] = sel.xpath('a/div[@class="site-title"]/text()').extract()
			item['link'] = sel.xpath('a/@href').extract()
			item['desc'] = sel.xpath('div[@class="site-descr "]/text()').extract()
			yield item

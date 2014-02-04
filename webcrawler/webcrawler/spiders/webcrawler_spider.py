from scrapy.spider import Spider
from scrapy.selector import Selector

from webcrawler.items import WebcrawlerItem

class WebcrawlerSpider(Spider):
	name = 'webcrawler'
	allowed_domains = ["rithium.com"]

	start_urls = [
		"http://www.rithium.com"
	]

	def parse(self, response):
		sel = Selector(response)
		sites = sel.xpath('//html/head')
		items = []

		for site in sites:
			item = WebcrawlerItem()
		
			item['url'] = site.xpath('title/text()').extract()
			item['link'] = site.xpath('script/@src').extract()
			items.append(item)

		return items		

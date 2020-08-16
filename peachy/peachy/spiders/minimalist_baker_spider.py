import scrapy
from peachy.items import RecipeItem

class MinimalistBakerSpider(scrapy.Spider):
	name = 'minimalist_baker_spider'
	start_urls = [ 'https://minimalistbaker.com/recipe-index?fwp_special-diet=vegan&fwp_paged=57' ]

	def parse(self, response):
		for recipeLink in response.css('.post-summary__title'):
			recipe = RecipeItem()
			recipe['url'] = recipeLink.css('a::attr(href)').get()
			recipe['title'] = 'test'
			recipe['image_url'] = 'test'
			yield recipe
		
		if len(response.css('.post-summary__title')) > 0:
			next_page_number = int(response.url.split('fwp_paged=')[1]) +  1
			next_page = f'https://minimalistbaker.com/recipe-index?fwp_special-diet=vegan&fwp_paged={next_page_number}'
			yield response.follow(next_page, callback=self.parse)
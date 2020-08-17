import scrapy
from peachy.items import RecipeItem

class MinimalistBakerSpider(scrapy.Spider):
	name = 'minimalist_baker_spider'
	start_urls = [ 'https://minimalistbaker.com/recipe-index?fwp_special-diet=vegan&fwp_paged=58' ]

	def parse(self, response):
		for recipeCard in response.css('.post-summary.primary'):
			recipe = RecipeItem()
			recipe['url'] = recipeCard.css('.post-summary__title a::attr(href)').get()
			recipe['title'] = recipeCard.css('.post-summary__title a::text').get()
			recipe['image_url'] = recipeCard.css('.post-summary__image img::attr(src)').get()
			yield recipe
		
		if len(response.css('.post-summary__title')) > 0:
			next_page_number = int(response.url.split('fwp_paged=')[1]) +  1
			next_page = f'https://minimalistbaker.com/recipe-index?fwp_special-diet=vegan&fwp_paged={next_page_number}'
			yield response.follow(next_page, callback=self.parse)
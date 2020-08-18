import scrapy
from peachy.items import RecipeItem
import re

class ForksOverKnivesSpider(scrapy.Spider):
	name = 'forks_over_knives_spider'
	start_urls = [ 'https://www.forksoverknives.com/recipes/page/64/?type=grid' ]

	def parse(self, response):
		if len(response.css('.post-holder .post-item h3 a')) == 0:
			return
			
		for recipeCard in response.css('.post-holder .post-item'):
			recipe = RecipeItem()
			recipe['url'] = recipeCard.css('h3 a::attr(href)').get()
			recipe['title'] = recipeCard.css('h3 a::text').get()
			recipe['image_url'] = recipeCard.css('img::attr(src)').get()
			yield recipe
		
		
		current_page_string = response.url.split('/page/')[1].split('/?type=grid')[0]
		next_page_number = int(current_page_string) + 1
		print(f'NEXT PAGE NUMBER={next_page_number}')
		next_page = f'https://www.forksoverknives.com/recipes/page/{next_page_number}/?type=grid'
		yield response.follow(next_page, callback=self.parse)
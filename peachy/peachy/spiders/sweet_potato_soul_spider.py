import scrapy
from peachy.items import RecipeItem
import re

class SweetPotatoSoulSpider(scrapy.Spider):
	name = 'sweet_potato_soul_spider'
	start_urls = [ 'https://sweetpotatosoul.com/recipes' ]

	def parse(self, response):
		if len(response.css('.recipe.active h4 a')) == 0:
			return
			
		for recipeCard in response.css('.recipe.active'):
			recipe = RecipeItem()
			recipe['url'] = recipeCard.css('h4 a::attr(href)').get()
			recipe['title'] = recipeCard.css('h4 a::text').get()
			recipe['image_url'] = recipeCard.css('img::attr(src)').get()
			yield recipe
import scrapy

class RecipeSpider(scrapy.Spider):
	name = 'recipespider'
	start_urls = [ 'https://minimalistbaker.com/recipe-index/?fwp_special-diet=vegan' ]

	def parse(self, response):
		for recipeLink in response.css('.post-summary__title'):
			yield { 'link' : recipeLink.css('a::attr(href)').get() }
		# TODO: go to recipe detail pages
		
		# TODO: go to next page
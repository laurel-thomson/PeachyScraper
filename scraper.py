import scrapy

class RecipeSpider(scrapy.Spider):
	name = 'recipespider'
	start_urls = [ 'https://minimalistbaker.com/recipe-index?fwp_special-diet=vegan&fwp_paged=57' ]

	def parse(self, response):
		for recipeLink in response.css('.post-summary__title'):
			yield { 'link' : recipeLink.css('a::attr(href)').get() }
		
		if len(response.css('.post-summary__title')) > 0:
			next_page_number = int(response.url.split('fwp_paged=')[1]) +  1
			next_page = f'https://minimalistbaker.com/recipe-index?fwp_special-diet=vegan&fwp_paged={next_page_number}'
			yield response.follow(next_page, callback=self.parse)
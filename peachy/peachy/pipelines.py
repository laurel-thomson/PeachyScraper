# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class PeachyPipeline:
	#def __init__(self):
		#set up database connection

	def process_item(self, item, spider):
		#save item in the database
		print(item)

		# IDEA: maybe the key could be a unique hash of the recipe's URL?? that way
		# the same recipe will always go to the same key and then duplicates are simply
		# saved over?
		return item
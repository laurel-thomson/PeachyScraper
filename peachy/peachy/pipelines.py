# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

class PeachyPipeline:
	def open_spider(self, spider):
		cred = credentials.Certificate('peachy/firebase_key.json')
		firebase_admin.initialize_app(cred, {
			'databaseURL' : 'https://friendly-chat-e1c79.firebaseio.com'
		})
		self.db_reference = db.reference('scrapedRecipes')

	def process_item(self, item, spider):
		self.db_reference.push({
			'name' : 'test'
		})
		print(item)

		# IDEA: maybe the key could be a unique hash of the recipe's URL?? that way
		# the same recipe will always go to the same key and then duplicates are simply
		# saved over?
		return item
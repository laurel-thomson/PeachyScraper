# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import hashlib

class PeachyPipeline:
	def open_spider(self, spider):
		cred = credentials.Certificate('peachy/firebase_key.json')
		firebase_admin.initialize_app(cred, {
			'databaseURL' : 'https://friendly-chat-e1c79.firebaseio.com'
		})
		self.db_reference = db.reference('scrapedRecipes')
	

	def process_item(self, item, spider):
		hashed_url = hashlib.md5(item['url'].encode()).hexdigest()
		self.db_reference.child(hashed_url).set({
			'url' : item['url'],
			'title' : item['title'],
			'imageUrl' : item['image_url']
		})

		return item
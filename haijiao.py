#coding=utf-8
#!/usr/bin/python
import sys
sys.path.append('..')
from base.spider import Spider
import base64
import json

class Spider(Spider):
	def init(self,extend=""):
		self.base_url = ""
		self.raw_json = "https://ghfast.top/https://raw.githubusercontent.com/YohannQin/my_test/refs/heads/main/hj_media_en.json"
		self.media_json_data = None
		self.id_map = None

	def homeContent(self,filter):
		classes = [{"type_name": "博主","type_id":"author"}]
		result = {"class": classes}
		return result

	def categoryContent(self,tid,pg,filter,extend):
		data = self.fetch(self.raw_json).text
		data = base64.b64decode(data)
		data = data.decode('utf-8')
		data = json.loads(data)
		#self.log(data)
		videos = data['list']
		self.media_json_data = data['list']
		self.id_map = {item["vod_id"]: item for item in self.media_json_data}
		result = {
			"page": pg,
			"pagecount": 1,
			"limit": len(videos),
			"total": len(videos),
			"list": videos
		}
		return result

	def detailContent(self,array):
		id = array[0]
		item = self.id_map.get(id)
		#self.log(item)
		vod = []
		vod.append(item)
		result = {"list": vod}
		return result

	def playerContent(self,flag,id,vipFlags):
		result = {
			'parse': 0,
			'url': id
		}
		return result

	def getName(self):
		return '色播聚合'

	def homeVideoContent(self):
		pass
	def isVideoFormat(self,url):
		pass
	def manualVideoCheck(self):
		pass
	def searchContent(self,key,quick):
		pass
	def destroy(self):
		pass
	def localProxy(self, param):
		pass
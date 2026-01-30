#coding=utf-8
#!/usr/bin/python
import sys
import json
import os
sys.path.append('..')
from base.spider import Spider

class Spider(Spider):
    def init(self,extend=""):
		self.base_url='http://api.hclyz.com:81/mf'
		self.json_file = "/storage/emulated/0/111/haijiao/conf/hjbox_media.json"
		self.raw_json = "https://ghfast.top/https://raw.githubusercontent.com/YohannQin/my_test/refs/heads/main/my_video.json"
        
	def homeContent(self,filter):
		classes = [{"type_name": "博主","type_id":"author"}]
		result = {"class": classes}
		return result

	def categoryContent(self,tid,pg,filter,extend):
		videos = [
			{
				"vod_id": "/12233",
				"vod_name": "55555",
				"vod_pic": "",
				"vod_remarks": "6666",
				"style": {"type": "rect", "ratio": 1.33}
			}
		]

        result = {
			"page": pg,
			"pagecount": 1,
			"limit": len(videos),
			"total": len(videos),
			"list": videos
		}
		return result

	def detailContent(self,array):
	    pass
	"""
		id = array[0]
		data = self.fetch(f'{self.base_url}/{id}').json()
		zhubo = data['zhubo']
		playUrls = '#'.join([f"{vod['title']}${vod['address']}" for vod in zhubo])
		vod = [{
			"vod_play_from": 'sebo',
			"vod_play_url": playUrls,
			"vod_content": 'https://github.com/fish2018',
		}]
		result = {"list": vod}
		return result
		"""

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

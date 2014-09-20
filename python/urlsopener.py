#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2
import urllib
import re
import thread
import time

class spider_model:
	def __init__(self):
		self.enable = False
		self.url = "http://www.ecjtu.net/html/ecjtunews1/"
	def GetPage(self,url):
		myUrl = url 
		user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
		headers = { 'User-Agent':user_agent }
		req = urllib2.Request(myUrl, headers = headers)
		myResponse = urllib2.urlopen(req)
		myPage = myResponse.read()
		unicodePage = myPage.decode("gbk")
		#print type(myPage).
		parttern = '<div.*?id="bigtitle".*?title="(.*?)">(.*?)</div>'
		myItem = re.findall(parttern, unicodePage,re.S)
		items = []
		for item in myItem:
			items.append([item[0].replace("\n",""),item[1].replace("\n","")])
		return items
		
	def Start(self):
		self.enable = True
		print u'loding...'
		result = self.GetPage(self.url)
		result = result
		for item in result:
			for itm in item:
				print itm
print u""" 开始嘛？quit退出"""
print u'enter start'
raw_input(' ')
myModel = spider_model()
myModel.Start()


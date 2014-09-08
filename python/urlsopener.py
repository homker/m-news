#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2
import urllib
import re
import thread
import time

class spider_model:
	def __init__(self):
		self.page = 1
		self.pages = []
		self.enable = False
	def GetPage(self,page):
		myUrl = "http://m.qiushibaike.com/hot/page" + page
		user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
		headers = { 'User-Agent':user_agent }
		req = urllib2.Request(myUrl, headers = headers)
		myResponse = urllib2.urlopen(req)
		myPage = myResponse.read()
		unicodePage = myPage.decode("utf-8")
		parttern = '<div.*?class="content".*?title="(.*?)">(.*?)</div>'
		myItem = re.findall(parttern, unicodePage,re.S)
		items = []
		for item in myItem:
			items.append([item[0].replace("\n",""),item[1].replace("\n","")])
		return items
	def LoadPage(self):
		while self.enable:
			if len(self.pages) < 2:
				try:
					myPage = self.GetPage(str(self.page))
					self.page += 1
					self.pages.append(myPage)
				except:
					print 'can\'t connect the server'
			else:
				time.sleep(1)
	def ShowPage(self,nowPage,page):
		i=0
		for items in nowPage:
			print u'第%d页' % page , items[0]  , items[1]
			i=i+1
			if i==10:			
				myInput = raw_input()
				if myInput == "quit":
					self.enable = False
					break
	def Start(self):
		self.enable = True
		page = self.page
		print u'loding...'
		thread.start_new_thread(self.LoadPage,())
		while self.enable:
			if self.pages:
				nowPage = self.pages[0]
				del self.pages[0]
				self.ShowPage(nowPage,page)
				page += 1
print u""" 开始嘛？quit退出"""
print u'enter start'
raw_input(' ')
myModel = spider_model()
myModel.Start()


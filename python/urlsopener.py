#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2
import urllib
import re
import thread
import time
import HTMLParser
import json
from htmlentitydefs import entitydefs

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
		'''
		partternB = '<div.*?id="bigtitle".*?href="(.*?)".*?>(.*?)</a>'
		partternG = '<a *?href="(.*?)".*?>(.*?)</a>'
		myItem = re.findall(partternG, unicodePage,re.S)
		items = []
		for item in myItem:
			items.append(['http://www.ecjtu.net'+item[0],item[1].replace("\n","")])
		return items
		'''
		return unicodePage
		
	def Start(self):
		self.enable = True
		print u'spider works'
		result = self.GetPage(self.url)
		return result

class parser_model(HTMLParser.HTMLParser):

	def __init__(self):
		self.taglevels = []
		self.handledtags = ['a']
		self.precessing = None
		self.linkstring = ''
		self.linkaddr = ''
		self.content = []
		HTMLParser.HTMLParser.__init__(self)
		
	def handle_starttag(self, tag, attrs):
		if tag in self.handledtags:
			for name,value in attrs:
				if name == 'href':
					if value.find('http://') == -1:
						value = 'http://www.ecjtu.net'+value
					self.linkaddr = value
			self.precessing = tag

	def handle_data(self,data):
		if self.precessing:
			#print self.precessing
			self.linkstring += data
			
	def handle_endtag(self,tag):
		if tag == self.precessing:
			q = self.linkstring
			if q.find('...') == -1 and len(q) != 0 and q.find('more>>') == -1:
				res = {'title':self.linkstring.encode('utf-8'),'url':self.linkaddr.encode('utf-8') }
				self.content.append(res)
			self.precessing = None
			self.linkstring = ''
			
	def handle_entityref(self, name):
		if entitydefs.has_key(name):
			self.handle_data(entitydefs[name])
		else:
			self.handle_data('&'+name+';')
			
	def handle_charref(self,name):
		try:
			charnum = int(name)
		except ValueError:
			return
		if charnum<1 or charnum>255:
			return
		self.handle_data(chr(charnum))
	
	def gettitle(self):
		return self.linkaddr
		
		
def start():
	print u"""start work"""
	myModel = spider_model()
	page = myModel.Start()
	content = parser_model()
	content.feed(page)
	json_code = json.dumps(content.content)
	#print type(json_code);
	return json_code


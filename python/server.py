#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SimpleHTTPServer import SimpleHTTPRequestHandler
import urlsopener

class TestHTTPHandle(BaseHTTPRequestHandler):

    def do_GET(self):
        self.protocal_version = "HTTP/1.1" 
        self.send_response(200)
        self.send_header("Welcome", "Contect")
        content = urlsopener.start()
        #print content
        self.end_headers()
        self.wfile.write(content)
        print "spider end"

def start_server(port):
    http_server = HTTPServer(('', int(port)), TestHTTPHandle)
    print 'started httpserver'
    #server_handle = TestHTTPHandle()
    #server_handle.do_GET("hello")
    http_server.serve_forever() 
    
start_server(8000)

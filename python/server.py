#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SimpleHTTPServer import SimpleHTTPRequestHandler

class TestHTTPHandle(BaseHTTPRequestHandler):

    def do_GET(self):
        buf = 'It works'
        print buf
        self.protocal_version = "HTTP/1.1" 
        self.send_response(200)

        self.send_header("Welcome", "Contect")       

        self.end_headers()

        self.wfile.write(buf)

def start_server(port):
    http_server = HTTPServer(('', int(port)), TestHTTPHandle)
    print 'started httpserver'
    http_server.serve_forever() 
start_server(8000)



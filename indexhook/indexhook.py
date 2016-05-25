# Copyright 2016 unionpay
# All Rights Reserved.
#
# 此工具主要根据url对应的gitbase目录，使用python进入到此目录后，执行gitpull命令
# 可以扩展其它函数，由于此工具根据url触发，没有关注gitlab pull过来的参数，如果有需要

__author__ = 'linxuhua'

import SocketServer
import SimpleHTTPServer
import commands

''' mapping url to gitbase url'''
dicpath = {'/indexhook': '/home/jhsadmin/httpserver/pages'}


class HttpRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):

        if self.path in dicpath:

            gpath = dicpath[self.path]
            self.git_handler(gpath)

        else:
            SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):

        if self.path in dicpath:

            gpath = dicpath[self.path]
            self.git_handler(gpath)

        else:
            SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

    def git_handler(self, gitpath):

        print('prepared command')
        status, outputs = commands.getstatusoutput('cd {path};git pull'.format(path=gitpath))
        print('exec command')
        self.wfile.write('result : {status}\n'.format(status=status))
        print('print command')
        self.wfile.write('-----------------output------------------------\n')
        self.wfile.write(outputs)


httpServer = SocketServer.TCPServer(("", 2222), HttpRequestHandler)

httpServer.serve_forever()

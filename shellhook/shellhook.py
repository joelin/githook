# Copyright 2016 unionpay
# All Rights Reserved.
#
# 此工具主要根据url对应的shell文件，执行shell文件
# 可以扩展其它函数

__author__ = 'linxuhua'

import SocketServer
import SimpleHTTPServer
import commands

'''mapping url to shell'''
dicpath = {'/cstudy': '/home/jhsadmin/xhlin/ggzjs-tutorails/make.sh'}


class HttpRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):

        if self.path in dicpath:

            shellpath = dicpath[self.path]
            self.git_handler(shellpath)

        else:
            SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):

        if self.path in dicpath:

            shellpath = dicpath[self.path]
            self.git_handler(shellpath)

        else:
            SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

    def git_handler(self, shellpath):

        status, outputs = commands.getstatusoutput('sh {shellpath}'.format(shellpath=shellpath))
        self.wfile.write('result : {status}\n'.format(status=status))
        self.wfile.write('-----------------output------------------------\n')
        self.wfile.write(outputs)


httpServer = SocketServer.TCPServer(("", 2223), HttpRequestHandler)

httpServer.serve_forever()

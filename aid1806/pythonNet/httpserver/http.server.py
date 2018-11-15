#http.server.py
try:
    from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
except ImportError:
    from http.server import BaseHTTPRequestHandler,HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # print(self.headers)
        # print(self.request)
        fd = open('test.html','rb')
        content = fd.read()
        #组织response
        self.send_response(200)
        self.send_header('Content-Type','text/html')
        self.end_headers()
        self.wfile.write(content)


    def do_POST(self):
        pass

    def do_PUT(self):
        pass

address = ('0.0.0.0',8080)
#生成httpserver对象
httpd = HTTPServer(address,RequestHandler)
httpd.serve_forever() #启动服务器

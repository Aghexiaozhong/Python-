#sock_server1.py


from socketserver import *

class Server(ForkingMixIn,UDPServer):
    pass

class Handler(DatagramRequestHandler):
    def handle(self):
        while True:
            data = self.rfile.readline().decode()
            if not data:
                break
            print(data)
            #发送消息
            self.wfile.write(b'Receive\n')



server  = Server(('0.0.0.0',8888),Handler)

server.serve_forever()












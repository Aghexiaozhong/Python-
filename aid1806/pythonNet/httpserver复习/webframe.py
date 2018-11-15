from viws import *
STATIC_DIR = './static'

class application(object):
    def __init__(self,urls):
        self.urls = urls

    def __call__(self,env):
        method = env.get('METHOD','GET')
        path = env.get('FILE_PATH','/')

        if method == 'GET':
            if path == '/' or path[-5:] == '.html':
                response = self.get_html(path)

            else:
                response = self.get_data(path)


        return response

    def get_html(self,path):
        if path == '/':
            get_file = STATIC_DIR + '/index.html'

        else:
            get_file = STATIC_DIR +path

        try:
            fd = open(get_file)

            
        except IOError:
            responseheadrs = 'HTTP/1.1 404 not found\r\n'
            responseheadrs += '\r\n'
            response_body = 'Sorry,not found the page'
        else:
            responseheadrs = 'HTTP/1.1 200 OK\r\n'
            responseheadrs += '\r\n'
            response_body = fd.read() 

        finally:
            response = responseheadrs + response_body
            return response

    def get_data(self,path):
      

        for url,handler in self.urls:
            if path == url:
                responseheadrs = 'HTTP/1.1 200 OK\r\n'
                responseheadrs += '\r\n'
                response_body = handler()
                response = responseheadrs + response_body
                return response
        responseheadrs = 'HTTP/1.1 404 not found\r\n'
        responseheadrs += '\r\n'
        response_body = 'Sorry,not found the page'
        response = responseheadrs + response_body
        return response







urls = [('/time',say_time),
('/tedu',tedu),
('/bye',say_bye)
]

app = application(urls)












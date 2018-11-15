import cv2
import time
from socket import * 
from threading import Thread


class Moni_Server(object):
    def __init__(self,addr):
        self.sockfd = socket(AF_INET,SOCK_DGRAM)
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        self.sockfd.bind(ADDR)




def start_moni(c):
    camera = cv2.VideoCapture(0)  
    while True:
        (grabbed, img) = camera.read()              
        result, imgencode = cv2.imencode('.jpg',img,encode_param)        
        img_code = numpy.array(imgencode)        
        imgdata  = img_code.tostring()
        c.send(struct.pack("iii",len(imgdata),self.resolution[0],self.resolution[1])+imgdata)

def view_moni():
    pass
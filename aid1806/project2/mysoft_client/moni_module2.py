import cv2
import time
import numpy as np
from socket import *
import threading 
import struct
import os
class Moni_obj(object):
    def __init__(self,sockfd):
        self.s = sockfd
        self.file_id = 0
        self.num_frames = 0  # 捕获图像的总帧数
        self.out_fps = 24  # 输出文件的帧率
        self.check_flag = False
        self.a = True
        self.thread_flag = True
        self.start_flag = False
        self.image=0
        self.frame1=0
        self.frame2=0
        self.video=0
    def moni_rece(self):
        while self.thread_flag:        
            bufSize = int(struct.unpack("i",self.s.recv(4))[0])
            if bufSize:
#                try:
                frame = b''
                print('buf',bufSize)
                while(bufSize):  
                    #循环读取到一张图片的长度
                    tempBuf = self.s.recv(bufSize)
                    bufSize -= len(tempBuf)
                    frame += tempBuf
                    data = np.fromstring(frame,dtype='uint8')
                    self.image=cv2.imdecode(data,1)

                    if self.start_flag:
                        cv2.imshow('监控画面',self.image)
                        if cv2.waitKey(10) == 100: 
                            cv2.destroyAllWindows() 
                    self.frame1 = self.image
                    if self.a:
                        self.a=False
                    else:
                        self.moni_check()
                    self.frame2 = self.frame1
            self.s.send(b'd')
#                except:
#                    print("接收失败")                
#                    break
#                finally:                
                    # if cv2.waitKey(10) == 27:                                       
                    #     cv2.destroyAllWindows()                    
                    #     print("放弃连接")                    
                    #     break
        self.s.send(b'q')              
    def moni_check(self):
        if not self.num_frames:
            frame3=np.maximum(self.frame1,self.frame2)
            frame4=np.minimum(self.frame1,self.frame2)
            frame=np.subtract(frame3,frame4)
            a= frame.var()
            print('a',a)
            a = int(a)
            print(a)
        #     if int(a)>50:

        #         self.num_frames = 500
        #         self.check_flag = True
        # else:
        #     self.write()
    def write(self):
        if self.check_flag:
            print('检查到第%d次异常，开始录制！！！'% (self.file_id+1))
            size = (640,480)

            file_name = './video/mino_view%d.avi' % self.file_id

            # 设置要保存视频的编码，分辨率和帧率
            self.video = cv2.VideoWriter(
                file_name,
                cv2.VideoWriter_fourcc('M', 'P', '4', '2'),
                self.out_fps,
                size
            )
            self.check_flag = False

        else:
            self.video.write(self.image)
            self.num_frames-=1
            # 释放资源并写入视频文件
            if not self.num_frames:
                self.video.release()
                self.file_id+=1

def view_moni():
    while True:
        d={}
        num = 1
        filelist = os.listdir('./video')
        for i in filelist:
            d[str(num)]= i        
            print('%d.'%num,i)
            num+=1
            
        a = input('请输入要查看的录像的编码（按q退出）：')
        if a in d:
            filename = d[a]
            cap = cv2.VideoCapture("./video/%s" % filename)
            for i in range(500):
                ret,frame = cap.read()
                time.sleep(0.2)
            
                if frame==[]:
                    break
                cv2.imshow("capture",frame)
                if cv2.waitKey(100) & 0xFF == ord('q'):           
                    cv2.destroyAllWindows() 
                    cap.release()
                    break
            cv2.destroyAllWindows() 
            cap.release()
        elif a == 'q':
            break
        else:
            print('请输入正确的编码')
            continue
#day9.py

socket并发集成模块
python2  SocketServer
python3  socketserver

功能：通过模块提供的接口组合可以完成多进程
/多线程  tcp/udp 的并发程序


 StreamRequestHandler   处理tcp请求
 DatagramRequestHandler   处理udp请求
 
 ForkingMixIn  创建多进程
 ThreadingMixIn   创建多线程
 
 UDPServer   创建tcp  server
 TCPServer   创建udp server
 
 ForkingTCPServer    ForkingMixIn+TCPServer
 ForkingUDPServer    ForkingMixIn+ UDPServer
 ThreadingTCPServer   ThreadingMixIn+TCPServer
 ThreadingUDPServer   ThreadingMixIn+UDPServer
 
 













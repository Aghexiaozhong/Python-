#day07.py

信号

一个进程向另外一个进程通过信号的方式传递某种信息
接收方在接受到消息后作出相应的处理

kill -l  查看信号
kill -sig  PID 想一个进程发送信号

关于信号

信号名称：系统自定义，名字或者数字
信号含义：系统定义，信号的作用
默认处理方法：当一个进程接受到信号时，默认产生的效果
           终止进程  暂停进程  忽略发生

常见的信号

SIGHUP     断开链接
SIGINT     ctrl+c
SIGQUIT    ctrl+\
SIGKILL    终止进程且不能被处理
SIGALRM    时钟信号
SIGSTOP    暂停进程且不能被处理
SIGTSTP    ctrl+z
SIGCHLD    子进程状态改变发送给父进程信息号

python信号处理

os.kill(pid,sig)
功能：发送一个信号给某个进程
参数：pid  给哪个进程发信号
     sig  要发送什么信号

signal.alram(sec)
功能：设置时钟信号，在一定时间后会给自身发送SIGALRM信号
参数： sec 时间  （秒）


程序的同步执行和异步执行
同步执行：
   程序按照步骤一步一步执行，呈现一个先后性和顺序性
异步执行：
    程序在执行过程中利用内核功能帮助完成必要的辅助操作
    ，不影响应用层持续执行

一个进程只能有一个时钟，后来的时钟会覆盖前面的

signal.pause()
功能：阻塞进程  等待一个信号


signal.signal(sig,handler)
功能：处理信号
参数：sig 要处理的信号
     handler :  信号处理方法
      可选值：SIG_DFL  表示会用默认方法 
             SIG_IGM  表示忽略这个信号
             func  自定义函数
    自定义函数格式：def fnuc(sig,frame)（必须有两个形参）
                sig 接收到的信号
                frame  信号结构对象
signal函数也是一个异步处理函数，只要执行了该函数，则
进程任意时候接受到相应信号都能处理

signal 是不能处理SIGKILL  SIGSTOP 的
父进程中可以用  signal(SIGCHLD,SIG_IGN)将子进程
的推出交给系统处理
信号是一种异步的进程间通信方法

信号量

给定一定的数量，对多个进程可见，并且多个进程根据信号量多少
确定不同的行为

sem = Semaphore(num)
功能：创建信号量对象
参数：信号量的初始值   
返回值：信号量对象

sem.acquire()  将信号量-1   当数量为0则阻塞
sem.release()  将信号量+1
sem.get_value()  获取当期信号量的值


同步互斥机制
目的：解决对共有资源产生的资源争夺

临界资源：多个进程或者线程都能操作的资源
临界区：操作临界资源的代码段

同步：同步是一种合作关系，为完成某个任务，多进程
或者多线程之间形成一种协调，按照约定执行，
相互告知，共同完成任务


互斥：互斥是一种制约关系，当一个进程或者线程
进入临界区操作资源时采用上锁的方式，阻止其他进程操作，
直到解锁才会让出资源


Event 事件
from multiprocessing import Event

创建事件对象

e = Event()
事件阻塞
e.wait([timeout])
功能：使进程处于阻塞状态。直到事件对象被set

事件设置
e.set()
功能：让事件对象变为被设置状态

清除设置
e.clear()
功能：使事件对象清除设置状态

事件判断：判断当前事件对象的状态
e.is_set()


multiprocessing ---> lock
创建对象
 lock = Lock()

 lock.acquire()  上锁
 lock.release()  解锁
*如果一个锁对象已经被上锁则在调用acquire会阻塞
with lock: 上锁


多线程（thread）
线程：线程也是一种多任务编程方式，可以使用计算机的
多核资源，线程被称为轻量级的进程


线程特征：
*一个进程可以包含多个线程
*线程是计算机内核使用的最小单元
*线程也是一个运行过程，也要消耗计算机资源
*多个线程共享共用进程的资源
*线程也有自己的特征属性  TID 指令集 线程栈
*多个线程之间独立运行互不干扰
*线程的创建删除消耗的资源要小于进程


threading 模块
threading.Thread()
功能：创建线程对象
参数：  target  线程函数
       name    线程名称 默认Thread-1
       args   元祖   给线程函数位置传参
       kwargs 字典   给线程函数键值传参
返回：线程对象

t.start()   启动线程
t.join([timeout]) 回收线程



线程对象属性
t.name 线程名称
t.setName() 设置线程名称
t.is_alive()  查看线程状态
threading.currentThread() 获取当前线程对象

t.daemon 属性
默认情况下主线程的结束不会影响分支线程的执行

设置daemon 值
t.daemon = True(这时主线程的结束会影响分支线程的执行
主线程退出，则分支线程也会退出)

查看daemon 值
t.isDaemon()

创建自己的线程类

步骤：
1，继承Thread
2,加载父类 __init__
3,重写run


创建父子进程分别表示司机和售票员
当售票员捕捉到SIGINT信号时，给司机发送SIGUSER1信号
 此时司机打印'老司机开车了'

当售票员捕捉到SIGQUIT信号时，给司机发送SIGUSER2信号
  此时司机打印'车速有点快，系好安全带'

当司机捕捉到SIGTSTP信号时，给售票员发送SIGUSER1信号
 此时售票员打印'到站了请下车'

到站后，售票员先下车（子进程先退出），然后司机下车






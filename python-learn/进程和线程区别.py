"""
进程 能够完成多任务 运行多个软件
线程 能够完成多任务 软件中运行多个窗口
同一进程间的不同线程可以共享全局变量
不同进程间不能共享全局变量
一个程序至少有一个主进程 一个主进程里至少有一个主线程
线程不能够独立运行，必须依赖于进程
线程和进程在使用上各有优缺点 线程执行开销小，但不利于资源的管理和保护；而进程正相反
"""
import os,threading,multiprocessing
from multiprocessing import Queue

"""
进程共享全局变量
需要传参

队列的使用

"""
n = 100


def test():
    global n
    n += 1
    print('{}n的值是{}'.format(os.getpid(), hex(id(n))))


def demo():
    global n
    n += 1
    print('{}n的值是{}'.format(os.getpid(), hex(id(n))))


def producer():
    for i in range(10):
        print('生产了+++pid{}{}'.format(os.getpid(), i))


def consumer():
    for i in range(10):
        print('消费了+++pid{}{}'.format(os.getpid(), i))


# t1 = threading.Thread(target=test)
# t2 = threading.Thread(target=demo)
if __name__ == '__main__':
    # 创建队列时，可以指定最大长度 默认0 代表不限
    q = Queue(5)
    # 不同进程各自保存一份全局变量，不会共享全局变量
    # t1 = multiprocessing.Process(target=test)
    t1 = multiprocessing.Process(target=producer, args=(q, ))
    # t2 = multiprocessing.Process(target=demo)
    t2 = multiprocessing.Process(target=consumer, args=(q, ))

    # 同一个主进程里的两个子进程， 线程之间可以共享同一个进程的全局变量
    t1.start()
    t2.start()

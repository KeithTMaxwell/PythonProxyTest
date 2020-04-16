import threading
import time


class MyThread(threading.Thread):
    def __init__(self, func, *args):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args

    def run(self):
        if self.args is ():
            self.func()
        else:
            self.func(*self.args)

    def wait(self):
        if self.is_alive():
            self.join()


def func1(a, b, c):
    for i in range(20):
        print(a, b, c)
        time.sleep(1)


def func2():
    for i in range(10):
        print('thread func2')
        time.sleep(2)


t1 = MyThread(func1, 'this', 'is', 'thread func1')
t2 = MyThread(func2)

t1.start()
t2.start()

t1.wait()
t2.wait()
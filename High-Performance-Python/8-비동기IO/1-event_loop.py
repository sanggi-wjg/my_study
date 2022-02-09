import time
from queue import Queue


class EventLoop(Queue):

    def start(self):
        while True:
            func = self.get()
            func()


def hello_sleep():
    global eventloop
    print("hello")
    for _ in range(5):
        print('.')
        time.sleep(1)
    eventloop.put(world_sleep)


def world_sleep():
    global eventloop
    print("world")
    for _ in range(5):
        print('...')
        time.sleep(1)
    eventloop.put(hello_sleep)


eventloop = EventLoop()
eventloop.put(hello_sleep)
eventloop.start()

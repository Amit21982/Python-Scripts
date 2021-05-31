import thread
from time import sleep

def printlog(threadName,counter):
    """
    function to emulate thread behavior
    """
    while counter > 0:
        sleep(2)
        counter -= 1
        print('Name %s - Counter %s' % (threadName, str(counter)))

def run_sample():
    try:
        thread.start_new_thread(printlog, ('Thread 2',5))
        thread.start_new_thread(printlog, ('Thread 1',10))

    except:
        print('exception in thread')

    while 1:
        pass

from threading import Thread

class ThreadExample(Thread):
    def __init__(self, id, name, counter):
        Thread.__init__(self)
        self.thread_id= id
        self.name = name
        self.counter = counter

    def run(self):
        print('Thread Name %s' % (self.name))
        printlog(self.name,self.counter )
        print('Thread Name %s' % (self.name))

def invokethreadclass():
    t1 = ThreadExample(1, 'Thread 1', 10)
    t2 = ThreadExample(2, 'Thread 2', 5)

    threads = []
    t1.start()
    t2.start()
    threads.extend([t1, t2])

    for thread in threads:
        thread.join()

invokethreadclass()

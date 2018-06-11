import threading
import time


class threadingTest(threading.Thread):

    def __init__(self, threadCount, name, delay):
        threading.Thread.__init__(self)
        self.threadCount = threadCount
        self.name = name
        self.delay = delay

    def run(self):
        print("{0} started".format(self.name))
        n = 0
        while n < 5:
            time.sleep(self.delay)
            n += 1
            print(threading.currentThread().getName() + '-' + str())
        print("{0} ended ".format(self.name))


threads = [1, 2, 3]
for i in threads:
    t1 = threadingTest(i, 'Thread-' + str(i), i)
    t1.start()

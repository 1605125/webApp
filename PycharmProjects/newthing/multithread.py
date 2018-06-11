import threading
import time


def workerOne(name, delay):
    threading.currentThread().setName(name)
    print("STARTED -" + threading.currentThread().getName())
    n = 0
    lock.acquire()
    while n < 5:
        time.sleep(delay)
        print(threading.currentThread().getName() + "-" + str(n) + "\n")
        n += 1
    if threading.currentThread().getName() == 'Thread - 1':
        if threading.currentThread().is_alive():
            print("Still alive")
    print("Ended -" + threading.currentThread().getName())
    lock.release()


lock = threading.Lock()
t1 = threading.Thread(target=workerOne, args=('Thread - 1', 2))  # when it is receiving arguments or not
t2 = threading.Thread(target=workerOne, args=('Thread - 2', 2))
t1.start()
t2.start()
t1.join()  # wait all thread to terminate
t2.join()
print("Still m executing because i m in async process")
# current thread always maintaIN EXCECUTABLE THREAD

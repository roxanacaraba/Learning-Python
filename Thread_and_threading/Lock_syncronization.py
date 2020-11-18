#using lock.acquire si lock.release
import threading
import time
l = threading.Lock()


def threadfunction(lock, n_list, start):
    for i in range(0, 10):
        lock.acquire()
        n_list += [start+i]
        lock.release()
        time.sleep(1)


lst = []

t1 = threading.Thread(target=threadfunction, args=(l, lst, 100))

t2 = threading.Thread(target=threadfunction, args=(l, lst, 1000))
t1.start()
t2.start()
t1.join()
print(lst)

#using with lock
import threading,time
l= threading.Lock()
def ThreadFnc(lock,n_list,start):
    for i in range(0,10):
        with lock:n_list+=[start+i]
        time.sleep(1)
lst = []
t1 = threading.Thread(target=ThreadFnc, args=(l,lst,100))
t2 = threading.Thread(target=ThreadFnc, args=(l,lst,1000))
t1.start ()
t2.start ()
t1.join ()
t2.join ()
print(lst)
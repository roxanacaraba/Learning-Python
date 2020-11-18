# Provides access to a limited number of threads to a resource. It has the following functions:
# acquire
# release

import threading, time
s = threading.Semaphore(4)
def WorkerThread(id):
    global s
    with s:
        print("Thread - #" + str(id) + "enter")
        time.sleep(1)
        print("Thread - #" + str(id) + "exit")
t=[]
for i in range(0,10):
    t += [threading.Thread(target=WorkerThread, args=(i,))]
for _th in t: _th.start()
for _th in t: _th.join()
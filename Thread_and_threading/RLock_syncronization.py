# Allows reentrant lock (the same thread can lock a resources multiple times).
# RLock objects have two functions:
# 1. Python 3: Lock.acquire(blocking=True, timeout=-1) (timeout means how many seconds the Lock has to wait until it is acquired.
# Lock.release()  decreases the counter. Once it reaches 0, the lock is unlocked

# Within the same thread, be sure that the number of acquire queries is the same as the number  of release (otherwise you risk keeping the lock unlocked

import threading
l = threading.RLock()


def threadfunction1(lock):
     with lock:
         print("Function_1_called")


def threadfunction2(lock):
    with lock:
        print("Function_2_called")
        threadfunction1(lock)



t1 = threading.Thread(target=threadfunction1, args=(l,))
t2 = threading.Thread(target=threadfunction2, args=(l,))
t1.start()
t2.start()
t1.join()
t2.join()

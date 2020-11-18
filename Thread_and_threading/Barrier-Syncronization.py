# Provides a mechanism to wait for multiple threads to start at the same time.
# It has the following functions:
# wait  wait until the number if threads that need to pass a barrier is completed. Only then all threads are released and will continue their execution
#  Reset  resets the barrier
#  abort  aborts current barrier
# parties  number of parties (threads) that has to pass the barrier
# Barriers can not be used with "with" keyword.
# Barriers are available only on Python 3.

import threading
import time
b = threading.Barrier(2) # Each barrier waits for 2 thread.
# if we write Barrier(3) Threads will be group  in groups of 3.
# As there  are 10 threads, thread no. 10 will never end  (b.wait will wait until  two more threads will enter in the barrier).


def WorkerThread(b, id): #  The b_id parameter indicates the id of a thread inside abarrier.
    b_id = b.wait() # The call to wait exits only when all threads that need to pass the barrier are present (in this case from 2 to 2 threads).
    print("#" + str(id) + "pass the barrier =>" + str(b_id))
    time.sleep(2)
    print("#" + str(id) + "exit")


t = []
for i in range(0, 10):
    t += [threading.Thread(target=WorkerThread, args=(b, i))]
for _th in t:
    _th.start()
for _th in t:
    _th.join()


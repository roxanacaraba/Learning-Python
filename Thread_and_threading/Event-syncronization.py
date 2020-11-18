# Event object provides a way to synchronize execution between two or more threads.
# It has the following functions:
#  set  to signal the current state of the event
#  clear  to clear the current state of the event
#  wait  wait until the event is signaled ( a call to set method was made)
#  is_set  to check if an event was signaled
# Events can not be used with "with" keyword.
# To synchronize two thread, two Events are usually used.

import threading
e1 = threading.Event()
e2 = threading.Event()
e1.set()


def add_number(start, event1, event2, lista):
    for i in range(start, 10, 2):
        event1.wait()
        event1.clear()
        lista += [i]
        event2.set()


l = []


t1 = threading.Thread(target=add_number, args=(1, e1, e2, l))
t2 = threading.Thread(target=add_number, args=(2, e2, e1, l))
t1.start()
t2.start()
t1.join()
t2.join()
print(l)



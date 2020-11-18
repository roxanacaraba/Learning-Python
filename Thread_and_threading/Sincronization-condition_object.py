# Provides a notification system to other systems based on a condition. It has the following  methods:
# acquire
# release
# wait
# wait_for (Python 3)
# notify
# notify_all

# Conditional objects also support working with with keyword.

import threading
import time
c = threading.Condition()
number = 0


def ThreadConsumer():
    global number, c
    with c:
        if number == 0:
            c.wait()
            print("Consume:" + str(number))
            number = 0
def ThreadProducer():
    global number, c
    with c:
        time.sleep(2)
        number=5
        c.notify()
t1 = threading.Thread(target=ThreadConsumer)
t2 = threading.Thread(target=ThreadProducer)
t1.start()
t2.start()
t1.join()
t2.join()


import time
c = threading.Condition()
number = 0


def ThreadConsumer():
    global number, c
    with c:
            c.wait_for(lambda: number != 0)
            print("Consume:" + str(number))
            number = 0
def ThreadProducer():
    global number, c
    with c:
        time.sleep(2)
        number=5
        c.notify()
t1 = threading.Thread(target=ThreadConsumer)
t2 = threading.Thread(target=ThreadProducer)
t1.start()
t2.start()
t1.join()
t2.join()

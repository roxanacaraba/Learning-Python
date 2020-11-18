# Exemplul 1
"""
import threading
import time


def wait_some_seconds(secs):
    time.sleep(secs)


t = threading.Thread(target=wait_some_seconds, args=(5,))   # The target function expect a touple with arguments.
# If that touple contains only one parameter, a ‘,’ must be added to specify a touple.
t.start()
print("Wait for the thread to complete...")
t.join()
"""
# Exemplul 2
import threading
import time


def wait_some_seconds(secs, x, y):
    time.sleep(secs)
    print(x+y)


t = threading.Thread(target=wait_some_seconds, args=(2, 10, 15))
t.start()
print("Wait for the thread to complete...")
t.join()

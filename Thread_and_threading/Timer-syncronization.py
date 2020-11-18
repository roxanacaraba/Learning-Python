# Timer is an object deriver from Thread.
# It allows to run a code after a specific period of time.
# A timer also have a cancel method to stop the timer.

import threading
import time


def timerfunction(mesaj,):
    print(mesaj)


timer = threading.Timer(5, timerfunction, ("test after 5 seconds",))
timer.start()
timer.join()
print("done")

# Thread code will be added in “run” method.
import threading
import time

class Mythread(threading.Thread):
    def __init__(self, seconds):
        threading.Thread.__init__(self)
        self.seconds=seconds
    def run(self):
        time.sleep(self.seconds)


t = Mythread(10)
t.start()
print("Wait for the thread to complete...")
t.join()



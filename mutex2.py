import threading
from time import sleep
mutex = threading.Lock()

n=0
class Hilo(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id

    def run(self):
        mutex.acquire()
        sleep(3-self.id)
        d.append(self.id)
        mutex.release()

d=[];
hilos = [Hilo(1),
Hilo(2),
Hilo(3)]

for h in hilos:
    h.start()

mutex.acquire()
print (d)
mutex.release()
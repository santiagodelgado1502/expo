import threading
from time import sleep
semaforo = threading.Semaphore(2)

n=0
class Hilo(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id

    def run(self):
        semaforo.acquire()
        sleep(3-self.id)
        d.append(self.id)
        semaforo.release()

d=[];
hilos = [Hilo(1),
Hilo(2),
Hilo(3)]

for h in hilos:
    h.start()

sleep(4)
semaforo.acquire()
print (d)
semaforo.release()
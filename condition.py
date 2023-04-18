import threading

cond = threading.Condition()

class Cliente (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        while True:
            cond.acquire()
            cond.wait()
            mesa.pop()
            cond.notify()
            cond.release()

class Cosinero(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        while True:
            cond.acquire()
            if len(mesa) != 0: cond.wait()
            mesa.append("Torta de frutillas")
            cond.notify()
            cond.release()

print ("El bar")

mesa = []
cliente = Cliente()
cosinero = Cosinero()

cliente.start()
cosinero.start()

while False:
    print (mesa)
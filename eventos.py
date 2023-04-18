import threading

evento = threading.Event()

class Cliente (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        while True:
            self.evento.wait()
            mesa.pop()

class Cosinero(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        while True:
            if len(mesa) != 0: cond.wait()
            mesa.append("Torta de frutillas")
            evento.set()

print ("El bar")

mesa = []
cliente = Cliente()
cosinero = Cosinero()

cliente.start()
cosinero.start()

while True:
    print (mesa)
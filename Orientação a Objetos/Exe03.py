class Smartphone(object):
    def __init__(self, tamanho, interface):
        self.tamanho = tamanho
        self.interface = interface

class MP3Player(Smartphone):
    def __init__(self, capacidade, tamanho = 'Pequeno', interface = 'Led'):
        self.capacidade = capacidade
        Smartphone.__init__(self, tamanho, interface)
     
    def printMP3(self):
        print("Valores para  o objeto criado %s %s %s" %(self.tamanho, self.interface, self.capacidade))

dev = MP3Player('128')
dev.printMP3()
# DEPRECATED
class Aviao:

    def __init__(self, id):
        self.id = id
        self.tentrada = 0
        self.tatendido = 0
        self.tsaida = 0

    def esperando_decolagem(self,t): #entra na fila
        self.tentrada = t

    def comecou_decolagem(self): #sendo atendido
        global tatual
        self.tatendido = tatual
        tatual += 1

    def terminou_decolagem(self): #acabou o serviço
        global tatual
        self.tsaida = tatual
        tatual += 1

    def __str__(self):
        return "Id:{} | Entrada na fila: {} | Sendo atendido: {} | Saida: {}".format(self.id, self.tentrada, self.tatendido, self.tsaida)


class Caixa:

    def __init__(self):
        self.fila = []
        self.decolando = 0
        self.ids=1

    def coloca_fila_decolagem(self):
        aviao = Aviao(self.ids)
        self.ids += 1
        aviao.esperando_decolagem()
        self.fila.append(aviao)

    def liberado_para_decolagem(self, aviao):
        aviao.comecou_decolagem()
        self.fila.remove(aviao)
        self.decolando = aviao

    def decolou(self, aviao):
        aviao.terminou_decolagem()
        self.decolando = 0

    def tam_fila(self):
        return len(self.fila)

    def __str__(self):
        for item in self.fila:
            print(item)
        return "Decolando: {}\n".format(self.decolando)

'''
aeroporto = Caixa()
teste1 = Aviao(1)
teste2 = Aviao(2)
teste3 = Aviao(3)
aeroporto.coloca_fila_decolagem(teste1)
time.sleep(5)
aeroporto.coloca_fila_decolagem(teste2)
time.sleep(5)
time.sleep(5)
aeroporto.coloca_fila_decolagem(teste3)
time.sleep(5)
print(aeroporto)
aeroporto.liberado_para_decolagem(teste1)
print(aeroporto)
time.sleep(5)
aeroporto.liberado_para_decolagem(teste2)
print(aeroporto)
time.sleep(5)
aeroporto.liberado_para_decolagem(teste3)
print(aeroporto)
time.sleep(5)
aeroporto.decolou(teste1)
print(teste1)
'''
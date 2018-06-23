import time
from math import log
import numpy as np
import matplotlib.pyplot as plt
import random

def congruentelinear(m, a, c, seed, n_iter):
    resp = []
    for i in range(0, n_iter):
        x = (a*seed+c) % m
        resp.append(x/m)
        seed = x
    return resp


def congruentelinearexp(m, a, c, seed, n_iter, l):
    resp = []
    for i in range(0, n_iter):
        x = (a*seed+c) % m
        resp.append(log(1-x/m)/-l)
        seed = x
    return resp

# Hull-Dobell Theorem
# m and the offset are relatively prime,
# a-1 is divisible by all prime factors of m,
# a-1 is divisible by 4 if m is divisible by 4
# 2**32 = 4294967296
# print(congruentelinearexp(4294967296, 134775813, 1, 1996, 1000, 7))


# Model components -----------------------------

class Aviao:

    def __init__(self, id):
        self.id = id
        self.tentrada = 0
        self.tatendido = 0
        self.tsaida = 0

    def esperando_decolagem(self): #entra na fila
        self.tentrada = time.time()

    def comecou_decolagem(self): #sendo atendido
        self.tatendido = time.time()

    def terminou_decolagem(self): #acabou o serviço
        self.tsaida = time.time()

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

    def __str__(self):
        for item in self.fila:
            print(item)
        return "Decolando: {}\n".format(self.decolando)

# E[X]=5, lambda = 0.2
aeroporto = Caixa()

for i in range(1000):
    lista_random = congruentelinearexp(4294967296, 134775813, 1, 1996, 1000, 0.2)
    if(lista_random[i] > 0.5):
        aeroporto.coloca_fila_decolagem()

print(aeroporto)


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


import random
from math import log
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

seedX = 571294189234
seedY = 103495101020


def congruentelinear(m, a, c, seed, n_iter):
    resp = []
    for i in range(0, n_iter):
        x = (a*seed+c) % m
        resp.append(x/m)
        seed = x
    return resp


def lista_congruentelinearexp(m, a, c, seed, n_iter, l):
    resp = []
    for i in range(0, n_iter):
        x = (a*seed+c) % m
        resp.append(log(1-x/m)/-l)
        seed = x
    return resp


def congruentelinearexpX(m, a, c, l):
        global seedX
        x = (a * seedX + c) % m
        u = log(1-x/m)/-l
        seedX = x
        return u


def congruentelinearexpY(m, a, c, l):
    global seedY
    x = (a * seedY + c) % m
    u = log(1 - x / m) / -l
    seedY = x
    return u


# Hull-Dobell Theorem
# m and the offset are relatively prime,
# a-1 is divisible by all prime factors of m,
# a-1 is divisible by 4 if m is divisible by 4
# 2**32 = 4294967296
# print(congruentelinearexp(4294967296, 134775813, 1, 1996, 1000, 7))


# E[X]=0,09 segundos, lambda = 11.11
# E[C]=0,11 segundos, lambda = 9.09

def simulator(tempo_sim, tam_fila, capacidade_servico, taxa_chegada): #tempo em segundos!!!
    t = 0
    nfila = 0 # NAO É O TAMANHO DA FILA DE EVENTOS!!!!!!!!!!!!!!!!!!!!!
    lnfila = []
    nchegada = 0
    nsaida = 0
    descartes = 0
    fila_eventos = [["req_decolagem", t]] #1 e 2]]#4 chegada = req_decolagem
    c = []
    s = []
    tservico = 0
    while(t<tempo_sim):#5
        evento_atual = fila_eventos.pop(0)
        if(evento_atual[0]=="req_decolagem"):#3
            t = evento_atual[1]
            nchegada += 1
            if nfila < tam_fila:
                c.append(t)
                nfila += 1
            else:
                descartes += 1
            x = congruentelinearexpX(4294967296, 134775813, 1, 1/taxa_chegada) #1 e 2
            # x = np.random.exponential(0.09)
            fila_eventos.append(["req_decolagem", t+x])#4
            if nfila == 1:
                y = congruentelinearexpY(4294967296, 134775813, 1, 1/capacidade_servico)#1 e 2
                # y = np.random.exponential(0.11)
                tservico += y
                fila_eventos.append(["saida", t+y])#4
        else:  # 3
            t = evento_atual[1]
            nfila -= 1
            nsaida += 1
            s.append(t)
            if nfila > 0:
                y = congruentelinearexpY(4294967296, 134775813, 1, 1/capacidade_servico)  # 1 e 2
                tservico += y
                #y = np.random.exponential(0.11)
                fila_eventos.append(["saida", t+y])  # 4
        fila_eventos.sort(key=lambda teste: teste[1])  # 4
        lnfila.append(nfila)
    lim = min(len(s), len(c))
    w = np.asarray(s[:lim]) - np.asarray(c[:lim])
    lnfila = np.asarray(lnfila)
    return w.mean(), lnfila.mean(), descartes/nchegada, tservico/tempo_sim


#tmedio_sis,tammedio_fila,taxa_descartes,utilizacao = simulator(3600, 15, 0.09, 0.11)
#print("Tempo medio no sistema: {}".format(tmedio_sis))#tempo medio no sistema
#print("Tamanho medio da fila: {}".format(tammedio_fila))#tamanho medio da fila
#print("Taxa de descartes: {}".format(taxa_descartes))#taxa de descartes
#print("Utilizacao: {}".format(utilizacao))

taxas = [1/0.09, 1/0.1, 1/0.12, 1/0.14, 1/0.16, 1/0.18, 1/0.2]

'''
tmedio_sis1, tammedio_fila1, taxa_descartes1, utilizacao1 = simulator(3600, 15, 0.09, 0.11)
tmedio_sis2, tammedio_fila2, taxa_descartes2, utilizacao2 = simulator(3600, 15, 0.1, 0.11)
tmedio_sis3, tammedio_fila3, taxa_descartes3, utilizacao3 = simulator(3600, 15, 0.12, 0.11)
tmedio_sis4, tammedio_fila4, taxa_descartes4, utilizacao4 = simulator(3600, 15, 0.14, 0.11)
tmedio_sis5, tammedio_fila5, taxa_descartes5, utilizacao5 = simulator(3600, 15, 0.16, 0.11)
tmedio_sis6, tammedio_fila6, taxa_descartes6, utilizacao6 = simulator(3600, 15, 0.18, 0.11)
tmedio_sis7, tammedio_fila7, taxa_descartes7, utilizacao7 = simulator(3600, 15, 0.2, 0.11)
lis_tmedio = [tmedio_sis1, tmedio_sis2, tmedio_sis3, tmedio_sis4, tmedio_sis5, tmedio_sis6, tmedio_sis7]
lis_tanmedio = [tammedio_fila1, tammedio_fila2, tammedio_fila3, tammedio_fila4, tammedio_fila5, tammedio_fila6, tammedio_fila7]
lis_taxadesc = [taxa_descartes1, taxa_descartes2, taxa_descartes3, taxa_descartes4, taxa_descartes5, taxa_descartes6, taxa_descartes7]
lis_util = [utilizacao1, utilizacao2, utilizacao3, utilizacao4, utilizacao5, utilizacao6, utilizacao7]
print(lis_tmedio)
print(lis_tanmedio)
print(lis_taxadesc)
print(lis_util)
print(taxas)
#plt.plot(taxas, lis_tmedio)
#plt.show()
#plt.plot(taxas, lis_tanmedio)
#plt.show()
#plt.plot(taxas, lis_taxadesc)
#plt.show()
#plt.plot(taxas,lis_util)
#plt.show()
'''

for i in range(15):
    seedX = random.randint(0, 9999999999999999999999)
    seedY = random.randint(0, 9999999999999999999999)
    tmedio_sis1, tammedio_fila1, taxa_descartes1, utilizacao1 = simulator(3600, 15, 0.09, 0.11)
    tmedio_sis2, tammedio_fila2, taxa_descartes2, utilizacao2 = simulator(3600, 15, 0.1, 0.11)
    tmedio_sis3, tammedio_fila3, taxa_descartes3, utilizacao3 = simulator(3600, 15, 0.12, 0.11)
    tmedio_sis4, tammedio_fila4, taxa_descartes4, utilizacao4 = simulator(3600, 15, 0.14, 0.11)
    tmedio_sis5, tammedio_fila5, taxa_descartes5, utilizacao5 = simulator(3600, 15, 0.16, 0.11)
    tmedio_sis6, tammedio_fila6, taxa_descartes6, utilizacao6 = simulator(3600, 15, 0.18, 0.11)
    tmedio_sis7, tammedio_fila7, taxa_descartes7, utilizacao7 = simulator(3600, 15, 0.2, 0.11)
    lis_tmedio = [tmedio_sis1, tmedio_sis2, tmedio_sis3, tmedio_sis4, tmedio_sis5, tmedio_sis6, tmedio_sis7]
    print(lis_tmedio)
    plt.plot(taxas, lis_tmedio,"--o")
plt.show()
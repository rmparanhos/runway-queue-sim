from math import log
import numpy as np
import matplotlib.pyplot as plt


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

def simulator(tam_fila,capacidade_servico,taxa_chegada): #taxas em segundos!!!
    t = 0
    nfila = 0 # NAO É O TAMANHO DA FILA DE EVENTOS!!!!!!!!!!!!!!!!!!!!!
    lnfila = []
    nchegada = 0
    nsaida = 0
    descartes = 0
    fila_eventos = [["req_decolagem",t]] #1 e 2]]#4 chegada = req_decolagem
    c = []
    s = []
    while(t<3600):#5
        evento_atual = fila_eventos.pop(0)
        if(evento_atual[0]=="req_decolagem"):#3
            t = evento_atual[1]
            nchegada += 1
            if nfila < tam_fila:
                c.append(t)
                nfila += 1
            else:
                descartes += 1
            x = congruentelinearexpX(4294967296, 134775813, 1,1/taxa_chegada) #1 e 2
            # x = np.random.exponential(0.09)
            fila_eventos.append(["req_decolagem",t+x])#4
            if nfila == 1:
                y = congruentelinearexpY(4294967296, 134775813, 1, 1/capacidade_servico)#1 e 2
                # y = np.random.exponential(0.11)
                fila_eventos.append(["saida",t+y])#4
        else:#3
            t = evento_atual[1]
            nfila -= 1
            nsaida += 1
            s.append(t)
            if nfila > 0:
                y = congruentelinearexpY(4294967296, 134775813, 1, 1/capacidade_servico)#1 e 2
                #y = np.random.exponential(0.11)
                fila_eventos.append(["saida",t+y])#4
        fila_eventos.sort(key=lambda teste: teste[1])#4
        lnfila.append(nfila)
    return c,s,lnfila,descartes,nchegada

c,s,lnfila,descartes,nchegada = simulator(15,0.11,0.09)
w = np.asarray(s[:32361]) - np.asarray(c[:32361])
print(w.mean())#tempo medio no sistema
lnfila = np.asarray(lnfila)
print(lnfila.mean())#tamanho medio da fila
print(descartes/nchegada)#taxa de descartes
np.set_printoptions(suppress=True)
plt.plot(w)
plt.show()
#i=0
#for item in c:
#    print(s[i]-item)
#    i+=1





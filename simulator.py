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
t = 0
nfila = 0 # NAO É O TAMANHO DA FILA DE EVENTOS!!!!!!!!!!!!!!!!!!!!!
nchegada = 0
nsaida = 0
fila_eventos = [["chegada",t]]
c = []
s = []
while(t<3600):
    evento_atual = fila_eventos.pop(0)
    if(evento_atual[0]=="chegada"):
        t = evento_atual[1]
        nfila += 1
        nchegada += 1
        c.append(t)
        x = congruentelinearexpX(4294967296, 134775813, 1,11.11)
        fila_eventos.append(["chegada",t+x])
        if nfila == 1:
            y = congruentelinearexpY(4294967296, 134775813, 1, 9.09)
            fila_eventos.append(["saida",t+y])
    else:
        t = evento_atual[1]
        nfila -= 1
        nsaida += 1
        s.append(t)
        if nfila > 0:
            y = congruentelinearexpY(4294967296, 134775813, 1, 9.09)
            fila_eventos.append(["saida",t+y])
    fila_eventos.sort(key=lambda teste: teste[1])
    print(nfila)

w = np.asarray(s[:32595]) - np.asarray(c[:32595])
np.set_printoptions(suppress=True)
plt.plot(w)
plt.show()
#i=0
#for item in c:
#    print(s[i]-item)
#    i+=1





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


print(congruentelinearexp(4294967296, 134775813, 1, 1996, 1000, 7))


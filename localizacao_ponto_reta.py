import matplotlib.pyplot as plt
import numpy as np
import random as rnd


pontos = []

#Define os 3 pontos necessários, com os 2 primeiros sendo os formadores da reta e o 3o o independente
for _ in range(3):
    ponto = (rnd.uniform(0, 10), rnd.uniform(0, 10))
    while ponto[0] == ponto[1]:
        ponto = (rnd.uniform(0, 10), rnd.uniform(0, 10))
    pontos.append(ponto)
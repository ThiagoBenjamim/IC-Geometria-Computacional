import sys
from pathlib import Path

PASTA_RAIZ = Path(__file__).resolve().parent.parent
if str(PASTA_RAIZ) not in sys.path:
    sys.path.append(str(PASTA_RAIZ))


import random as rnd
import numpy as np
import src.classes_numpy as cl


def cramer(ponto, idx):

    S_den = np.copy(S_div)
    S_den[0][idx] = ponto.x
    S_den[1][idx] = ponto.y

    return np.linalg.det(S_den)/np.linalg.det(S_div)


#Cria o plano no qual estarão a reta e o plano
graf_min = 0
graf_max = 9
plano = cl.Plano(graf_min, graf_max)

ponto = cl.Ponto(plano, rnd.randint(graf_min, graf_max), rnd.randint(graf_min, graf_max))

triangulo = cl.PoligonoConvexo(plano, 3)

S_div = np.array([[i.x for i in triangulo.iter_pontos()], [i.y for i in triangulo.iter_pontos()], [1, 1, 1]])

ver_ponto_em_triangulo = "Ponto esta dentro do Poligono"
for idx in range(3):
    if cramer(ponto, idx) <= 0:
        ver_ponto_em_triangulo = "Ponto esta fora do Poligono"


triangulo.plot_poligono()
ponto.plot_point()
print(ver_ponto_em_triangulo)
plano.apresentar()
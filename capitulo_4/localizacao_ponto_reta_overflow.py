import sys
from pathlib import Path

PASTA_RAIZ = Path(__file__).resolve().parent.parent
if str(PASTA_RAIZ) not in sys.path:
    sys.path.append(str(PASTA_RAIZ))


import numpy as np
import src.classes_numpy as cl


#Cria o plano no qual estarão a reta e o plano
plano = cl.Plano(-(2**15), 2**15)


#Pontos para reta(A, B) e ponto C para comparação
pontos = {"A": cl.Ponto(plano.ax, 0, 0),
          "B": cl.Ponto(plano.ax, 2**15, 2**15),
          "C": cl.Ponto(plano.ax, -(2**15), 2**15, "blue")}

for ponto in pontos.values():
    ponto.vec = ponto.vec.astype(np.int32)

#Cria a reta
reta = cl.Reta(pontos["A"], pontos["B"])
if reta.ver_degenerado():
    raise ValueError("Caso de reta degenerada")

reta_ponto = cl.Reta(pontos["A"], pontos["C"])

produto_interno = reta_ponto.produto_interno(reta.perpendicular())

if produto_interno > 0:
    print("C esta a esquerda de AB")
elif produto_interno < 0:
    print("C esta a direita de AB")
elif produto_interno == 0:
    print("C esta em AB")
    if not reta.ver_vertical():
        x_a, x_b, x_c = [i.x for i in pontos.values()]
        men, mai = min(x_a, x_b), max(x_a, x_b)
        if men < x_c < mai: print("C esta entre A e B")
        elif x_c < men:
            if men == x_a: print("C esta antes de A")
            elif men == x_b: print("C esta depois de B")
        elif x_c > mai:
            if mai == x_a: print("C esta antes de A")
            elif mai == x_b: print("C esta depois de B")
        elif x_c == x_a: print("C esta em A")
        elif x_c == x_b: print("C esta em B")

    else:
        y_a, y_b, y_c = [i.y for i in pontos.values()]
        men, mai = min(y_a, y_b), max(y_a, y_b)
        if men < y_c < mai: print("C esta entre A e B")
        elif y_c < men:
            if men == y_a: print("C esta antes de A")
            elif men == y_b: print("C esta depois de B")
        elif y_c > mai:
            if mai == y_a: print("C esta antes de A")
            elif mai == y_b: print("C esta depois de B")
        elif y_c == y_a: print("C esta em A")
        elif y_c == y_b: print("C esta em B")


print(type(pontos["A"].vec[0]))
pontos["A"].adic_tit("A")
pontos["B"].adic_tit("B")
pontos["C"].adic_tit("C")
pontos["C"].plot_point()
reta.plot_reta_infinita()
plano.apresentar()
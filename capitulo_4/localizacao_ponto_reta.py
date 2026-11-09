import sys
from pathlib import Path

PASTA_RAIZ = Path(__file__).resolve().parent.parent
if str(PASTA_RAIZ) not in sys.path:
    sys.path.append(str(PASTA_RAIZ))


import random as rnd
import src.classes_numpy as cl


#Cria o plano no qual estarão a reta e o plano
graf_min = 0
graf_max = 10
plano = cl.Plano(graf_min, graf_max)

#Pontos para reta(A, B) e ponto C para comparação
pontos = {"A": cl.Ponto(plano.ax, rnd.randint(graf_min, graf_max), rnd.randint(graf_min, graf_max)),
          "B": cl.Ponto(plano.ax, rnd.randint(graf_min, graf_max), rnd.randint(graf_min, graf_max)),
          "C": cl.Ponto(plano.ax, rnd.randint(graf_min, graf_max), rnd.randint(graf_min, graf_max), "blue")}


#Cria a reta
reta = cl.Reta(pontos["A"], pontos["B"])
if reta.ver_degenerado():
    raise ValueError("Caso de reta degenerada")


def localizacao_ponto_reta(ponto, reta):

    reta_ponto = cl.Reta(reta.p1, ponto)
        
    produto_interno = reta_ponto.produto_interno(reta.perpendicular())

    if produto_interno > 0:
        return ["C esta a esquerda de AB"]
    elif produto_interno < 0:
        return ["C esta a direita de AB"]
    elif produto_interno == 0:
        resposta = ["C esta em AB"]
        if not reta.ver_vertical():
            x_a, x_b, x_c = reta.p1.x, reta.p2.x, ponto.x
            men, mai = min(x_a, x_b), max(x_a, x_b)
            if men < x_c < mai: resposta.append("C esta entre A e B")
            elif x_c < men:
                if men == x_a: resposta.append("C esta antes de A")
                elif men == x_b: resposta.append("C esta depois de B")
            elif x_c > mai:
                if mai == x_a: resposta.append("C esta antes de A")
                elif mai == x_b: resposta.append("C esta depois de B")
            elif x_c == x_a: resposta.append("C esta em A")
            elif x_c == x_b: resposta.append("C esta em B")
            
            return resposta
        else:
            y_a, y_b, y_c = reta.p1.y, reta.p2.y, ponto.y
            men, mai = min(y_a, y_b), max(y_a, y_b)
            if men < y_c < mai: resposta.append("C esta entre A e B")
            elif y_c < men:
                if men == y_a: resposta.append("C esta antes de A")
                elif men == y_b: resposta.append("C esta depois de B")
            elif y_c > mai:
                if mai == y_a: resposta.append("C esta antes de A")
                elif mai == y_b: resposta.append("C esta depois de B")
            elif y_c == y_a: resposta.append("C esta em A")
            elif y_c == y_b: resposta.append("C esta em B")

            return resposta


pontos["A"].adic_tit("A")
pontos["B"].adic_tit("B")
pontos["C"].adic_tit("C")
pontos["C"].plot_point()
reta.plot_reta_infinita()
print(localizacao_ponto_reta(pontos["C"], reta))
plano.apresentar()
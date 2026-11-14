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
pontos = {"A": cl.Ponto(plano, rnd.randint(graf_min, graf_max), rnd.randint(graf_min, graf_max)),
          "B": cl.Ponto(plano, rnd.randint(graf_min, graf_max), rnd.randint(graf_min, graf_max)),
          "C": cl.Ponto(plano, rnd.randint(graf_min, graf_max), rnd.randint(graf_min, graf_max), "blue")}


#Cria a reta
reta = cl.Reta(pontos["A"], pontos["B"])
if reta.ver_degenerado():
    raise ValueError("Caso de reta degenerada")


pontos["A"].adic_tit("A")
pontos["B"].adic_tit("B")
pontos["C"].adic_tit("C")
pontos["C"].plot_point()
reta.plot_reta_infinita()
print(reta.localizacao_ponto_reta(pontos["C"]))
plano.apresentar()
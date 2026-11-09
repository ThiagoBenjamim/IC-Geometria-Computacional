import sys
from pathlib import Path

PASTA_RAIZ = Path(__file__).resolve().parent.parent
if str(PASTA_RAIZ) not in sys.path:
    sys.path.append(str(PASTA_RAIZ))


import random as rnd
import src.classes_numpy as cl
from localizacao_ponto_reta import localizacao_ponto_reta


#Cria o plano no qual estarão a reta e o plano
graf_min = 0
graf_max = 30
plano = cl.Plano(graf_min, graf_max)

triangulo_A = cl.Ponto(plano.ax, rnd.randint(graf_min, graf_max), rnd.randint(graf_min, graf_max))
triangulo_A.adic_tit("A")
triangulo_B = cl.Ponto(plano.ax, rnd.randint(graf_min, graf_max), rnd.randint(graf_min, graf_max))
triangulo_B.adic_tit("B")
triangulo_C = cl.Ponto(plano.ax, rnd.randint(graf_min, graf_max), rnd.randint(graf_min, graf_max))
triangulo_C.adic_tit("C")


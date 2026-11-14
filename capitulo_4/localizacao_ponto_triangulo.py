import sys
from pathlib import Path

PASTA_RAIZ = Path(__file__).resolve().parent.parent
if str(PASTA_RAIZ) not in sys.path:
    sys.path.append(str(PASTA_RAIZ))


import random as rnd
import src.classes_numpy as cl


#Cria o plano no qual estarão a reta e o plano
graf_min = 0
graf_max = 9
plano = cl.Plano(graf_min, graf_max)

ponto = cl.Ponto(plano, rnd.randint(graf_min, graf_max), rnd.randint(graf_min, graf_max))

triangulo = cl.PoligonoConvexo(plano, 3)

triangulo.plot_poligono()
ponto.plot_point()
print(triangulo.localizacao_ponto_poligono(ponto))
plano.apresentar()
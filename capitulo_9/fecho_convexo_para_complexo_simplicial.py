import sys
from pathlib import Path

PASTA_RAIZ = Path(__file__).resolve().parent.parent
if str(PASTA_RAIZ) not in sys.path:
    sys.path.append(str(PASTA_RAIZ))


import random as rnd
import src.classes_numpy as cl


graf_min = 0
graf_max = 30
plano = cl.Plano(graf_min, graf_max)

fecho_convexo = cl.FechoConvexo(plano, n=10)

triangulacao = cl.TriangulacaoPontos(plano, fecho_convexo)

triangulacao.plot_triangulacao()
plano.apresentar()
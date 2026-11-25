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

max_tentativas = 10_000
tentativas = 0
while tentativas < max_tentativas:
    ponto = cl.Ponto(plano, rnd.randint(graf_min, graf_max), rnd.randint(graf_min, graf_max))
    try: triangulo = triangulacao.localizacao_ponto_triangulo(ponto); break
    except: tentativas += 1

if tentativas == max_tentativas:
    raise ValueError("Nao foi possivel estabelecer ponto dentro de FechoConvexo")

fatores = triangulo.cramer(ponto)
valores = [rnd.randint(0, 100) for _ in range(3)]
vertices = triangulo.pontos
valor_ponto = sum([fatores[i] * valores[i] for i in range(3)])


triangulacao.plot_triangulacao("red")
triangulo.plot_poligono("blue")
ponto.plot_point("green")
for idx, vertice in enumerate(vertices):
    vertice.adic_tit(valores[idx])
ponto.adic_tit(f"{valor_ponto:.2f}")
plano.apresentar()
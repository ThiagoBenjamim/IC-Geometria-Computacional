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
pontos = {"A": cl.Ponto(plano, 0, 0),
          "B": cl.Ponto(plano, 2**15, 2**15),
          "C": cl.Ponto(plano, -(2**15), 2**15, "blue")}

for ponto in pontos.values():
    ponto.vec = ponto.vec.astype(np.int32)

#Cria a reta
reta = cl.Reta(pontos["A"], pontos["B"])
if reta.ver_degenerado():
    raise ValueError("Caso de reta degenerada")


print(type(pontos["A"].vec[0]))
pontos["A"].adic_tit("A")
pontos["B"].adic_tit("B")
pontos["C"].adic_tit("C")
pontos["C"].plot_point()
reta.plot_reta_infinita()
print(reta.localizacao_ponto_reta(pontos["C"]))
plano.apresentar()
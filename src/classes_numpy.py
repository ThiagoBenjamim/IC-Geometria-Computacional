import matplotlib.pyplot as plt
import numpy as np
import random as rnd
import math


class Ponto:
    def __init__(self, plano, x, y):
        self.ax = plano.ax
        self.plano = plano
        self.vec = np.array([x, y])

    @property
    def x(self):
        return self.vec[0]

    @property
    def y(self):
        return self.vec[1]

    def plot_point(self, cor="red"):
        self.ax.scatter(self.x, self.y, c=cor)

    def __repr__(self):
        return f"Ponto({self.x}, {self.y})"

    def __add__(self, outro):
        if (isinstance(outro, list) or isinstance(outro, tuple) or isinstance(outro, np.ndarray)) and len(outro) == 2:
            return Ponto(self.plano, self.x + outro[0], self.y + outro[1])
        raise TypeError("Variavel nao compativel com soma com ponto")

    def __eq__(self, outro):
        if isinstance(outro, Ponto):
            if self.plano.ax == outro.plano.ax:
                if np.array_equal(self.vec, outro.vec):
                    return True
        return False

    def adic_tit(self, tit):
        self.ax.text(self.x + 0.05, self.y + 0.05, tit, fontsize=10, fontweight='bold')

    def dist_pontos(self, outro):
        if not isinstance(outro, Ponto):
            raise TypeError("Parametro inserido nao e da classe Ponto")

        return np.linalg.norm(self.vec - outro.vec)


class Reta:
    def __init__(self, ponto1, ponto2):
        if ponto1.ax != ponto2.ax:
            raise AttributeError("Os pontos pertencem a graficos diferentes")

        self.ax = ponto1.ax
        self.plano = ponto1.plano
        self.p1 = ponto1
        self.p2 = ponto2

    @property
    def vec(self):
        return self.p2.vec - self.p1.vec

    @property
    def x_coords(self):
        return np.array([self.p1.x, self.p2.x])

    @property
    def y_coords(self):
        return np.array([self.p1.y, self.p2.y])

    def perpendicular(self):
        dx, dy = self.vec

        p1_novo = Ponto(self.plano, self.p1.x, self.p1.y)
        p2_novo = Ponto(self.plano, self.p1.x - dy, self.p1.y + dx)

        return Reta(p1_novo, p2_novo)

    def produto_interno(self, outro):
        if not isinstance(outro, Reta):
            raise TypeError("Parametro inserido nao e outra Reta")

        return (np.inner(self.vec, outro.vec))

    def ver_degenerado(self):
        return (np.count_nonzero(self.vec) == 0)

    def ver_vertical(self):
        return (self.vec[0] == 0 and not self.ver_degenerado())

    def ver_horizontal(self):
        return (self.vec[1] == 0 and not self.ver_degenerado())

    def plot_reta_finita(self, cor="red"):
        self.ax.plot(self.x_coords, self.y_coords, color=cor, marker="o")

    def plot_reta_infinita(self, cor="red"):
        self.ax.axline(self.p1.vec, self.p2.vec, color=cor, linestyle="-")
        self.plot_reta_finita(cor)

    def determinante(self):
        return (self.p1.x * self.p2.y) - (self.p2.x * self.p1.y)

    def localizacao_ponto_reta(self, ponto) -> list:

        if not isinstance(ponto, Ponto):
            raise ValueError("Parametro inserido nao e um Ponto")

        reta_ponto = Reta(self.p1, ponto)
            
        produto_interno = reta_ponto.produto_interno(self.perpendicular())

        if self.ver_degenerado():
            return ["Reta degenerada", "Ponto nao esta na Reta"]

        if produto_interno > 0:
            return [True, "Ponto nao esta na Reta"]
        elif produto_interno < 0:
            return [False, "Ponto nao esta na Reta"]
        elif produto_interno == 0:
            resposta = []
            resposta.append(False)
            if not self.ver_vertical():
                x_a, x_b, x_c = self.p1.x, self.p2.x, ponto.x
                men, mai = min(x_a, x_b), max(x_a, x_b)
                if men < x_c < mai: resposta.append("Ponto esta entre A e B")
                elif x_c < men:
                    if men == x_a: resposta.append("Ponto esta antes de A")
                    elif men == x_b: resposta.append("Ponto esta depois de B")
                elif x_c > mai:
                    if mai == x_a: resposta.append("Ponto esta antes de A")
                    elif mai == x_b: resposta.append("Ponto esta depois de B")
                elif x_c == x_a: resposta.append("Ponto esta em A")
                elif x_c == x_b: resposta.append("Ponto esta em B")

                return resposta
            else:
                y_a, y_b, y_c = self.p1.y, self.p2.y, ponto.y
                men, mai = min(y_a, y_b), max(y_a, y_b)
                if men < y_c < mai: resposta.append("Ponto esta entre A e B")
                elif y_c < men:
                    if men == y_a: resposta.append("Ponto esta antes de A")
                    elif men == y_b: resposta.append("Ponto esta depois de B")
                elif y_c > mai:
                    if mai == y_a: resposta.append("Ponto esta antes de A")
                    elif mai == y_b: resposta.append("Ponto esta depois de B")
                elif y_c == y_a: resposta.append("Ponto esta em A")
                elif y_c == y_b: resposta.append("Ponto esta em B")

                return resposta
        return ["Reta degenerada", "Ponto nao esta na Reta"]

    def cruzamento_retas(self, outro):

        if not isinstance(outro, Reta):
            raise ValueError("Parametro inserido nao e uma Reta")

        a = outro.localizacao_ponto_reta(self.p1)
        b = outro.localizacao_ponto_reta(self.p2)
        c = self.localizacao_ponto_reta(outro.p1)
        d = self.localizacao_ponto_reta(outro.p2)
        
        cruzamento =(
            c[1] == "Ponto nao esta na Reta"
            and d[1] == "Ponto nao esta na Reta"
            and a[1] == "Ponto nao esta na Reta"
            and b[1] == "Ponto nao esta na Reta"
            and (c[0] != d[0])
            and (a[0] != b[0])
        )
        return cruzamento
    

class PoligonoConvexo:
    def __init__(self, plano, n):

        if (plano.max_val - plano.min_val) < n < 3:
            raise ValueError("Quantidade de pontos invalida para formar um poligono")

        self.ax = plano.ax
        self.plano = plano

        #Algoritmo de Valtr
        pontos_x = sorted(rnd.sample(range(*map(int, plano.min_max_val)), n))
        pontos_y = sorted(rnd.sample(range(*map(int, plano.min_max_val)), n))

        extremos = [pontos_x[0], pontos_x[-1], pontos_y[0], pontos_y[-1]]

        ran_dis = rnd.randint(1, n-1)
        shuffled = pontos_x[1:-1]
        rnd.shuffle(shuffled)
        x_inter = [shuffled[:ran_dis], shuffled[ran_dis:]]
        x_inter[0].sort(reverse=True)
        x_inter[1].sort()
        x_inter[0].insert(0, extremos[1])
        x_inter[0].append(extremos[0])
        x_inter[1].insert(0, extremos[0])
        x_inter[1].append(extremos[1])

        ran_dis = rnd.randint(1, n-1)
        shuffled = pontos_y[1:-1]
        rnd.shuffle(shuffled)
        y_inter = [shuffled[:ran_dis], shuffled[ran_dis:]]
        y_inter[0].sort(reverse=True)
        y_inter[1].sort()
        y_inter[0].insert(0, extremos[3])
        y_inter[0].append(extremos[2])
        y_inter[1].insert(0, extremos[2])
        y_inter[1].append(extremos[3])

        val_len = [len(x_inter[0]), len(x_inter[1])]
        difs_x = ([(x_inter[0][i+1] - x_inter[0][i]) for i in range(val_len[0]-1)] +
                [(x_inter[1][i+1] - x_inter[1][i]) for i in range(val_len[1]-1)])
        val_len = [len(y_inter[0]), len(y_inter[1])]
        difs_y = ([(y_inter[0][i+1] - y_inter[0][i]) for i in range(val_len[0]-1)] +
                [(y_inter[1][i+1] - y_inter[1][i]) for i in range(val_len[1]-1)])

        rnd.shuffle(difs_x)
        rnd.shuffle(difs_y)

        vetores = [[difs_x[i], difs_y[i]] for i in range(n)]

        vetores = sorted(vetores, key=lambda x: np.arctan2(x[1], x[0]))
        
        coords = np.vstack(([0, 0], np.cumsum(vetores[:-1], axis=0)))
        desloc_x = extremos[0] - coords[:, 0].min()
        desloc_y = extremos[2] - coords[:, 1].min()
        coords[:, 0] += desloc_x
        coords[:, 1] += desloc_y

        self.pontos = np.array([Ponto(plano, x, y) for x, y in coords])

        self.retas = np.array([Reta(self.pontos[i], self.pontos[(i+1)%len(self.pontos)]) for i in range(len(self.pontos))])

    def __len__(self):
        return len(self.retas)

    def iter_retas(self):
        return iter(self.retas)

    def iter_pontos(self):
        return iter(self.pontos)

    def localizacao_ponto_poligono_generalizacao(self, ponto):
        for reta in self.iter_retas():
            if reta.localizacao_ponto_reta(ponto)[0] == False:
                return False
        return True

    def localizacao_ponto_poligono_reta_log(self, ponto):
        esq = 1
        dir = len(self)-1

        while dir - esq > 1:
            meio = ((dir + esq)//2)
            diagonal = Reta(self.pontos[0], self.pontos[meio])
            resultado = diagonal.localizacao_ponto_reta(ponto)

            if resultado[1] == "Ponto esta entre A e B":
                return True
            elif resultado[1] != "Ponto nao esta na Reta":
                return False
            elif resultado[0]:
                esq = meio
            else:
                dir = meio

        if not Reta(self.pontos[dir], self.pontos[0]).localizacao_ponto_reta(ponto)[0]:
            return False
        if not Reta(self.pontos[0], self.pontos[esq]).localizacao_ponto_reta(ponto)[0]:
            return False
        if not Reta(self.pontos[esq], self.pontos[dir]).localizacao_ponto_reta(ponto)[0]:
            return False

        return True

    def plot_poligono(self, cor="red"):
        for reta in self.iter_retas():
            reta.plot_reta_finita(cor)


class PoligonoGeral:
    def __init__(self, plano, n):

        if n < 3:
            raise ValueError("Numero de Pontos insuficiente para formar Poligono")

        self.ax = plano.ax
        self.plano = plano

        pontos = []
        tentativas = 0
        tentativas_max = 10000*n
        while len(pontos) < n:
            tentativas += 1
            novo_ponto = Ponto(plano, rnd.randint(plano.min_val, plano.max_val), rnd.randint(plano.min_val, plano.max_val))

            if novo_ponto in pontos:
                continue

            colinear = False
            for i in range(len(pontos)):
                for j in range(i + 1, len(pontos)):
                    if Reta(pontos[i], pontos[j]).localizacao_ponto_reta(novo_ponto)[1] != "Ponto nao esta na Reta":
                        colinear = True
                        break
                if colinear: break
            if not colinear: pontos.append(novo_ponto)

            if tentativas >= tentativas_max:
                raise ValueError("Nao foi possivel formar o Poligono")

        retas = [Reta(pontos[i], pontos[(i+1)%n]) for i in range(n)]
        varredura_incompleta = True
        while varredura_incompleta:
            varredura_incompleta = False
            for i in range(n):
                for j in range(i+1, n):
                    if retas[i].cruzamento_retas(retas[j]):
                        retas[i], retas[j] = Reta(retas[i].p1, retas[j].p1), Reta(retas[i].p2, retas[j].p2)
                        retas[i + 1 : j] = [Reta(r.p2, r.p1) for r in reversed(retas[i + 1 : j])]
                        varredura_incompleta = True

        soma_dets = sum([i.determinante() for i in retas])
        if soma_dets < 0:
            retas = [Reta(reta.p2, reta.p1) for reta in retas]
            retas.reverse()

        self.retas = np.array(retas)
        self.pontos = np.array([reta.p1 for reta in retas])

    def __len__(self):
        return len(self.retas)

    def iter_retas(self):
        return iter(self.retas)

    def iter_pontos(self):
        return iter(self.pontos)

    def plot_poligono(self, cor="red"):
        for reta in self.iter_retas():
            reta.plot_reta_finita(cor)

    def localizacao_ponto_poligono_ray_casting(self, ponto):

        for reta in self.retas:
            resultado = reta.localizacao_ponto_reta(ponto)
            if resultado[1] in {"Ponto esta em A", "Ponto esta em B", "Ponto esta entre A e B"}:
                return False

        cruzamentos = 0
        for reta in self.retas:
            y1 = reta.p1.y
            y2 = reta.p2.y
            if y1 < y2:
                reta_aux = Reta(reta.p1, reta.p2)
                if y1 <= ponto.y < y2:
                    if reta_aux.localizacao_ponto_reta(ponto)[0]:
                        cruzamentos += 1
            if y1 > y2:
                reta_aux = Reta(reta.p2, reta.p1)
                if y1 > ponto.y >= y2:
                    if reta_aux.localizacao_ponto_reta(ponto)[0]:
                        cruzamentos += 1

        if (cruzamentos%2) == 1: return True
        else: return False

#==================================================================================

class FechoConvexo(PoligonoConvexo):
    def __init__(self, plano, pontos=None, n=None):

        if n is None and pontos is None:
            raise ValueError("Um dos parâmetros precisa ser definido")

        if n is None and pontos is not None:
            n = len(pontos)

        self.ax = plano.ax
        self.plano = plano

        if pontos is None and n is not None:
            lista_pontos = []
            tentativas = 0
            tentativas_max = 10000 * n
            while len(lista_pontos) < n:
                if tentativas >= tentativas_max:
                    raise ValueError("Nao foi possivel sortear n pontos distintos no plano")
                tentativas += 1

                novo_ponto = Ponto(
                    plano,
                    rnd.randint(plano.min_val, plano.max_val),
                    rnd.randint(plano.min_val, plano.max_val),
                    )
                if novo_ponto not in lista_pontos:
                    lista_pontos.append(novo_ponto)
        elif pontos is not None:
            lista = []
            for ponto in pontos:
                if ponto not in lista:
                    lista.append(ponto)
            if len(lista) < len(pontos):
                raise ValueError("Parametro pontos inválido")
            lista_pontos = pontos

        self.todos_pontos = np.array(lista_pontos)

        ordenados = sorted(lista_pontos, key=lambda p: (p.x, p.y))

        inferior = []
        for p in ordenados:
            while len(inferior) >= 2 and not Reta(inferior[-2], inferior[-1]).localizacao_ponto_reta(p)[0]:
                inferior.pop()
            inferior.append(p)

        superior = []
        for p in reversed(ordenados):
            while len(superior) >= 2 and not Reta(superior[-2], superior[-1]).localizacao_ponto_reta(p)[0]:
                superior.pop()
            superior.append(p)

        vertices_fecho = inferior[:-1] + superior[:-1]

        if len(vertices_fecho) < 3:
            raise ValueError("Todos os pontos sorteados sao colineares; nao formam poligono")

        self.pontos = np.array(vertices_fecho)
        self.retas = np.array([
            Reta(self.pontos[i], self.pontos[(i + 1) % len(self.pontos)])
            for i in range(len(self.pontos))
        ])
        self.pontos_internos = np.array([ponto for ponto in self.todos_pontos if ponto not in self.pontos])

    def iter_todos_pontos(self):
        return iter(self.todos_pontos)

    def plot_poligono(self, cor="red"):
        for ponto in self.iter_todos_pontos():
            ponto.plot_point(cor)
        for reta in self.iter_retas():
            reta.plot_reta_finita(cor)

    def len_total(self):
        return len(self.todos_pontos)


class Triangulo(PoligonoConvexo):
    def __init__(self, plano, pontos=None):

        self.plano = plano
        self.ax = plano.ax

        if pontos is None:
            while True:
                pontos = [Ponto(plano, 
                        rnd.randint(plano.min_val, plano.max_val), 
                        rnd.randint(plano.min_val, plano.max_val))
                        for _ in range(3)]
                if Reta(pontos[0], pontos[1]).localizacao_ponto_reta(pontos[2])[1] == "Ponto nao esta na Reta" and not Reta(pontos[0], pontos[1]).ver_degenerado():
                    break
        elif len(pontos) == 3:
            pontos = list(pontos)
            if Reta(pontos[0], pontos[1]).localizacao_ponto_reta(pontos[2])[1] != "Ponto nao esta na Reta" or Reta(pontos[0], pontos[1]).ver_degenerado():
                raise ValueError("Pontos inválidos para formação de Triangulo")
        else:
            raise ValueError("Numero de pontos diferente de 3")

        if not Reta(pontos[0], pontos[1]).localizacao_ponto_reta(pontos[2])[0]:
            pontos.reverse()

        self.pontos = np.array(pontos)
        self.retas = np.array([Reta(pontos[i], pontos[(i+1)%3]) for i in range(3)])

    def cramer(self, ponto):

        eq1 = [self.pontos[i].x for i in range(3)]
        eq2 = [self.pontos[i].y for i in range(3)]
        eq3 = [1, 1, 1]

        return np.linalg.solve([eq1, eq2, eq3], [ponto.x, ponto.y, 1])


class TriangulacaoPontos:
    def __init__(self, plano, pontos=None, n=0):

        if pontos is None and n < 3:
            raise ValueError("Numero de pontos insuficiente para realizar TriangulacaoPontos")
        
        if pontos is None:
            pontos = FechoConvexo(plano, n=n)

        if not isinstance(pontos, FechoConvexo):
            try:
                self.fecho_convexo = FechoConvexo(plano, pontos)
            except: raise ValueError("Parametro pontos invalido para criar FechoConvexo")
        else:
            self.fecho_convexo = pontos

        self.plano = plano
        self.ax = plano.ax

        ancora = self.fecho_convexo.pontos[0]
        triangulos_iniciais = [Triangulo(plano, [ancora, self.fecho_convexo.pontos[i], self.fecho_convexo.pontos[i + 1]])
                                for i in range(1, len(self.fecho_convexo.pontos) - 1)]
        
        for ponto in self.fecho_convexo.pontos_internos:
            proximos_triangulos = []
            for triangulo in triangulos_iniciais:
                if triangulo.localizacao_ponto_poligono_generalizacao(ponto):
                    for idx in range(3):
                        proximos_triangulos.append(Triangulo(plano, [triangulo.pontos[idx],triangulo.pontos[(idx+1)%3], ponto]))
                    continue

                edge_idx = None
                for idx, reta in enumerate(triangulo.retas):
                    if reta.localizacao_ponto_reta(ponto)[1] == "Ponto esta entre A e B":
                        edge_idx = idx
                        break

                if edge_idx is not None:
                    va = triangulo.pontos[edge_idx]
                    vb = triangulo.pontos[(edge_idx + 1) % 3]
                    v_oposto = triangulo.pontos[(edge_idx + 2) % 3]
                    proximos_triangulos.append(Triangulo(plano, (va, ponto, v_oposto)))
                    proximos_triangulos.append(Triangulo(plano, (ponto, vb, v_oposto)))
                else:
                    proximos_triangulos.append(triangulo)

            triangulos_iniciais = proximos_triangulos

        self.triangulos = np.array(triangulos_iniciais)

        arestas_unicas = []
        vistos = set()
        for triangulo in self.triangulos:
            for reta in triangulo.retas:
                set_ver = frozenset({(reta.p1.x, reta.p1.y), (reta.p2.x, reta.p2.y)})
                if set_ver not in vistos:
                    arestas_unicas.append(reta)
                    vistos.add(set_ver)
        self.retas = np.array(arestas_unicas)

    def localizacao_ponto_triangulo(self, ponto: Ponto):
        for triangulo in self.triangulos:
            if triangulo.localizacao_ponto_poligono_generalizacao(ponto):
                return triangulo
            for reta in triangulo.retas:
                if reta.localizacao_ponto_reta(ponto)[1] in ("Ponto esta em A", "Ponto esta em B", "Ponto esta entre A e B"):
                    return triangulo
        raise ValueError("Parametro Ponto esta fora do Triangulo")

    def plot_triangulacao(self, cor="red"):
        for reta in self.retas:
            reta.plot_reta_finita(cor)


class TriangulacaoPontosSweepLine(TriangulacaoPontos):
    def __init__(self, plano, pontos=None, n=0):
        if pontos is None and n < 3:
            raise ValueError("Numero de pontos insuficiente para realizar TriangulacaoPontos")
        
        if pontos is None:
            pontos = FechoConvexo(plano, n=n)

        if not isinstance(pontos, FechoConvexo):
            try:
                self.fecho_convexo = FechoConvexo(plano, pontos)
            except: raise ValueError("Parametro pontos invalido para criar FechoConvexo")
        else:
            self.fecho_convexo = pontos

        self.plano = plano
        self.ax = plano.ax

        pontos_ordenados = sorted(self.fecho_convexo.pontos, key=lambda p: (p.x, p.y))
        total = len(pontos_ordenados)

        reta_ancora = Reta(pontos_ordenados[0], pontos_ordenados[1])
        m = 2
        while m < total and reta_ancora.localizacao_ponto_reta(pontos_ordenados[m])[1] != "Ponto nao esta na Reta":
            m += 1

        triangulos = [Triangulo(plano, 
                                (pontos_ordenados[m], pontos_ordenados[i], pontos_ordenados[i+1]))
                                for i in range(total-1)]

        if Reta(pontos_ordenados[0], pontos_ordenados[m - 1]).localizacao_ponto_reta(pontos_ordenados[m])[0]:
            sequencia = pontos_ordenados[:m] + [pontos_ordenados[m]]
        else:
            sequencia = [pontos_ordenados[m]] + list(reversed(pontos_ordenados[:m]))

        pontos_iniciais = [ListaEncadeada(p) for p in sequencia]
        cont_pontos = len(pontos_iniciais)

        ponto_ultimo = pontos_iniciais[0] if sequencia[0] == pontos_ordenados[m] else pontos_iniciais[-1]

        raise NotImplementedError("Classe ainda não implementada")


class ListaEncadeada:
    def __init__(self, ponto: Ponto):
        self.ponto = ponto
        self.next = None
        self.prev = None

#==================================================================================


class Plano:
    def __init__(self, min_val, max_val):
        plt.style.use('_mpl-gallery')

        if min_val >= max_val:
            raise ValueError("Valor mínimo para o gráfico não pode ser maior ou igual do que o valor máximo")
        self.min_val = min_val
        self.max_val = max_val
        self.fig, self.ax = plt.subplots()
        self.ax.set(xlim=(min_val, max_val), xticks=np.linspace(min_val, max_val, 11),
            ylim=(min_val, max_val), yticks=np.linspace(min_val, max_val, 11))
        self.fig.subplots_adjust(
            left=0.04,
            right=0.96,
            top=0.96,
            bottom=0.04
        )

    @property
    def min_max_val(self):
        return [self.min_val, self.max_val]

    def apresentar(self):
        plt.show()
import matplotlib.pyplot as plt
import numpy as np
import random as rnd


class Ponto:
    def __init__(self, plano, x, y, cor="red"):
        self.ax = plano.ax
        self.plano = plano
        self.vec = np.array([x, y])
        self.cor = cor

    @property
    def x(self):
        return self.vec[0]

    @property
    def y(self):
        return self.vec[1]

    def plot_point(self):
        self.ax.scatter(self.x, self.y, c=self.cor)

    def __repr__(self):
        return f"Ponto({self.x}, {self.y})"

    def __add__(self, outro):
        if isinstance(outro, list) or isinstance(outro, tuple) or isinstance(outro, np.ndarray):
            return Ponto(self.plano, self.x + outro[0], self.y + outro[1])
        raise TypeError("Variavel nao compativel com soma com ponto")

    def adic_tit(self, tit):
        self.ax.text(self.x + 0.05, self.y + 0.05, tit, fontsize=10, fontweight='bold')

    def dist_pontos(self, outro):
        if not isinstance(outro, Ponto):
            raise TypeError("Parametro inserido nao e da classe Ponto")

        return np.linalg.norm(self.vec - outro.vec)


class Reta:
    def __init__(self, ponto1, ponto2, cor="red"):
        if ponto1.ax != ponto2.ax:
            raise AttributeError("Os pontos pertencem a graficos diferentes")

        self.ax = ponto1.ax
        self.plano = ponto1.plano
        self.p1 = ponto1
        self.p2 = ponto2
        self.cor = cor

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

        p1_novo = Ponto(self.plano, self.p1.x, self.p1.y, self.p1.cor)
        p2_novo = Ponto(self.plano, self.p1.x - dy, self.p1.y + dx, self.p2.cor)

        return Reta(p1_novo, p2_novo, self.cor)

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

    def plot_reta_finita(self):
        self.ax.plot(self.x_coords, self.y_coords, color=self.cor, marker="o")

    def plot_reta_infinita(self):
        self.ax.axline(self.p1.vec, self.p2.vec, color=self.cor, linestyle="-")
        self.plot_reta_finita()

    def localizacao_ponto_reta(self, ponto):

        reta_ponto = Reta(self.p1, ponto)
            
        produto_interno = reta_ponto.produto_interno(self.perpendicular())

        if produto_interno > 0:
            return ["Ponto esta a esquerda de AB"]
        elif produto_interno < 0:
            return ["Ponto esta a direita de AB"]
        elif produto_interno == 0:
            resposta = ["Ponto esta em AB"]
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
    

class PoligonoConvexo:
    def __init__(self, plano, n):

        if n < 3:
            raise ValueError("Quantidade de pontos insuficiente para formar um poligono")

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

        self.retas = np.array([Reta(self.pontos[i], self.pontos[(i+1)%len(self.pontos)], "blue") for i in range(len(self.pontos))])

    def __len__(self):
        return len(self.retas)

    def __iter__(self):
        return iter(self.retas)

    def localizacao_ponto_poligono(self, ponto):
        for reta in self:
            if reta.localizacao_ponto_reta(ponto)[0] == "Ponto esta a direita de AB":
                return "Ponto esta fora do Poligono"
        return "Ponto esta dentro do Poligono"

    def plot_poligono(self):
        for reta in self:
            reta.plot_reta_finita()
    

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
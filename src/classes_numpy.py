import matplotlib.pyplot as plt
import numpy as np


class Ponto:
    def __init__(self, ax, x, y, cor="red"):
        self.ax = ax
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

        p1_novo = Ponto(self.ax, self.p1.x, self.p1.y, self.p1.cor)
        p2_novo = Ponto(self.ax, self.p1.x - dy, self.p1.y + dx, self.p2.cor)

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
    

class Plano:
    def __init__(self, min_val, max_val):

        plt.style.use('_mpl-gallery')

        self.fig, self.ax = plt.subplots()
        self.ax.set(xlim=(min_val, max_val), xticks=np.linspace(min_val, max_val, 11),
            ylim=(min_val, max_val), yticks=np.linspace(min_val, max_val, 11))
        self.fig.subplots_adjust(
            left=0.04,
            right=0.96,
            top=0.96,
            bottom=0.04
        )

    def apresentar(self):
        plt.show()
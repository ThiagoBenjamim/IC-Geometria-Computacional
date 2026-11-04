'''Este codigo possui algumas implementacoes proprias das classes usadas nos arquivos,
essas classes nao serao utilizadas nos codigos de implementacao das Notas de Geometria computacional,
nao estao completas e foram criadas por curiosidade.'''
import matplotlib.pyplot as plt
import numpy as np


class Ponto:
    def __init__(self, ax, x, y, cor="red"):
        self.ax = ax
        self.x_point = x
        self.y_point = y
        self.cor = cor

    def plot_point(self):
        self.ax.scatter(self.x_point, self.y_point, c=self.cor)

    def __repr__(self):
        return f"Ponto({self.x_point}, {self.y_point})"

    @property
    def coord(self):
        return (self.x_point, self.y_point)

    def adic_tit(self, tit):
        self.ax.text(self.x_point + 0.05, self.y_point + 0.05, tit, fontsize=10, fontweight='bold')


class Reta:
    def __init__(self, ponto1, ponto2, cor="red"):
        if ponto1.ax != ponto2.ax:
            raise AttributeError("Pontos de mesma reta estão em gráficos diferentes")
        self.ax = ponto1.ax
        self.ponto1 = ponto1
        self.ponto2 = ponto2
        self.cor = cor

    @property
    def x_coords(self):
        return [self.ponto1.x_point, self.ponto2.x_point]

    @property
    def y_coords(self):
        return [self.ponto1.y_point, self.ponto2.y_point]

    @property
    def dif_x(self):
        return self.ponto2.x_point - self.ponto1.x_point

    @property
    def dif_y(self):
        return self.ponto2.y_point - self.ponto1.y_point

    @property
    def dif_xy(self):
        return (((self.dif_x)**2) + ((self.dif_y)**2))**(1/2)

    def plot_reta_finita(self):
        self.ax.plot(self.x_coords, self.y_coords, color=self.cor, marker="o")
    
    def plot_reta_infinita(self):
        self.ax.axline(self.ponto1.coord, self.ponto2.coord, color=self.cor, linestyle="-")
        self.plot_reta_finita()
    
    def perpendicular(self):
        dx = self.ponto2.x_point - self.ponto1.x_point
        dy = self.ponto2.y_point - self.ponto1.y_point

        p1_novo = Ponto(self.ax, self.ponto1.x_point, self.ponto1.y_point, self.cor)
        p2_novo = Ponto(self.ax, self.ponto1.x_point - dy, self.ponto1.y_point + dx, self.cor)

        return Reta(p1_novo, p2_novo, self.cor)

    def produto_interno(self, outro):

        if not isinstance(outro, Reta):
            raise TypeError("Classe inserida nao é uma Reta")

        prod_int = (self.dif_x * outro.dif_x) + (self.dif_y * outro.dif_y)
        return prod_int

class Plano:
    def __init__(self, min_val, max_val):

        plt.style.use('_mpl-gallery')

        self.fig, self.ax = plt.subplots()
        self.ax.set(xlim=(min_val, max_val), xticks=np.linspace(min_val, max_val, 11),
            ylim=(min_val, max_val), yticks=np.linspace(min_val, max_val, 11))

    def apresentar(self):
        plt.show()
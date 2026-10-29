import matplotlib.pyplot as plt
import numpy as np

def criar_plano(min, max):

    freq_linhas = (max - min)/10

    fig, ax = plt.subplots(figsize=(10, 10))
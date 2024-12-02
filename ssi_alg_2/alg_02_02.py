import numpy as np
import matplotlib.pyplot as plt
import random


def plot():
    # Tworzenie siatki danych
    x1 = np.linspace(0, 100, 100)
    x2 = np.linspace(0, 100, 100)
    X, Y = np.meshgrid(x1, x2)

    # Definiowanie funkcji
    Z = np.sin(X * 0.05) + np.sin(Y * 0.05) + 0.4 * np.sin(X * 0.15) * np.sin(Y * 0.15)

    # Wykres konturowy
    contour1 = plt.contour(X, Y, Z, levels=10, cmap='viridis')
    plt.clabel(contour1, inline=True, fontsize=8)

    # Wyświetlenie wykresu
    plt.tight_layout()


N = 4
r_inercji = 0
r_glob = 0.05
r_lok = 0.8

iteracja_liczba = 20
x_glob = []

x_min = 0
x_max = 100
punkty_startowe = []
x_lok = []

for i in range(N):
    x1 = np.random.uniform(x_min, x_max)
    x2 = np.random.uniform(x_min, x_max)

    punkty_startowe.append([x1, x2])
    x_lok.append([x1, x2])

V_2d = np.zeros((N, 2))


def Func(x1, x2):
    return np.sin(x1 * 0.05) + np.sin(x2 * 0.05) + 0.4 * np.sin(x1 * 0.15) * np.sin(x2 * 0.15)

for iter in range(iteracja_liczba):
    punkty_startowe_ocenione = [Func(x1, x2) for x1, x2 in punkty_startowe]
    x_lok_ocenione = [Func(x1, x2) for x1, x2 in x_lok]

    if iter == 0:
        ocena_x_glob = np.argmax(punkty_startowe_ocenione)
        x_glob = punkty_startowe[ocena_x_glob]

        min_ocena_x_glob = np.argmin(punkty_startowe_ocenione)
        min_x_glob = punkty_startowe[min_ocena_x_glob]

        x = [x_values[0] for x_values in punkty_startowe]
        y = [y_values[1] for y_values in punkty_startowe]

        plot()
        plt.scatter(x, y, color='blue')
        plt.scatter(x_glob[0], x_glob[1], color='green')
        plt.scatter(min_x_glob[0], min_x_glob[1], color='red')

    else:
        ocena_x_glob = np.argmax(punkty_startowe_ocenione)
        if x_glob < punkty_startowe[ocena_x_glob]:
            x_glob = punkty_startowe[ocena_x_glob]

    for j in range(0, len(punkty_startowe)):
        if x_lok_ocenione[j] < punkty_startowe_ocenione[j]:
            x_lok[j]= punkty_startowe[j]

    for j in range(0, len(punkty_startowe)):
        rnd_glob = random.uniform(0, 1)
        rnd_lok = random.uniform(0, 1)

        for i in range(0, len(punkty_startowe[j])):
            V_2d[j][i] = V_2d[j][i] * r_inercji + (x_glob[i] - punkty_startowe[j][i]) * r_glob * rnd_glob + (x_lok[j][i] - punkty_startowe[j][i]) * r_lok * rnd_lok
            punkty_startowe[j][i] += V_2d[j][i]

    x = [x_values[0] for x_values in punkty_startowe]
    y = [y_values[1] for y_values in punkty_startowe]

    plot()
    plt.scatter(x, y, color='blue')
    plt.scatter(x_glob[0], x_glob[1], color='green')

    plt.show()




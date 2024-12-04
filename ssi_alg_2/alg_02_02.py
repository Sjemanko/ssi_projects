import numpy as np
import matplotlib.pyplot as plt
import random

global_static_points = []

def plot():
    # dane
    x1 = np.linspace(0, 100, 100)
    x2 = np.linspace(0, 100, 100)
    X, Y = np.meshgrid(x1, x2)

    Z = np.sin(X * 0.05) + np.sin(Y * 0.05) + 0.4 * np.sin(X * 0.15) * np.sin(Y * 0.15)

    # Wykres konturowy
    contour1 = plt.contour(X, Y, Z, levels=10, cmap='viridis')
    plt.clabel(contour1, inline=True, fontsize=8)
    plt.tight_layout()


def Func(x1, x2):
    return np.sin(x1 * 0.05) + np.sin(x2 * 0.05) + 0.4 * np.sin(x1 * 0.15) * np.sin(x2 * 0.15)


def main(N, r_inercji, r_glob, r_lok, iteracja_liczba, iterations, punkty_startowe=None):
    # ZMIANA - USTAWIENIE PUNKTÓW NA SZTYWNO
    # if punkty_startowe is None:
    #     punkty_startowe = []
    #
    #     x_glob = []
    #     x_lok = []
    #     x_min = 0
    #     x_max = 100
    #
    #     for i in range(N):
    #         x1 = np.random.uniform(x_min, x_max)
    #         x2 = np.random.uniform(x_min, x_max)
    #
    #         punkty_startowe.append([x1, x2])
    #         x_glob.append([x1, x2])
    #         x_lok.append([x1, x2])
    #         global_static_points.append([x1, x2])

    punkty_startowe=[[58,28], [64, 28], [58, 32], [64, 32]]
    global_static_points = punkty_startowe.copy()
    x_glob = punkty_startowe.copy()
    x_lok = punkty_startowe.copy()

    min_x_glob = []

    V_2d = np.zeros((N, 2))

    for iter in range(iteracja_liczba):
        punkty_startowe_ocenione = [Func(x1, x2) for x1, x2 in punkty_startowe]
        x_lok_ocenione = [Func(x1, x2) for x1, x2 in x_lok]

        if iter == 0:
            ocena_x_glob = np.argmax(punkty_startowe_ocenione)
            x_glob = punkty_startowe[ocena_x_glob]

            min_ocena_x_glob = np.argmin(punkty_startowe_ocenione)
            min_x_glob = punkty_startowe[min_ocena_x_glob]

            print(f'iteracja: {iter}\n'
                  f'Położenie najlepszego punktu: {float(x_glob[0]), float(x_glob[1])}\n'
                  f'Położenie najgorszego punktu: {float(min_x_glob[0]), float(min_x_glob[1])}')

            x = [x_values[0] for x_values in punkty_startowe]
            y = [y_values[1] for y_values in punkty_startowe]

            plot()
            plt.scatter(x, y, color='blue')
            plt.scatter(x_glob[0], x_glob[1], color='green')
            plt.scatter(min_x_glob[0], min_x_glob[1], color='red')

            plt.show()

        else:
            ocena_x_glob = np.argmax(punkty_startowe_ocenione)
            min_ocena_x_glob = np.argmin(punkty_startowe_ocenione)

            if x_glob < punkty_startowe[ocena_x_glob]:
                x_glob = punkty_startowe[ocena_x_glob]

            if min_x_glob > punkty_startowe[min_ocena_x_glob]:
                min_x_glob = punkty_startowe[min_ocena_x_glob]

        for j in range(0, len(punkty_startowe)):
            if x_lok_ocenione < punkty_startowe_ocenione:
                x_lok[j]= punkty_startowe[j]

        for j in range(0, len(punkty_startowe)):
            rnd_glob = random.uniform(0, 1)
            rnd_lok = random.uniform(0, 1)

            for i in range(0, len(punkty_startowe[j])):
                V_2d[j][i] = V_2d[j][i] * r_inercji + (x_glob[i] - punkty_startowe[j][i]) * r_glob * rnd_glob + (x_lok[j][i] - punkty_startowe[j][i]) * r_lok * rnd_lok
                punkty_startowe[j][i] += V_2d[j][i]
                if punkty_startowe[j][i] < 0:
                    punkty_startowe[j][i] = 0
                elif punkty_startowe[j][i] > 100:
                    punkty_startowe[j][i] = 100

        for j in iterations:
            if iter == j:
                x = [x_values[0] for x_values in punkty_startowe]
                y = [y_values[1] for y_values in punkty_startowe]

                print(f'iteracja: {iter}\n'
                      f'Położenie najlepszego punktu: {float(x_glob[0]), float(x_glob[1])}\n'
                      f'Położenie najgorszego punktu: {float(min_x_glob[0]), float(min_x_glob[1])}')

                plot()
                plt.scatter(x, y, color='blue')
                plt.scatter(min_x_glob[0], min_x_glob[1], color='red')
                plt.scatter(x_glob[0], x_glob[1], color='green')

                plt.show()
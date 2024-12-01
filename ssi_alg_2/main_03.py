import random
import numpy as np
import matplotlib.pyplot as plt


def main():
    x = random.randint(15, 36)
    y = np.sin(x / 10.0) * np.sin(x / 200.0)

    x_wyznaczone_punkty = []
    y_wyznaczone_punkty = []

    # zakres_zm = [i for i in range(0, 101)]

    rozrzut = 5
    l_iteracji = 100
    wsp_przyrostu = 1.1

    for i in range(l_iteracji):
        x_pot = x + random.uniform(-rozrzut, rozrzut)
        if x_pot > 100:
            x_pot = 100
        elif x_pot < 0:
            x_pot = 0

        y_pot = np.sin(x_pot / 10.0) * np.sin(x_pot / 200.0)

        if y_pot >= y:
            x = x_pot
            y = y_pot
            rozrzut += wsp_przyrostu
        else:
            rozrzut /= wsp_przyrostu

        if i == 0 or i == 20:
            print(f'iteracja: {i}, x = {x}, y = {y}')
            x_wyznaczone_punkty.append(x)
            y_wyznaczone_punkty.append(y)

        x_axis = np.linspace(0, 100, 100)
        y_axis = np.sin(x_axis / 10.0) * np.sin(x_axis / 200.0)

        plt.scatter(x_wyznaczone_punkty, y_wyznaczone_punkty, color='green')
        plt.plot(x_axis, y_axis, color='blue', linewidth=0.5)

    plt.show()
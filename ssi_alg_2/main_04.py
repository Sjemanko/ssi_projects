import random
import numpy as np
import matplotlib.pyplot as plt


def main():
    # ZMIANA PRZEDZIAŁU
    x = random.randint(55, 66)
    y = np.sin(x / 10.0) * np.sin(x / 200.0)

    x_wyznaczone_punkty = []
    y_wyznaczone_punkty = []

    # zakres_zm = [i for i in range(0, 101)]

    # ZMIANA PARAMETRÓW
    rozrzut = 2
    l_iteracji = 100
    wsp_przyrostu = 1.3

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

        if i == 0 or i == 4 or i == 9 or i == 14:
            print(f'iteracja: {i + 1}, x = {x}, y = {y}, rozrzut = {rozrzut}')
            x_wyznaczone_punkty.append(x)
            y_wyznaczone_punkty.append(y)

        x_axis = np.linspace(0, 100, 100)
        y_axis = np.sin(x_axis / 10.0) * np.sin(x_axis / 200.0)

        plt.scatter(x_wyznaczone_punkty, y_wyznaczone_punkty, color='green')
        plt.plot(x_axis, y_axis, color='blue', linewidth=0.5)

    plt.show()

import numpy as np
import math


def manhattan(point1, point2):
    return np.abs(point1[0] - point2[0]) + np.abs(point1[1] - point2[1])


def czebyszew(point1, point2):
    return max(abs(point1[0] - point2[0]), abs(point1[1] - point2[1]))


def euclidean(point1, point2):
    return np.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def miara_niepodobienstwa(BA, BB, dist_func):
    miara_calosc = 0
    for i in range(BA.shape[0]):
        for j in range(BA.shape[1]):
            if BA[i][j] == 1:
                odl_min = np.inf
                for k in range(BB.shape[0]):
                    for l in range(BB.shape[1]):
                        if BB[k][l] == 1:
                            odl_akt = dist_func([i, j], [k, l])
                            odl_min = min(odl_min, odl_akt)
                miara_calosc += odl_min
    return miara_calosc


def miara_podobienstwa_obustronnego(BA, BB, dist_func):
    return -(miara_niepodobienstwa(BA, BB, dist_func) + miara_niepodobienstwa(BB, BA, dist_func))


def main(BA, BB, dist_func):
    miara_podob_obustr = miara_podobienstwa_obustronnego(BA, BB, dist_func)
    return miara_podob_obustr


wzorzec1 = np.array([[0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 0, 1], [0, 0, 0, 1], [0, 0, 0, 1]])
wzorzec2 = np.array([[0, 1, 1, 1], [1, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]])
wzorzec3 = np.array([[1, 1, 1, 0], [0, 0, 0, 1], [1, 1, 1, 1], [0, 0, 0, 1], [1, 1, 1, 0]])

test1 = np.array([[0, 0, 0, 0], [0, 0, 1, 1], [0, 1, 1, 1], [0, 0, 0, 1], [0, 0, 0, 1]])
test2 = np.array([[1, 1, 1, 1], [0, 0, 0, 1], [1, 1, 1, 1], [0, 0, 1, 1], [1, 1, 1, 1]])
test3 = np.array([[1, 1, 1, 1], [0, 0, 0, 1], [0, 0, 1, 0], [1, 1, 0, 0], [1, 1, 1, 1]])

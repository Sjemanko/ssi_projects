import re
import math
import random


def read_data(filename: str) -> dict:
    """
    read data file,
    remove redundant spaces,
    save data into dictionary -> dict: {index: int [a_value: float, b_value: float], ...}
    """
    point_values_dict = {}
    with open(filename) as data:
        for idx, line in enumerate(data):
            [a, b] = re.sub(' +', ' ', line).rstrip().split()
            point_values_dict.update({idx: [float(a), float(b)]})
    return point_values_dict


def euclidean_distance(a: list, b: list) -> float:
    """
    Calculate Euclidean distance between two points in 2d.
    :param a: a_point
    :param b: b_point
    :return: Euclidean distance between points
    """
    return math.sqrt(((b[0] - a[0]) ** 2) + ((b[1] - a[1]) ** 2))


def find_random_middles(number_of_groups: int, data: dict) -> dict:
    """
    Find random middles in data dict by randomizing indexes in data dict and get their value
    :param number_of_groups: how many groups algorithm will take to split data into groups
    :param data: dictionary with points positions
    :return: dictionary with number of random points equal to number of groups
    """
    random_middles = {}
    for i in range(number_of_groups):
        random_middles.update({i: list(data.get(random.choice(list(data.keys()))))})
    return random_middles

def get_defined_middles(data: dict) -> dict:
    defined_middles = {}
    defined_middles.update({0: data.get(0), 1: data.get(1), 2: data.get(2)})
    return defined_middles
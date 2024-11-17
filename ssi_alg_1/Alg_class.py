import re
import math
import random

from ssi_alg_1.Strategy import Strategy

class Algorithm:

    def __init__(self, data_file_path: str, count_distance_method: Strategy):
        self._data_file_path = data_file_path
        self._count_distance_method_strategy = count_distance_method
        self.data = self.read_data()

    @property
    def count_distance_method_strategy(self):
        return self._count_distance_method_strategy

    @count_distance_method_strategy.setter
    def count_distance_method_strategy(self, strategy: Strategy):
        self._count_distance_method_strategy = strategy

    def read_data(self) -> dict:
        point_values_dict = {}
        with open(self._data_file_path) as data:
            for idx, line in enumerate(data):
                [a, b] = re.sub(' +', ' ', line).rstrip().split()
                point_values_dict.update({idx: [float(a), float(b)]})
        return point_values_dict

    def find_random_middle_points(self, number_of_groups: int) -> dict:
        random_middles = {}
        for i in range(number_of_groups):
            random_middles.update({i: list(self.data.get(random.choice(list(self.data.keys()))))})
        return random_middles

    def get_defined_middle_points(self) -> dict:
        defined_middles = {}
        data = self.read_data()
        defined_middles.update({0: [-1.5638, 1.0163], 1: [-1.7208, 0.2806], 2: [-1.681, 0.476]})
        return defined_middles
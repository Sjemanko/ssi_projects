import re
import random

import numpy as np

from Strategy import Strategy

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
        """
        Read data from file and return it in specific format
        :return dict[int, list[float(x), float(y)]]:
        """
        point_values_dict = {}
        with open(self._data_file_path) as data:
            for idx, line in enumerate(data):
                [a, b] = re.sub(' +', ' ', line).rstrip().split()
                point_values_dict.update({idx: [float(a), float(b)]})
        return point_values_dict

    def find_random_middle_points(self, number_of_groups: int) -> dict:
        f"""
        Return {number_of_groups} points chosen from given dataset. Data is from read_data function.
        :param number_of_groups: int
        :return dict[int, list[float(x), float(y)]:
        """
        random_middles = {}
        for i in range(number_of_groups):
            random_middles.update({i: list(self.data.get(random.choice(list(self.data.keys()))))})
        return random_middles

    def get_defined_middle_points(self) -> dict:
        """
        Return defined middle points
        :return dict[int, list[float(x), float(y)]:
        """
        defined_middles = {}
        data = self.read_data()
        defined_middles.update({0: [-1.5638, 1.0163], 1: [-1.7208, 0.2806], 2: [-1.681, 0.476]})
        return defined_middles

    def count_distances_and_create_points_groups(self, points_positions, middles_points):
        """
        Return point and the group which every point belongs to (calculated before in count_distance_method_strategy)
        :param points_positions: dict[int, list[float(x), float(y)]]
        :param middles_points: dict[int, list[float(x), float(y)]]
        :return list[tuple[int, int]]:
        """
        group_indexes = []
        for s_index, point in enumerate(points_positions.values()):
            distances = [self.count_distance_method_strategy.count_distance(point, middle) for middle in
                         middles_points.values()]
            closest_group_idx = np.argmin(distances)
            group_indexes.append((s_index, closest_group_idx))
        return group_indexes

    def count_middle_points_position(self, middles_points, group_points, points_positions):
        """
        Update middle points positions based on new group indexes and points positions
        :param middles_points: dict[int, list[float(x), float(y)]
        :param group_points: list[tuple[int, int]
        :param points_positions: dict[int, list[float(x), float(y)]
        :return:
        """
        for j_index, group_point_values in enumerate(middles_points.values()):
            Xgr = []
            x_pos = 0
            y_pos = 0

            # adding points to group based on index
            for group in group_points:
                if j_index == group[1]:
                    Xgr.append(group[0])
            if len(Xgr) == 0:
                break

            # sum all x,y points values
            for el in Xgr:
                x_pos += points_positions.get(el)[0]
                y_pos += points_positions.get(el)[1]

            # count average values for middle points
            x_pos /= len(Xgr)
            y_pos /= len(Xgr)

            middles_points.update({j_index: [x_pos, y_pos]})
        return middles_points

    def return_closest_point_to_middle(self, middles_points, group_points, points_positions):
        """
        Method for fining the closest points to counted middles point
        :param middles_points: dict[int, list[float(x), float(y)]
        :param group_points: list[tuple[int, int]
        :param points_positions: dict[int, list[float(x), float(y)]
        :return:
        """
        for j_index, group_point_values in enumerate(middles_points.values()):
            Xgr = []
            x_pos = 0
            y_pos = 0
            distances = {}

            # adding points to group based on index
            for group in group_points:
                if j_index == group[1]:
                    Xgr.append(group[0])
            if len(Xgr) == 0:
                break

            # sum all x,y points values
            for el in Xgr:
                x_pos += points_positions.get(el)[0]
                y_pos += points_positions.get(el)[1]

            # count average values for middle points
            x_pos /= len(Xgr)
            y_pos /= len(Xgr)

            for el in Xgr:
                point_dist = self.count_distance_method_strategy.count_distance([x_pos, y_pos], [points_positions.get(el)[0], points_positions.get(el)[1]], )
                distances[el] = point_dist

            min_index = min(distances, key=distances.get)

            middles_points.update({j_index: [points_positions.get(min_index)[0], points_positions.get(min_index)[1]]})
        return middles_points
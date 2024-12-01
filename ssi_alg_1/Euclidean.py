from Strategy import Strategy
import math

class Euclidean(Strategy):

    def count_distance(self, a_points: list, b_points: list) -> float:
        return math.sqrt(((b_points[0] - a_points[0]) ** 2) + ((b_points[1] - a_points[1]) ** 2))

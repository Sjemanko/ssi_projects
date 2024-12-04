from Strategy import Strategy

class DistOfOnlyX2Param(Strategy):

    def count_distance(self, a_points: list, b_points: list):
        return abs(a_points[1] - b_points[1])
from Strategy import Strategy


class DistOfOnlyX1Param(Strategy):

    def count_distance(self, a_points: list, b_points: list):
        return abs(a_points[0] - b_points[0])

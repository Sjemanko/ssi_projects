from abc import ABC, abstractmethod

class Strategy(ABC):

    @abstractmethod
    def count_distance(self, x_points: list, y_points: list):
        pass

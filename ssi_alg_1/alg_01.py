import matplotlib.pyplot as plt
import matplotlib.markers as markers
import numpy as np

from ssi_alg_1.Euclidean import Euclidean
from ssi_alg_1.Manhattan import Manhattan
from ssi_alg_1.Alg_class import Algorithm

marker = markers.MarkerStyle(marker='s', fillstyle='none')
iterations = 40

# colors defined for groups
groups = 3
colors = ['red', 'green', 'yellow']

# flag for break loop after find middle points copy (when middle_points cords are the same, loops break)
optimized = True

Alg_obj = Algorithm('data.txt', Euclidean())

points_positions = Alg_obj.data

middles_groups = Alg_obj.find_random_middle_points(groups)
print(middles_groups)

# middles_groups = Alg_obj.get_defined_middle_points()

# memory
prev_middles = {}

x_values, y_values = zip(*points_positions.values())

for i in range(iterations):
    group_indexes = []
    for s, point in enumerate(points_positions.values()):
        distances = [Alg_obj.count_distance_method_strategy.count_distance(point, middle) for middle in middles_groups.values()]
        closest_group_idx = np.argmin(distances)
        group_indexes.append((s, closest_group_idx))

    for j, group_point_values in enumerate(middles_groups.values()):
        temp = []
        xpos = 0
        ypos = 0
        for group in group_indexes:
            if j == group[1]:
                temp.append(group[0])
        if len(temp) == 0:
            break
        for el in temp:
            xpos += points_positions.get(el)[0]
            ypos += points_positions.get(el)[1]
        xpos /= len(temp)
        ypos /= len(temp)

        middles_groups.update({j: [xpos, ypos]})

    if optimized:
        if prev_middles.get(0) == middles_groups.get(0) and prev_middles.get(1) == middles_groups.get(
                1) and prev_middles.get(2) == middles_groups.get(2):
            break
        else:
            prev_middles = middles_groups.copy()

    x_middle_values, y_middle_values = zip(*middles_groups.values())

    x_middle_values = list(x_middle_values)
    y_middle_values = list(y_middle_values)

    for s, (x, y) in enumerate(zip(x_values, y_values)):
        group_idx = next(group[1] for group in group_indexes if group[0] == s)
        plt.scatter(x, y, color=colors[group_idx], marker=marker)

    # print(i, middles_groups)
    # plt.scatter(x_values, y_values, marker=marker)
    plt.scatter(x_middle_values, y_middle_values, marker='o')
    plt.show()


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.markers as markers

from functions import read_data, euclidean_distance, find_random_middles
from ssi_alg_1.functions import get_defined_middles

marker = markers.MarkerStyle(marker='s', fillstyle='none')

# flag for break loop after find middle points copy (when middle_points cords are the same, loops break)
optimized = True

groups = 4

# colors defined for groups
colors = ['red', 'green', 'yellow', 'purple']

iterations = 100

# memory
prev_middles = {}

points_values = read_data('data.txt')

# random middles cords
middles_groups = find_random_middles(groups, points_values)

# defined middles cords
# middles_groups = get_defined_middles(points_values)

x_values, y_values = zip(*points_values.values())

x_values = list(x_values)
y_values = list(y_values)

for i in range(iterations):
    group_indexes = []
    for s, point in enumerate(points_values.values()):
        distances = []
        for middle_idx, middle in enumerate(middles_groups.values()):
            distances.append(euclidean_distance(point, middle))
        closest_group_idx = distances.index(min(distances))
        group_indexes.append([s, closest_group_idx])

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
            xpos += points_values.get(el)[0]
            ypos += points_values.get(el)[1]
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

    print(i, middles_groups)
    # plt.scatter(x_values, y_values, marker=marker)
    plt.scatter(x_middle_values, y_middle_values, marker='o')
    plt.show()


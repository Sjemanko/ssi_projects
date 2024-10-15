import numpy as np
import matplotlib.pyplot as plt
import matplotlib.markers as markers

from functions import read_data, euclidean_distance, find_random_middles

x_values = []
y_values = []

x_middle_values = []
y_middle_values = []

groups = 1
iterations = 100

group_indexes = []
split_groups = []


points_values = read_data('data.txt')
marker = markers.MarkerStyle(marker='s', fillstyle='none')

middles_groups = find_random_middles(groups, points_values)

for point_values in points_values.values():
    x_values.append(point_values[0])
    y_values.append(point_values[1])

for i in range(iterations):
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

    for middle_values in middles_groups.values():
        x_middle_values.append(middle_values[0])
        y_middle_values.append(middle_values[1])

    plt.scatter(x_values, y_values, marker=marker)
    plt.scatter(x_middle_values, y_middle_values, marker='o')
    plt.show()

    print(middles_groups)
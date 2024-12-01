import matplotlib.pyplot as plt
import matplotlib.markers as markers
from Alg_class import Algorithm

def main(iterations, groups, colors, Alg_strat, mode='means'):
    marker = markers.MarkerStyle(marker='s', fillstyle='none')

    Alg_obj = Algorithm('data.txt', Alg_strat)

    points_positions = Alg_obj.data

    # dict[int, list[float(x), float(y)]
    middles_points = Alg_obj.find_random_middle_points(groups)

    # middles_points = Alg_obj.get_defined_middle_points()

    for i in range(iterations):

        # index of point and group which it belongs -> list[tuple[index, group_index]]
        group_points = Alg_obj.count_distances_and_create_points_groups(points_positions, middles_points)

        if i > 0:
            # count new positions for middle points
            if mode == 'means':
                middles_points = Alg_obj.count_middle_points_position(middles_points, group_points, points_positions)
            else:
                middles_points = Alg_obj.return_closest_point_to_middle(middles_points, group_points, points_positions)

        x_middle_values, y_middle_values = zip(*middles_points.values())
        x_middle_values = list(x_middle_values)
        y_middle_values = list(y_middle_values)

        group_points_number = {i:0 for i in range(groups)}
        groups_x_values = {i:[] for i in range(groups)}
        groups_y_values = {i:[] for i in range(groups)}

        # plotting and printing data
        for s_index, (x, y) in enumerate(points_positions.values()):
            # choosing group index from group point values [index, group_index] and save it to group_idx
            group_idx = next(group[1] for group in group_points if group[0] == s_index)
            group_points_number[group_idx] += 1

            groups_x_values.get(group_idx).append(x)
            groups_y_values.get(group_idx).append(y)

            plt.scatter(x, y, color=colors[group_idx], marker=marker)

        # iterations
        if i == 0 or i == 3 or i == 9:

            print(f'\niterations: {i + 1}\n')
            for j, point in enumerate(middles_points.values()):
                print(f'middle point {j+1}: [{round(point[0], 4)}; {round(point[1], 4)}]:'
                      f' \n-> number of points in group: {j+1}: {group_points_number[j]}',
                      f' \n-> min values in group {j+1}: (x: {min(groups_x_values.get(j))}, y: {min(groups_y_values.get(j))})'
                      f' \n-> max values in group {j+1}: (x: {max(groups_x_values.get(j))}, y: {max(groups_y_values.get(j))})\n'
                      )
            plt.scatter(x_middle_values, y_middle_values, marker='o', color="black")
            plt.show()
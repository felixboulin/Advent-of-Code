import numpy as np
from functools import reduce


def main():

    with open('input.txt') as f:
        data = f.read().splitlines()

    data = [list(x) for x in data]
    data = [[int(x) for x in y] for y in data]
    data = np.array(data)
    target = data[1:-1, 1:-1]

    max_view_size = 0

    for i in range(len(target)):
        for j in range(len(target[i])):
            target_row_left = data[i+1, :j+1]
            target_row_right = data[i+1, j+2:]
            target_col_top = data[:i+1, j+1]
            target_col_bottom = data[i+2:, j+1]

            view_size_four_sides = []

            view_size_four_sides.append(evaluateView(
                np.flip(target_row_left), target[i][j]))
            view_size_four_sides.append(
                evaluateView(target_row_right, target[i][j]))
            view_size_four_sides.append(evaluateView(
                np.flip(target_col_top), target[i][j]))
            view_size_four_sides.append(
                evaluateView(target_col_bottom, target[i][j]))

            view_size = reduce(lambda x, y: x * y, view_size_four_sides)

            if view_size > max_view_size:
                max_view_size = view_size

    print('Max view size is: ', max_view_size)


def evaluateView(array, target):
    view_size = 0
    for element in array:
        view_size += 1
        if element >= target:
            break
    return view_size


if __name__ == "__main__":
    main()

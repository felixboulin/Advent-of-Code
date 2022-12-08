import numpy as np


def main():

    with open('input.txt') as f:
        data = f.read().splitlines()

    data = [list(x) for x in data]
    data = [[int(x) for x in y] for y in data]
    data = np.array(data)
    target = data[1:-1, 1:-1]

    # Initialise visible tree count with the number of trees on the edges
    visible_tree_count = (np.size(data, 0) + np.size(data, 1)) * 2 - 4

    for i in range(len(target)):
        for j in range(len(target[i])):
            target_row_left = data[i+1, :j+1]
            target_row_right = data[i+1, j+2:]
            target_col_top = data[:i+1, j+1]
            target_col_bottom = data[i+2:, j+1]

            if target[i][j] > max(target_row_left) or target[i][j] > max(target_row_right)\
                    or target[i][j] > max(target_col_top) or target[i][j] > max(target_col_bottom):
                visible_tree_count += 1

    print('Total number of visible trees is: ', visible_tree_count)


if __name__ == "__main__":
    main()

def main():

    with open('input.txt') as f:
        data = f.read().splitlines()

    # initialise visited positions as an empty set
    count_visited = set()
    count_visited.add('0,0')

    rope = [{'x': 0, 'y': 0} for i in range(10)]

    for element in data:

        for i in range(int(element[1:])):
            if element[0] == 'U':
                rope[0]['y'] += 1
            elif element[0] == 'D':
                rope[0]['y'] -= 1
            elif element[0] == 'L':
                rope[0]['x'] -= 1
            elif element[0] == 'R':
                rope[0]['x'] += 1

            for j in range(1, len(rope)):
                x_gap = rope[j-1]['x'] - rope[j]['x']
                y_gap = rope[j-1]['y'] - rope[j]['y']

                if x_gap == 0 and y_gap == 2:
                    rope[j]['y'] += 1

                elif x_gap == 0 and y_gap == -2:
                    rope[j]['y'] -= 1

                elif x_gap == 1 and y_gap == 2:
                    rope[j]['x'] += 1
                    rope[j]['y'] += 1

                elif x_gap == 1 and y_gap == -2:
                    rope[j]['x'] += 1
                    rope[j]['y'] -= 1

                elif x_gap == -1 and y_gap == -2:
                    rope[j]['x'] -= 1
                    rope[j]['y'] -= 1

                elif x_gap == -1 and y_gap == 2:
                    rope[j]['x'] -= 1
                    rope[j]['y'] += 1

                elif x_gap == 2 and y_gap == 1:
                    rope[j]['x'] += 1
                    rope[j]['y'] += 1

                elif x_gap == 2 and y_gap == 0:
                    rope[j]['x'] += 1

                elif x_gap == 2 and y_gap == -1:
                    rope[j]['x'] += 1
                    rope[j]['y'] -= 1

                elif x_gap == -2 and y_gap == -1:
                    rope[j]['x'] -= 1
                    rope[j]['y'] -= 1

                elif x_gap == -2 and y_gap == 0:
                    rope[j]['x'] -= 1

                elif x_gap == -2 and y_gap == 1:
                    rope[j]['x'] -= 1
                    rope[j]['y'] += 1

                elif x_gap == 2 and y_gap == -2:
                    rope[j]['x'] += 1
                    rope[j]['y'] -= 1

                elif x_gap == -2 and y_gap == 2:
                    rope[j]['x'] -= 1
                    rope[j]['y'] += 1

                elif x_gap == 2 and y_gap == 2:
                    rope[j]['x'] += 1
                    rope[j]['y'] += 1

                elif x_gap == -2 and y_gap == -2:
                    rope[j]['x'] -= 1
                    rope[j]['y'] -= 1

                elif j < len(rope):
                    break

                if j == len(rope) - 1:
                    count_visited.add(f"{rope[j]['x']},{rope[j]['y']}")

    print('The number of positions that the tail visited at least once are: ', len(
        count_visited))

if __name__ == "__main__":
    main()

def main():

    with open('input.txt') as f:
        data = f.read().splitlines()

    p_head = {
        'x': 0,
        'y': 0
    }

    p_tail = {
        'x': 0,
        'y': 0
    }

    # initialise visited positions as an empty set
    count_visited = set()
    count_visited.add('0,0')

    for element in data:

        if element[0] == 'U':
            for i in range(int(element[1:])):
                p_head['y'] += 1
                if checkIfTailMoves(p_head, p_tail):
                    p_tail['x'] = p_head['x']
                    p_tail['y'] = p_head['y'] - 1
                    count_visited.add(
                        str(p_tail['x']) + ',' + str(p_tail['y']))

        elif element[0] == 'D':
            for i in range(int(element[1:])):
                p_head['y'] -= 1
                if checkIfTailMoves(p_head, p_tail):
                    p_tail['x'] = p_head['x']
                    p_tail['y'] = p_head['y'] + 1
                    count_visited.add(
                        str(p_tail['x']) + ',' + str(p_tail['y']))

        elif element[0] == 'L':
            for i in range(int(element[1:])):
                p_head['x'] -= 1
                if checkIfTailMoves(p_head, p_tail):
                    p_tail['x'] = p_head['x'] + 1
                    p_tail['y'] = p_head['y']
                    count_visited.add(
                        str(p_tail['x']) + ',' + str(p_tail['y']))

        elif element[0] == 'R':
            for i in range(int(element[1:])):
                p_head['x'] += 1
                if checkIfTailMoves(p_head, p_tail):
                    p_tail['x'] = p_head['x'] - 1
                    p_tail['y'] = p_head['y']
                    count_visited.add(
                        str(p_tail['x']) + ',' + str(p_tail['y']))

    print('The number of positions that the tail visited at least once are: ', len(
        count_visited))


def checkIfTailMoves(p_head, p_tail):
    if abs(p_head['y'] - p_tail['y']) > 1 or abs(p_head['x'] - p_tail['x']) > 1:
        return True
    else:
        return False


if __name__ == "__main__":
    main()

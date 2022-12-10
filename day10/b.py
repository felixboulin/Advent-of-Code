def main():

    with open('input.txt') as f:
        data = f.read().splitlines()

    X = 1
    count_cycles = 0
    screen = ""
    for instruction in data:
        if instruction[:4] == 'addx':
            for _ in range(2):
                screen += printPixel(count_cycles, X)
                count_cycles += 1
            X += int(instruction[5:])
        elif instruction[:4] == 'noop':
            screen += printPixel(count_cycles, X)
            count_cycles += 1

    print(screen)


def printPixel(count_cycles, X):
    if count_cycles + 1 in [40, 80, 120, 160, 200, 240]:
        return ".\n"
    else:
        if count_cycles % 40 in [X-1, X, X+1]:
            return "#"
        else:
            return "."


if __name__ == "__main__":
    main()

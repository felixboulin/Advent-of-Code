def main():

    with open('input.txt') as f:
        data = f.read().splitlines()

    X = 1
    count_cycles = 0

    cycles_of_interest = [20, 60, 100, 140, 180, 220]
    signal_strength = 0

    for instruction in data:
        if instruction[:4] == 'addx':
            for _ in range(2):
                count_cycles += 1
                if count_cycles in cycles_of_interest:
                    signal_strength += X * count_cycles
            X += int(instruction[5:])
        elif instruction[:4] == 'noop':
            count_cycles += 1
            if count_cycles in cycles_of_interest:
                signal_strength += X * count_cycles

    print(f"final signal strneght = {signal_strength}")


if __name__ == "__main__":
    main()

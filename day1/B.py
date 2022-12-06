with open("input.txt") as f:
    data = f.read().splitlines()

    max_cals = [0, 0, 0]
    cal = 0
    for e in range(len(data)):
        if data[e] == "":
            if cal > max_cals[0]:
                max_cals[0] = cal
                max_cals.sort()
            cal = 0

        elif e == len(data) - 1:
            cal += int(data[e])
            if cal > max_cals[0]:
                max_cals[0] = cal
                max_cals.sort()

        else:
            cal += int(data[e])

    print("Max calories: ", sum(max_cals))

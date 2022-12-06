with open("input.txt") as f:
    data = f.read().splitlines()
    max_cal = 0
    cal = 0

    for e in data:
        if e == "":
            if cal > max_cal:
                max_cal = cal
            cal = 0
        else:
            cal += int(e)

    print("Max calories: ", max_cal)

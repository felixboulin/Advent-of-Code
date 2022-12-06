with open("input.txt") as f:
    data = f.read().splitlines()
    # print(data)
    elf_no = 1
    best_elf = 1
    max_cal = 0
    cal = 0
    for e in data:
        # print("Elf: ", elf_no)
        if e == "":
            if cal > max_cal:
                max_cal = cal
                best_elf = elf_no
            cal = 0
            elf_no += 1
        else:
            cal += int(e)
            # print("Calories: ", cal)

    print("Best elf is: ", best_elf)
    print("Max calories: ", max_cal)

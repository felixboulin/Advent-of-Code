def main():

    with open('input.txt') as f:
        data = f.read().splitlines()
        totalPrio = 0
        for rucksack in data:
            comp1 = rucksack[0:(len(rucksack)//2)]
            comp2 = rucksack[(len(rucksack)//2):]

            for letter in comp1:
                if letter in comp2:
                    item_type = letter
                    break

            totalPrio += getPrio(item_type)

    print('totalPrio: ', totalPrio)


def getPrio(charInput):
    val = ord(charInput)
    if charInput.isupper():
        return val - 65 + 1 + 26
    elif charInput.islower():
        return val - 97 + 1
    else:
        return 1


if __name__ == "__main__":
    main()

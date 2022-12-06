def main():

    with open('input.txt') as f:
        data = f.read().splitlines()
        totalPrio = 0
        for rucksack in data:
            comp1 = rucksack[0:(len(rucksack)//2)]
            comp2 = rucksack[(len(rucksack)//2):]
            # print('comp1: ', comp1)
            # print('comp2: ', comp2)

            for letter in comp1:
                if letter in comp2:
                    item_type = letter
                    break

            # print('item_type: ', item_type)
            totalPrio += getPrio(item_type)

    print('totalPrio: ', totalPrio)


def getPrio(charInput):
    val = ord(charInput)
    if charInput.isupper():
        return val - 65 + 1 + 26
    elif charInput.islower():
        return val - 97 + 1
    else:
        print('incorrect input')
    pass


if __name__ == "__main__":
    main()

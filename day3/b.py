def main():

    with open('input.txt') as f:
        data = f.read().splitlines()
        totalPrio = 0
        i = 0
        while i < len(data):
            for letter in data[i]:
                if letter in data[i+1] and letter in data[i+2]:
                    # print('letter: ', letter)
                    item_type = letter
                    break
            # print('item_type: ', item_type)
            totalPrio += getPrio(item_type)
            i += 3
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

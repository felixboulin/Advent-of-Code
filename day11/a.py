def main():

    with open('input.txt') as f:
        data = f.read().split('Monkey ')

    monkeys = []

    for e in data:
        elist = e.splitlines()
        if elist != []:
            starting_items = getItems(elist)
            operation = getOperation(elist)
            divi_check = getDiviCheck(elist)
            monkey = [starting_items, operation, divi_check]
            monkeys.append(monkey)

    inspection_counts = [0 for _ in range(len(monkeys))]

    for i in range(20):
        for monkey in monkeys:
            for item in monkey[0]:
                inspection_counts[monkeys.index(monkey)] += 1
                worry_level = monkey[1](item)
                to_monkey = monkey[2](worry_level)
                monkeys[to_monkey][0].append(worry_level)
            monkey[0] = []

    inspection_counts.sort(reverse=True)
    monkey_business = inspection_counts[0] * inspection_counts[1]
    print(monkey_business)


def getDiviCheck(elist):
    divi_check = int(elist[3].split('Test: divisible by ')[1])
    dir_true = int(elist[4].split('If true: throw to monkey ')[1])
    dir_false = int(elist[5].split('If false: throw to monkey ')[1])

    def divi_func(x):
        if x % divi_check == 0:
            return dir_true
        else:
            return dir_false
    return divi_func


def getItems(elist):
    starting_items = elist[1].split(':')[1].split(',')
    starting_items = [int(x) for x in starting_items]
    return starting_items


def getOperation(elist):
    operation = elist[2].split('old ')[1]
    try:
        amount = int(operation[2:])
    except:
        amount = False

    if operation[0] == '*' and amount:
        def multiplication(x):
            return int((x * amount) / 3 // 1)
        return multiplication
    elif operation[0] == '*':
        def multiplication(x):
            return int((x * x) / 3 // 1)
        return multiplication
    elif operation[0] == '+' and amount:
        def addition(x):
            return int((x + amount) / 3 // 1)
        return addition
    elif operation[0] == '+':
        def addition(x):
            return int((x + x) / 3 // 1)
        return addition


if __name__ == "__main__":
    main()

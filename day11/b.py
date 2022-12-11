def main():

    with open('input.txt') as f:
        data = f.read().split('Monkey ')

    monkeys = []

    divisors = [5, 7, 13, 11, 3, 2, 17, 19]
    lcm = 1
    for e in divisors:
        lcm *= e

    for e in data:
        elist = e.splitlines()
        if elist != []:
            starting_items = getItems(elist)
            operation = getOperation(elist)
            to_mondey = getDiviCheck(elist)
            worry_cap = getWorryCap(elist)
            monkey = [starting_items, operation, to_mondey, worry_cap]
            monkeys.append(monkey)

    inspection_counts = [0 for _ in range(len(monkeys))]

    for i in range(10000):
        for monkey in monkeys:
            for item in monkey[0]:
                inspection_counts[monkeys.index(monkey)] += 1
                worry_level = monkey[1](item)
                to_monkey = monkey[2](worry_level)
                monkeys[to_monkey][0].append(
                    worry_level % lcm)
            monkey[0] = []

    inspection_counts.sort(reverse=True)
    print(inspection_counts)
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


def getWorryCap(elist):
    divi_check = int(elist[3].split('Test: divisible by ')[1])

    def worry_cap(x):
        if x % divi_check == 0:
            return divi_check
        else:
            return 1
    return worry_cap


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
            return (x * amount)
        return multiplication
    elif operation[0] == '*':
        def multiplication(x):
            return (x * x)
        return multiplication
    elif operation[0] == '+' and amount:
        def addition(x):
            return (x + amount)
        return addition
    elif operation[0] == '+':
        def addition(x):
            return (x + x)
        return addition


if __name__ == "__main__":
    main()

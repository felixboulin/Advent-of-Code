import re


def main():

    with open('input.txt') as f:
        data = f.read().splitlines()
        breakPoint = data.index('')
        config = data[0:breakPoint]
        nb_stacks = int((len(config[0])+1) / 4)
        stacks = []

        for i in range(nb_stacks):
            position = 1 + i * 4
            stacks.append(list(filter(getStackItems, [c[position]
                                                      for c in config[0:len(config)-1]])))
            stacks[i].reverse()

        instructions = data[breakPoint+1:]

        for instruction in instructions:
            instList = re.findall(r'\d+', instruction)
            nb_items = int(instList[0])
            from_stack = int(instList[1]) - 1
            to_stack = int(instList[2]) - 1

            if nb_items == 1:
                stacks[to_stack].append(stacks[from_stack].pop())
            else:
                stacks[to_stack].extend(stacks[from_stack][-nb_items:])
                stacks[from_stack] = stacks[from_stack][:-nb_items]

        print(''.join([stack[-1] for stack in stacks]))


def getStackItems(item):
    if item == ' ':
        return False
    else:
        return True


if __name__ == "__main__":
    main()

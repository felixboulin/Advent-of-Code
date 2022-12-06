def main():

    with open('input.txt') as f:
        data = f.read().splitlines()
        # print(data)
        count = 0
        for pair in data:
            p1 = pair.split(',')[0].split('-')
            p2 = pair.split(',')[1].split('-')

            print('p1: ', p1)
            print('p2: ', p2)

            r1 = range(int(p1[0]), int(p1[1])+1)
            # print('r1 ', [r for r in r1])
            r1l = [r for r in r1]
            r2 = range(int(p2[0]), int(p2[1])+1)
            # print('r2 ', [r for r in r2])
            r2l = [r for r in r2]

            cont = True
            for e in r1l:
                if e not in r2l:
                    break
                if e == r1l[-1] and e in r2l:
                    # print('r1l in r2l')
                    count += 1
                    cont = False

            if cont:
                for e in r2l:
                    if e not in r1l:
                        break
                    if e == r2l[-1] and e in r1l:
                        # print('r2l in r1l')
                        count += 1

        print('count: ', count)


if __name__ == "__main__":
    main()

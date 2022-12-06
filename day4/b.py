def main():

    with open('input.txt') as f:
        data = f.read().splitlines()
        count = 0
        for pair in data:
            p1 = pair.split(',')[0].split('-')
            p2 = pair.split(',')[1].split('-')

            r1 = range(int(p1[0]), int(p1[1])+1)
            r1l = [r for r in r1]
            r2 = range(int(p2[0]), int(p2[1])+1)
            r2l = [r for r in r2]

            for e in r1l:
                if e in r2l:
                    count += 1
                    break

        print('count: ', count)

if __name__ == "__main__":
    main()

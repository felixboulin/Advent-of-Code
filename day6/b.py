def main():

    with open('input.txt') as f:
        data = f.read().splitlines()[0]

        for i in range(len(data)-14):
            # print(i)
            if len(set(data[i:i+14])) == 14:
                print('1st market at', i+14)
                break


if __name__ == "__main__":
    main()

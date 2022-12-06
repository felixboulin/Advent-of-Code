def main():

    with open('input.txt') as f:
        data = f.read().splitlines()[0]

        for i in range(len(data)-4):
            if len(set(data[i:i+4])) == 4:
                print('1st market at', i+4)
                break


if __name__ == "__main__":
    main()

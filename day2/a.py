
def main():

    with open('input.txt') as f:
        data = f.read().splitlines()

        score = 0

        for battle in data:
            # get battle result core
            score += playBattle(battle)

            # add played move score
            if battle[2] == 'X':
                score += 1
            elif battle[2] == 'Y':
                score += 2
            elif battle[2] == 'Z':
                score += 3

        print('finale score: ', score)


def playBattle(battle_string):
    opponent_move = convertInput(battle_string[0])
    my_move = convertInput(battle_string[2])

    if opponent_move == my_move:
        return 3
    elif opponent_move == 'R' and my_move == 'S':
        return 0
    elif opponent_move == 'R' and my_move == 'P':
        return 6
    elif opponent_move == 'P' and my_move == 'R':
        return 0
    elif opponent_move == 'P' and my_move == 'S':
        return 6
    elif opponent_move == 'S' and my_move == 'P':
        return 0
    elif opponent_move == 'S' and my_move == 'R':
        return 6


def convertInput(input):
    if input == 'A' or input == 'X':
        return 'R'
    elif input == 'B' or input == 'Y':
        return 'P'
    elif input == 'C' or input == 'Z':
        return 'S'


if __name__ == "__main__":
    main()

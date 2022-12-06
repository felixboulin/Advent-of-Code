
def main():

    with open('input.txt') as f:
        data = f.read().splitlines()
        # print(data)

        score = 0

        for battle in data:
            if battle[2] == 'X':
                score += lose(battle[0])
            elif battle[2] == 'Y':
                score += draw(battle[0])
            elif battle[2] == 'Z':
                score += win(battle[0])

        print('finale score: ', score)


def lose(opponent_move):
    if opponent_move == 'A':
        # 0 for lose + 3 for scissors
        return 0 + 3
    elif opponent_move == 'B':
        # 0 for lose + 1 for rock
        return 0 + 1
    elif opponent_move == 'C':
        # 0 for lose + 2 for paper
        return 0 + 2


def win(opponent_move):
    if opponent_move == 'A':
        # 6 for win + 2 for paper
        return 6 + 2
    elif opponent_move == 'B':
        # 6 for win + 3 for scissors
        return 6 + 3
    elif opponent_move == 'C':
        # 6 for win + 1 for rock
        return 6 + 1


def draw(opponent_move):
    if opponent_move == 'A':
        # 3 for draw + 1 for rock
        return 3 + 1
    elif opponent_move == 'B':
        # 3 for draw + 2 for paper
        return 3 + 2
    elif opponent_move == 'C':
        # 3 for draw + 3 for scissors
        return 3 + 3


if __name__ == "__main__":
    main()

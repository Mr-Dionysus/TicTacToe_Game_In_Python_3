def player_side():
    p1 = -1
    while p1 != 'X' or p1 != 'O':
        p1 = input('P1, choose your side - X or O: ').upper()
        if p1 in ['x', 'X']:
            p2 = 'O'
            print('P1 - X, P2 - O')
            break
        elif p1 in ['o', 'O']:
            p2 = 'X'
            print('P1 - O, P2 - X')
            break
        else:
            print('Incorrect. Please, write X or O, P1')
    return {'P1': p1, 'P2': p2}


def game_board(boards):
    print(f'\n {boards[6]} | {boards[7]} | {boards[8]}\n---|---|---')
    print(f' {boards[3]} | {boards[4]} | {boards[5]}\n---|---|---')
    print(f' {boards[0]} | {boards[1]} | {boards[2]}\n')


def player_choice(boards):
    pick = -1
    variables_picks = []
    for item in boards:
        if item != 'X' and item != 'O':
            variables_picks.append(str(item))
    while pick not in boards:
        pick = input(f'Write a number from the list - {variables_picks}: ')
        if pick in variables_picks:
            return int(pick)
        else:
            print(f'Please, write a number from the list - {variables_picks}')


def player_turns(turns):
    if turns:
        return turns.pop(0)
    elif not turns:
        print('You two are lose!')
        return False


def player_references(boards, turns, sides, picks):
    if turns == 'P1':
        boards[picks - 1] = sides['P1']
    elif turns == 'P2':
        boards[picks - 1] = sides['P2']


def win_conditions(boards, turns):
    if boards[0] == boards[3] == boards[6] or boards[1] == boards[4] == boards[7] or boards[2] == boards[5] == boards[8] or boards[0] == boards[4] == boards[8] or boards[0] == boards[1] == boards[2] or boards[3] == boards[4] == boards[5] or boards[6] == boards[7] == boards[8] or boards[2] == boards[4] == boards[6]:
        print(f'{turns} you WIN!')
        return True
    else:
        return False


def tic_tac_toe():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    turn = ['P1', 'P2', 'P1', 'P2', 'P1', 'P2', 'P1', 'P2', 'P1']
    side = player_side()
    condition = True
    while condition:
        player_turn = player_turns(turn)
        game_board(board)
        print(f'{player_turn} - {side[player_turn]}')
        player_references(board, player_turn, side, player_choice(board))
        win = win_conditions(board, player_turn)
        if win or player.turn == False:
            break


def play_again():
    choice = True
    while choice:
        again_choice = input('Do you want to play again? Y or N: ')
        if again_choice in 'Yy':
            tic_tac_toe()
        elif again_choice in 'Nn':
            print('Ok, goodbye!')
        else:
            print('Please, write Y or N')


tic_tac_toe()
play_again()

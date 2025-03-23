VALID_MOVES: list[str] = ['1,1', '1,2', '1,3','2,1', '2,2', '2,3','3,1', '3,2', '3,3']
PLAYER_SIGN: list[str] = ['X', 'O']
EMPTY_BOARD: list[list[str]] = [
    ['', '', '',],
    ['', '', '',],
    ['', '', '',],
]

def print_board(board: list) -> None:
    str = 6 * '--' + '\n'
    for x in board:
        for y in x:
            val = y
            if val == '':
                val = ' '
            str +='| ' + val + ' '
        str += '|\n' + 6 * '--' + '\n'
    print(str)

def is_valid(board: list, move: str) -> bool:
    if move not in VALID_MOVES:
        return False
    [x, y] = move.split(',')
    x, y = int(x) - 1, int(y) - 1
    return board[x][y] == ''

def clean_input(input: str) -> str:
    return input.strip().replace(' ', '')

def is_win(board: list) -> bool:
    for i in range(3):
        if board[0][i] != '' and board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            return True
        if board[i][0] != '' and board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            return True
    if board[0][0] != '' and board[1][1] == board[0][0] and board[1][1] == board[2][2]:
        return True
    if board[0][2] != '' and board[0][2] == board[1][1] and board[0][2] == board[2][0]:
        return True
    return False

def add_move(board: list, move: str, sign: str) -> None:
    [x, y] = move.split(',')
    x, y = int(x) - 1, int(y) - 1
    board[x][y] = sign

def get_valid_input(board: list, player: int) -> str:
    player_input = input('Player ' + str(player) + ' please enter ' + PLAYER_SIGN[player-1] + ' in valid place ')
    player_input = clean_input(player_input)
    while not is_valid(board, player_input):
        print(player_input + ' is invalid')
        player_input = input('Player ' + str(player) + ' please enter ' + PLAYER_SIGN[player-1] + ' in valid place ')
        player_input = clean_input(player_input)
    return player_input

if __name__ == '__main__':
    current_move: int = 0
    board = EMPTY_BOARD
    while True:
        player = current_move % 2 + 1
        print_board(board)
        player_input = get_valid_input(board, player)
        add_move(board, player_input, PLAYER_SIGN[player-1])
        if current_move > 3:
            if is_win(board) == 1:
                print('Player ' + str(player) + ' WIN')
                print_board(board)
                break
            if current_move == 8:
                print('It is a draw')
                print_board(board)
                break
        current_move += 1


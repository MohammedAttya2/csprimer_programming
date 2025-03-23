#test tic_tac_toe.py
from tic_tac_toe import is_valid, clean_input, is_win, add_move

def test_is_valid():
    board = [
        ['X', 'O', 'X',],
        ['O', 'X', 'O',],
        ['X', 'O', '',],
    ]
    assert is_valid(board, '1,1') == False
    assert is_valid(board, '1,4') == False
    assert is_valid(board, '4,4') == False
    assert is_valid(board, '3,3') == True

def test_clean_input():
    assert clean_input(' 1, 1 ') == '1,1'
    assert clean_input(' 1, 1') == '1,1'
    assert clean_input('1, 1 ') == '1,1'

def test_is_win():
    board = [
        ['X', 'O', 'X',],
        ['O', 'X', 'O',],
        ['X', 'O', 'X',],
    ]
    assert is_win(board) == True
    board = [
        ['X', 'O', 'X',],
        ['O', 'X', 'O',],
        ['', 'O', '',],
    ]
    assert is_win(board) == False
    board = [
        ['X', 'O', 'X',],
        ['O', 'X', 'O',],
        ['X', '', 'X',],
    ]
    assert is_win(board) == True
    board = [
        ['X', 'O', 'X',],
        ['O', 'X', 'O',],
        ['', 'O', 'X',],
    ]
    assert is_win(board) == True

def test_add_move():
    board = [
        ['', '', '',],
        ['', '', '',],
        ['', '', '',],
    ]
    add_move(board, '3,3', 'X')

    assert board == [
        ['', '', '',],
        ['', '', '',],
        ['', '', 'X',],
    ]
    add_move(board, '2,2', 'O')

    assert board == [
        ['', '', '',],
        ['', 'O', '',],
        ['', '', 'X',],
    ]
    add_move(board, '1,2', 'X')
    assert board == [
        ['', 'X', '',],
        ['', 'O', '',],
        ['', '', 'X',],
    ]

def test_all():
    test_is_valid()
    test_clean_input()
    test_is_win()
    test_add_move()

if __name__ == '__main__':
    test_all()
    print('All tests passed')

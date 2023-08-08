from project import horizontal_match, vertical_match, diagonal_left_match, diagonal_right_match

def main():
    test_horizontal_match()
    test_vertical_match()
    test_diagonal_left_match()
    test_diagonal_right_match()

def test_horizontal_match():
    board = [
        ['◯', '◯', '◯', '◯', '◯', '◯'],
        ['◯', '◯', '◯', '◯', '◯', '◯'],
        ['◯', '◯', '◯', '◯', '◯', '◯'],
        ['◯', '◯', '◯', '◯', '◯', '◯'],
        ['◯', '🔴', '🔴', '🔴', '◯', '◯'],
        ['◯', '🟡', '🟡', '🟡', '🟡', '◯']
    ]
    
    assert horizontal_match(5, 4, board, 1) == True
    
    
def test_vertical_match():
    board = [
        ['◯', '◯', '◯', '◯', '◯', '◯'],
        ['◯', '◯', '◯', '◯', '◯', '◯'],
        ['◯', '🟡', '◯', '◯', '◯', '◯'],
        ['◯', '🟡', '🔴', '◯', '◯', '◯'],
        ['◯', '🟡', '🔴', '◯', '◯', '◯'],
        ['◯', '🟡', '🔴', '◯', '◯', '◯']
    ]
    
    assert vertical_match(2, 1, board, 1)
    
def test_diagonal_left_match():
    board = [
        ['◯', '◯', '◯', '◯', '◯', '◯'],
        ['◯', '◯', '◯', '◯', '◯', '◯'],
        ['◯', '◯', '◯', '🟡', '◯', '◯'],
        ['◯', '◯', '🟡', '🟡', '◯', '◯'],
        ['◯', '🟡', '🔴', '🔴', '◯', '◯'],
        ['🟡', '🔴', '🔴', '🔴', '◯', '◯']
    ]
    
    assert diagonal_left_match(2, 3, board, 1)
    
def test_diagonal_right_match():
    board = [
        ['◯', '◯', '◯', '◯', '◯', '◯'],
        ['◯', '◯', '◯', '◯', '◯', '◯'],
        ['◯', '◯', '🟡', '◯', '◯', '◯'],
        ['◯', '◯', '🟡', '🟡', '◯', '◯'],
        ['◯', '◯', '🔴', '🔴', '🟡', '◯'],
        ['◯', '◯', '🔴', '🔴', '🔴', '🟡']
    ]
    
    diagonal_right_match(3, 2, board, 1)
    
if __name__ == '__main__':
    main()
import random
ROWS, COLS = 6, 7
PLAYER_SYMBOL = ['🔴', '🟡']
EMPTY = '◯'
SEARCH_RANGE = [1, 2, 3]

def main():
    
    while True:
        board = [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]
        player = random.choice(PLAYER_SYMBOL)
        pieces_in_col = [
            {1: 0}, {2: 0}, {3: 0}, {4: 0}, {5: 0}, {6: 0}, {7: 0}
        ]
        full_columns = 0
        print('Welcome to Connect 4!')
        print('By: Daniel McGuire\n')
        print_board(board)
        while True:
            
            if full_columns == 7:
                break
            print(f"{player} player's turn")
            while True:
                
                column_index = get_column()
                if pieces_in_col[column_index][column_index + 1] == 6:
                    print('This column has no more space!')
                    continue
                break
        
            pieces_in_col[column_index][column_index + 1] += 1
            
            if pieces_in_col[column_index][column_index + 1] == 6:
                full_columns += 1
                
            row_index = get_row(board, player, column_index) 
            board[row_index][column_index] = player  
            print_board(board)  
            if is_four(row_index, column_index, board):
                winner = player
                break
            
            player = PLAYER_SYMBOL[0] if player == PLAYER_SYMBOL[1] else PLAYER_SYMBOL[1]
            
        if winner:
            print(f'{winner} player wins!')
        else:
            print('Draw game!')
        
        answer = get_answer()   
            
        if answer == 'n':
            print('Goodbye!')
            break
    
    
def print_board(board) -> None:
    
    print('+----------------------------------+')
    for i in range(ROWS):
        print('|', end='')
        for j in range(COLS):
            if board[i][j] == EMPTY:
                print(f' {board[i][j]}  |', end='')
            else:
               print(f' {board[i][j]} |', end='') 
        print()
        print('+----------------------------------+')
    print('  1    2    3    4     5    6    7\n')


def get_column() -> int:
    
    while True:
        
        try:
            column = int(input('Select column to drop: ')) - 1
            if column < 0 or column > 8:
                raise ValueError()
        
        except ValueError:
            print('Input a column between 1 and 7')
            
        else:
            return column


def get_row(board, player, column) -> int:
    
    for row in reversed(range(ROWS)):
        if board[row][column] != EMPTY:
            continue
        else:
            row_index = row
        break
    
    return row


def is_four(row, col, board) -> bool:
    
    if horizontal_match(row, col, board, 1):
        return True
    
    if vertical_match(row, col, board, 1):
        return True
    
    
    if diagonal_left_match(row, col, board, 1):
        return True
    
    if diagonal_right_match(row, col, board, 1):
        return True
    
    return False


def horizontal_match(row, col, board, matches) -> bool:
    
    # search right
    for inc in SEARCH_RANGE:
        if col + inc >= COLS:
            continue
        
        if board[row][col] == board[row][col + inc]:
            matches += 1  
        else:
            break
         
    # search left
    for inc in SEARCH_RANGE:
        if col - inc < 0:
            continue
        
        if board[row][col] == board[row][col - inc]:
            matches += 1  
        else:
            break        
    
    if matches >= 4:
        return True
    
    return False
        
        
def vertical_match(row, col, board, matches) -> bool:
    
    # search down
    for inc in SEARCH_RANGE:
        if row + inc >= ROWS:
            continue
        
        if board[row][col] == board[row + inc][col]:
            matches += 1 
        else:
            break 
         
    # search up
    for inc in SEARCH_RANGE:
        if row - inc < 0:
            continue
        
        if board[row][col] == board[row - inc][col]:
            matches += 1  
        else:
            break        
        
    if matches >= 4:
        return True
    
    return False


def diagonal_left_match(row, col, board, matches) -> bool:
    
    # search up-right
    for inc in SEARCH_RANGE:
        if row - inc < 0 or col + inc >= COLS:
            continue
        
        if board[row][col] == board[row - inc][col + inc]:
            matches += 1 
        else:
            break 
         
    # search down-left
    for inc in SEARCH_RANGE:
        if row + inc >= ROWS or col - inc < 0:
            continue
        
        if board[row][col] == board[row + inc][col - inc]:
            matches += 1
        else:
            break
           
    if matches >= 4:
        return True
    
    return False


def diagonal_right_match(row, col, board, matches) -> bool:
    
# search up-left
    for inc in SEARCH_RANGE:
        if row - inc < 0  or col + inc >= COLS:
            continue
        
        if board[row][col] == board[row - inc][col + inc]:
            matches += 1 
        else:
            break 
         
    # search down-right
    for inc in SEARCH_RANGE:
        if row + inc >= ROWS or col + inc >= COLS:
            continue
        
        if board[row][col] == board[row + inc][col + inc]:
            matches += 1
        else:    
            break
           
    if matches >= 4:
        return True
    
    return False


def get_answer() -> None:
    
    while True:
        answer = input('Would you like to play another? (y/n): ').lower()
        
        if answer == 'y' or answer == 'n':
            return answer

    
if __name__ == '__main__':
    main()
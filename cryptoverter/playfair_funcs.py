from constants import UPPERCASES, UPPERCASE_START, ENC, DEC


def add_text_between_same_char(text):
    
    new_text = ''
    null_value = 'x'
    text_len = len(text)    
    
    for i in range(text_len):
        if i + 1 != text_len and i % 2 == 0 and text[i] == text[i+1]:
            new_text += text[i]
            new_text += null_value
        else:
            new_text += text[i]
            
    return new_text


def create_playfair_board(key):
    
    grid = []
    used_letters = []
    
    letter_count = 0
    row = 0
    is_full = False
    
    for i, char in enumerate(key):
        
        index = ord(char) - UPPERCASE_START
        
        if char not in used_letters:
            if char == 'J':
                used_letters.append('I')
            elif char == 'I':
                used_letters.append('J')
            grid.append(char)
            used_letters.append(char)
            
    grid = fill_remaining_grid(grid, used_letters)
            
    new_grid = [[], [], [], [], []] 
    grid_dimensions = len(new_grid)
    
    for row in range(grid_dimensions):
        for col in range(grid_dimensions):
            char = grid[row * 5 + col]
            new_grid[row].append(char)    
            
    return new_grid


def get_translated_text(pairs, grid, mode):
    
    encrypted_text = ''
    
    if mode == ENC:
        shift_amount = 1
    elif mode == DEC:
        shift_amount = -1 
    
    for pair in pairs:
        
        char1 = pair[0]
        char2 = pair[1]
        for row in range(len(grid)):
            for col in range(len(grid)):
                if char1 == grid[row][col]:
                    row1 = row
                    col1 = col
                if char2 == grid[row][col]:
                    row2 = row
                    col2 = col
                    
        if col1 == col2:
            next_row1 = (row1 + shift_amount) % 5
            next_row2 = (row2 + shift_amount) % 5
            encrypted_text += grid[next_row1][col1] + grid[next_row2][col2]
            
        elif row1 == row2:
            next_col1 = (col1 + shift_amount) % 5
            next_col2 = (col2 + shift_amount) % 5
            encrypted_text += grid[row1][next_col1] + grid[row1][next_col2]
            
        else:
            encrypted_text += grid[row1][col2] + grid[row2][col1]
                
    return encrypted_text

def get_playfair_key():
    
    while True:
        
        key = input('Enter your key: ')
        key = key.replace(' ', '')
        
        if not key:
            print('Key must be a minimum of 1 character')
            
        elif not key.isalpha():
            print('Key must be all alphabetical characters')
            
        else:
            return key.upper()
                

def get_text_list(text):
    
    text_list = []
    
    for i, char in enumerate(text):
        letter = char.upper()
        if i % 2 == 0:
            text_list.append(letter)
        else:
            text_list[int(i / 2)] += letter
    
    return text_list


def fill_remaining_grid(grid, used_letters):
    
    for letter in UPPERCASES:
        
        if letter not in used_letters:
            
            grid.append(letter)
            used_letters.append(letter)
            
    return grid
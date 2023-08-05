from constants import ROUND_CONST, ENC, DEC, SBOX, INVERSE_SBOX, GALOIS_ENC, GALOIS_DEC, X_TO_POWER_TEN, IRREDUCIBLE_POLY_1, X_TO_POWER_NINE, IRREDUCIBLE_POLY_2, X_TO_POWER_EIGHT, IRREDUCIBLE_POLY_3, AES_CBC, AES_ECB


def add_to_end_matrix(end_matrix, state_array):
    
    matrix_row = len(state_array)
    matrix_col = (len(state_array[0]))
    
    for row in range(matrix_row):
        
        for col in range(matrix_col):
            
            end_matrix[row].append(state_array[row][col])
    
    return end_matrix


def add_to_keyschedule(key_matrix, col):
    for i in range(len(col)):
        key_matrix[i].append(col[i])
        
    return key_matrix


def apply_round_consts(last, round_num):
    
    last[0] = hex(int(last[0], 16) ^ ROUND_CONST[round_num])
            
    return last 


def apply_sbox(matrix, mode=0): 

    row_len = len(matrix)
    col_len = len(matrix[0])

    if mode == ENC:
        reference_table = SBOX
    elif mode == DEC:
        reference_table = INVERSE_SBOX
    else:
        reference_table = SBOX
        row_len = 1

    for row in range(row_len):
        for col in range(col_len):
            if row_len != 1:
                sbox_row, sbox_col = get_sbox_coordinates(matrix[row][col]) 
                matrix[row][col] = hex(reference_table[sbox_row][sbox_col]) 
            else:
                sbox_row, sbox_col = get_sbox_coordinates(matrix[col]) 
                matrix[col] = hex(reference_table[sbox_row][sbox_col])            
        
    return matrix


def cbc_decryption(matrix_num, hex_matrix, iv_matrix, state_array):

    if matrix_num == 0:
        state_array = xor_matrices(state_array, iv_matrix)
    else:
        prev_matrix = get_matrix(hex_matrix, matrix_num - 1)
        state_array = xor_matrices(state_array, prev_matrix) 
        
    return state_array  
  
            
def cbc_encryption(matrix_num, current_matrix, key, iv_matrix, state_array):

    if matrix_num == 0:
        state_array = xor_matrices(current_matrix, iv_matrix)
    else:
        state_array = xor_matrices(current_matrix, state_array)
    state_array = xor_matrices(state_array, key)

    return state_array


def create_hex_matrix(hexcode):

    hex_matrix = [[], [], [], []]
    matrix_dimensions = len(hex_matrix)
    row_len = int(len(hexcode) / 8)
    value = 0
    
    for row in range(row_len):
        for col in range(matrix_dimensions):
            first_letter = value + row * 4 + col
            second_letter = first_letter + 1
            hex_matrix[col].append(hexcode[first_letter] + hexcode[second_letter])
            value += 1
            
    for row in range(matrix_dimensions):
        for col in range(row_len):
            hex_matrix[row][col] = hex(int(hex_matrix[row][col], 16))

    return hex_matrix


def create_matrix_from_ascii(value):
    
    matrix = [[],[],[],[]]
    
    for i, char in enumerate(value):
        index = i
        if index + 1 >= 4:
            index %= 4
        matrix[index].append(hex(ord(char)))
             
    return matrix


def dec_rounds(hex_matrix, count_hex_matrices, iv_matrix, key_schedule, rounds, mode):

    decryption_hex_matrix = [[], [], [], []]

    for matrix_num in range(count_hex_matrices):
        
        last_key = get_matrix(key_schedule, rounds)
        current_matrix = get_matrix(hex_matrix, matrix_num)
        state_array = xor_matrices(current_matrix, last_key)

        for round in reversed(range(rounds)):
            
            state_array = shift_rows(state_array, DEC)
            state_array = apply_sbox(state_array, DEC)
            round_key = get_matrix(key_schedule, round)
            state_array = xor_matrices(state_array, round_key)
            
            if round != 0:
                state_array = mix_columns(state_array, DEC)   
        
        if mode == AES_CBC:
            state_array = cbc_decryption(matrix_num, hex_matrix, iv_matrix, state_array)
            
        decryption_hex_matrix = add_to_end_matrix(decryption_hex_matrix, state_array)
        
    return decryption_hex_matrix


def enc_rounds(text_matrix, count_text_matrices, iv_matrix, key_schedule, rounds, mode):

    encryption_matrix = [[],[],[],[]]
    
    for matrix_num in range(count_text_matrices):
        
        first_key = get_matrix(key_schedule, 0)
        current_matrix = get_matrix(text_matrix, matrix_num)
        
        if mode == AES_ECB:
            state_array = xor_matrices(current_matrix, first_key)
        elif mode == AES_CBC:
            if matrix_num == 0:
                state_array = [[hex(0) for _ in range(4)] for _ in range(4)]
            state_array = cbc_encryption(matrix_num, current_matrix, first_key, iv_matrix, state_array)
        
        for round in range(rounds):
            
            state_array = apply_sbox(state_array, ENC)
            state_array = shift_rows(state_array, ENC)
            if not round + 1 == rounds:
                state_array = mix_columns(state_array, ENC) 
            round_key = get_matrix(key_schedule, round + 1)
            state_array = xor_matrices(state_array, round_key)
            
        encryption_matrix = add_to_end_matrix(encryption_matrix, state_array)
        
    return encryption_matrix


def galois_multiplication(matrix_col, mode):

    new_col = []
    bit_values = [1, 2, 4, 8]
    if mode == ENC:
        galois_array = GALOIS_ENC
    elif mode == DEC:    
        galois_array = GALOIS_DEC

    for i in range(len(matrix_col)):

        byte_value = 0
        for j in range(len(matrix_col)):

            multiplication_value = 0
            for value in bit_values:
                multiplication_value ^= (galois_array[i][j] & value) * int(matrix_col[j], 16)
            byte_value ^= multiplication_value

        if byte_value >= X_TO_POWER_TEN:
            byte_value -= X_TO_POWER_TEN
            byte_value ^= IRREDUCIBLE_POLY_1
        if byte_value >= X_TO_POWER_NINE:    
            byte_value -= X_TO_POWER_NINE
            byte_value ^= IRREDUCIBLE_POLY_2
        if byte_value >= X_TO_POWER_EIGHT:
            byte_value ^= IRREDUCIBLE_POLY_3
        
        new_col.append(hex(byte_value))

    return new_col


def get_count_matrices(matrix):

    return int(len(matrix[0]) / 4)


def get_encrypted_hex():

    while True:
        valid_numbers = ['0', '1' , '2', '3', '4', '5', '6', '7', '8', '9']
        valid_letters = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F']
        valid_hex = True
        encrypted_hex = input('Enter encrypted value in hexadecimal: ')
        for value in encrypted_hex:
            if value not in valid_numbers and value not in valid_letters:
                print('One of the values in your Hexcode is not a valid hexadecimal value. Valid values are 0-f')
                valid_hex = False

        if not valid_hex:
            continue            

        if not encrypted_hex:
            print('You cannot leave this field blank')
        elif len(encrypted_hex) % 32 != 0:
            print("Input hexadecimal value must must be divisible by 32 hexadecimal digits long")
        else:
            break

    return encrypted_hex


def get_expansions(key_len):
    
    expansions = 10 if key_len == 16 else 9 if key_len == 24 else 7
    
    return expansions


def get_first_and_last_col(key_matrix, first_index, col_count):
    
    num_rows = len(key_matrix)
    num_cols = len(key_matrix[0])
    last_word = first_index + col_count - 1
    last_col = []
    first_col = []
    
    for i in range(num_rows):
        for j in range(num_cols):
            if j == first_index:
                first_col.append(key_matrix[i][j])
            elif j == last_word:
                last_col.append(key_matrix[i][j])  
                
    return first_col, last_col


def get_iv():

    while True:

        iv = input('Enter IV(Optional): ')
        iv_len = len(iv)

        if not iv:
            return iv
        elif iv_len == 16:
            break
        else:
            print('The IV entered must either be 128 bits or empty')

    return iv


def get_aes_key():

    valid_bits = [16, 24, 32]

    while True:

        key = input('Enter Secret Key: ')
        if len(key) not in valid_bits:
            print('You did not enter a valid amount of bits for the key (128, 192 or 256 bits)')
        else:
            break

    return key


def get_key_schedule(key_matrix, expansions):

    first_index = 0
    col_count = len(key_matrix[0])

    for round in range(expansions):
        
        first = False
        
        for word in range(col_count):
            
            first_col, last_col = get_first_and_last_col(key_matrix, first_index, col_count)
            
            if not first:
                last_col = shift_column(last_col)
                last_col = apply_sbox(last_col)
                last_col = apply_round_consts(last_col, round)
                first = True
                
            elif col_count == 8 and word % 4 == 0:
                last_col = apply_sbox(last_col)
                
            new_col = xor_columns(first_col, last_col)
            key_matrix = add_to_keyschedule(key_matrix, new_col)
            first_index += 1
          
    return key_matrix


def get_matrix(full_matrix, matrix_num):
    
    matrix = [[],[],[],[]]
    start_col = matrix_num * 4
    end_col = start_col + 4
    matrix_len = len(full_matrix)

    for i in range(matrix_len):
         for j in range(start_col, end_col):
             matrix[i].append(full_matrix[i][j])
             
    return matrix


def get_padding(key_len, text_len):

    block_len = 16
    padding = key_len - (text_len % key_len)

    if padding >= block_len:
        padding -= key_len % block_len
        while padding >= block_len:
            padding -= block_len

    return padding


def get_rounds(key_len):

    rounds = 10 if key_len == 16 else 12 if key_len == 24 else 14

    return rounds


def get_sbox_coordinates(hex_byte):

    byte_len = len(hex_byte)

    if byte_len == 3:
        first_hex = str(0)
        second_hex = hex_byte[2]
    else:
        first_hex = hex_byte[2]
        second_hex = hex_byte[3]

    if first_hex.isdigit():
        row = int(first_hex)
    else:
        row = int(first_hex, 16)
    
    if second_hex.isdigit():
        col = int(second_hex)
    else:
        col = int(second_hex, 16)

    return row, col


def hex_matrix_to_ascii(end_matrix):
    
    matrix_len = len(end_matrix)
    count_matrices = get_count_matrices(end_matrix)
    plain_text = ''
    
    for count in range(count_matrices):
        
        index_matrix = get_matrix(end_matrix, count)
        
        for row in range(matrix_len):
            
            for col in range(matrix_len):
                
                ascii_value = int(index_matrix[col][row], 16)
                if  0 <= ascii_value <= 16:
                    continue
                plain_text += chr(ascii_value)
            
    return plain_text


def hex_matrix_to_string(end_matrix):
    
    hex_string = ''
    matrix_len = len(end_matrix)
    matrix_count = get_count_matrices(end_matrix)
    
    for count in range(matrix_count):
        
        index_matrix = get_matrix(end_matrix, count)
        
        for row in range(matrix_len):
            
            for col in range(matrix_len):
                
                byte = str(index_matrix[col][row])
                byte_len = len(byte)
               
                if byte_len == 3:
                    value = '0' + byte[2]
                else:
                    value = byte[2] + byte[3]
                
                hex_string += value
    
    return hex_string


def mix_columns(matrix, mode):

    col_matrix = [[], [], [], []]
    new_matrix = [[], [], [], []]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            col_matrix[i].append(matrix[j][i])

        col_matrix[i] = galois_multiplication(col_matrix[i], mode)
         
    for i in range(len(new_matrix)):
        for j in range(len(new_matrix)):
            new_matrix[j].append(col_matrix[i][j])     

    return new_matrix


def pad_text(text, padding):

    for _ in range(padding):
        text += chr(padding)

    return text


def shift_column(last_col):
    
    first_element = last_col[0]
    last_col = last_col[1:] + [first_element]
    return last_col


def shift_rows(matrix, mode):
       
    temp = [] 
       
    for i in range(len(matrix)):
        temp = matrix[i].copy()
        for j in range(len(matrix[0])):
            if mode == ENC:
                matrix[i][j - i] = temp[j]
            else:
                index = j + i 
                if index > 3:
                    index -= 4
                matrix[i][index] = temp[j]
            
    return matrix


def xor_columns(first_col, last_col):
    
    col_len = len(last_col)

    for i in range(col_len):
        last_col[i] = hex(int(last_col[i], 16) ^ int(first_col[i], 16))
        
    return last_col


def xor_matrices(first, second):
        
    matrix = [[],[],[],[]]
    matrix_len = len(matrix)

    for i in range(matrix_len):
        for j in range(matrix_len):
            matrix[j].append(hex(int(first[j][i], 16) ^ int(second[j][i], 16))) 
    
    return matrix
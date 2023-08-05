from aes_funcs import get_aes_key, create_matrix_from_ascii, get_padding, pad_text, get_count_matrices, get_iv, get_rounds, get_expansions, get_key_schedule, enc_rounds, hex_matrix_to_string
from caesar_funcs import get_caesar_key, apply_shift_with_one_key, get_multiple_keys, apply_shift_with_multiple_keys
from playfair_funcs import get_text_list, add_text_between_same_char, get_playfair_key, create_playfair_board, get_translated_text
from general_funcs import print_mode, get_plain_text, get_option_from_list
from constants import AES_ENC, CAESAR_ENC, ENC, ONE_KEY, MULTIPLE_KEYS, AES_CBC, AES_ECB, PLAYFAIR_ENC


def advanced_encryption_system():
    
    while True:

        try:

            print_mode(AES_ENC)

            text = get_plain_text()
            text_len = len(text)

            key = get_aes_key()
            key_len = len(key)
            key_matrix = create_matrix_from_ascii(key)

            padding = get_padding(key_len, text_len)
            if padding != 0:
                text = pad_text(text, padding)

            text_matrix = create_matrix_from_ascii(text)
            count_text_matrices = get_count_matrices(text_matrix)

            mode = get_option_from_list([AES_ECB, AES_CBC])
                        
            if mode == AES_ECB:
                iv_matrix = [[hex(0) for _ in range(4)] for _ in range(4)]
            elif mode == AES_CBC:
                iv = get_iv()
                iv_matrix = create_matrix_from_ascii(iv) 
               
            rounds = get_rounds(key_len)
            expansions = get_expansions(key_len)
            
            key_schedule = get_key_schedule(key_matrix, expansions) 
            encrypted_matrix = enc_rounds(text_matrix, count_text_matrices, iv_matrix, key_schedule, rounds, mode)
            plain_text = hex_matrix_to_string(encrypted_matrix)
            print(f'Encrypted value: {plain_text}\n')

        except KeyboardInterrupt:
            print()
            return
        
        
def caesar():
    
    while True:
        
        try:
            
            print_mode(CAESAR_ENC)
            
            text = get_plain_text()
            
            mode = get_option_from_list([ONE_KEY, MULTIPLE_KEYS])
            
            if mode == ONE_KEY:            
                shift_key = get_caesar_key()
                encrypted_text = apply_shift_with_one_key(text, shift_key, ENC)
            elif mode == MULTIPLE_KEYS:
                key_list = get_multiple_keys(text)
                encrypted_text = apply_shift_with_multiple_keys(text, key_list, ENC)
            
            print(f'Encrypted value: {encrypted_text}\n')            
            
        except KeyboardInterrupt:
            print()
            return
        
        
def playfair():
    
    while True:
        
        try:
            
            print_mode(PLAYFAIR_ENC)
            
            while True:
                
                text = get_plain_text()
                text = text.replace(' ', '')
                
                if not text.isalpha():
                    print('In playfair cipher all characters must be a letter of the alphabet')
                else:
                    break
                    
            text = add_text_between_same_char(text)
            
            if len(text) % 2 != 0:
                text += 'X'
            
            text_list = get_text_list(text)
                
            key = get_playfair_key()
            
            board = create_playfair_board(key)
            
            text = get_translated_text(text_list, board, ENC)
            
            print(f'Encypted value: {text}')
            
        except KeyboardInterrupt:
            print()
            return
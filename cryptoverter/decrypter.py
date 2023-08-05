from aes_funcs import get_encrypted_hex, create_hex_matrix, get_count_matrices, get_aes_key, create_matrix_from_ascii, get_iv, get_rounds, get_expansions, get_key_schedule, dec_rounds, xor_matrices, hex_matrix_to_ascii 
from caesar_funcs import get_encrypted_text, get_caesar_key, apply_shift_with_one_key, get_multiple_keys, apply_shift_with_multiple_keys
from playfair_funcs import get_text_list, get_playfair_key, create_playfair_board, get_translated_text
from general_funcs import print_mode, get_option_from_list, get_plain_text
from constants import AES_DEC, CAESAR_DEC, DEC, ONE_KEY, MULTIPLE_KEYS, AES_ECB, AES_CBC, PLAYFAIR_DEC


def advanced_encryption_system():
        
        while True:

            try:
                print_mode(AES_DEC)

                encrypted_hex = get_encrypted_hex()
                hex_matrix = create_hex_matrix(encrypted_hex)
                count_hex_matrices = get_count_matrices(hex_matrix)

                key = get_aes_key()
                key_len = len(key)
                key_matrix = create_matrix_from_ascii(key)

                mode = get_option_from_list([AES_ECB, AES_CBC])
                
                if mode == AES_ECB:
                    iv_matrix = [[hex(0) for _ in range(4)] for _ in range(4)]
                elif mode == AES_CBC:
                    iv = get_iv()
                    iv_matrix = create_matrix_from_ascii(iv)
                
                rounds = get_rounds(key_len)
                expansions = get_expansions(key_len)

                key_schedule = get_key_schedule(key_matrix, expansions)     
                decrypted_hex_matrix = dec_rounds(hex_matrix, count_hex_matrices, iv_matrix, key_schedule, rounds, mode)
                plain_text = hex_matrix_to_ascii(decrypted_hex_matrix)
                print(f'Decrypted value: {plain_text}')
            
            except KeyboardInterrupt:
                print()
                return
            
            
def caesar():
    
    while True:
        
        try:
            
            print_mode(CAESAR_DEC)
            
            text = get_encrypted_text()
                       
            mode = get_option_from_list([ONE_KEY, MULTIPLE_KEYS])
            
            if mode == ONE_KEY:
                shift_key = get_caesar_key()
                decrypted_text = apply_shift_with_one_key(text, shift_key, DEC)
                
            elif mode == MULTIPLE_KEYS:
                key_list = get_multiple_keys(text)
                decrypted_text = apply_shift_with_multiple_keys(text, key_list, DEC)
            
            print(f'Decrypted value: {decrypted_text}\n')            
            
        except KeyboardInterrupt:
            print()
            return
        
        
def playfair():
    
    while True:
        
        try:
            
            print_mode(PLAYFAIR_DEC)
            
            while True:
                
                encrypted_text = get_plain_text()
                encrypted_text.replace(' ', '')
                
                if not encrypted_text.isalpha():
                    print('All characters in the encrypted text must be a letter of the alphabet')
                    
                else:
                    break
             
            text_list = get_text_list(encrypted_text)
            
            key = get_playfair_key()
            
            board = create_playfair_board(key)
            
            decrypted_text = get_translated_text(text_list, board, DEC)
            
            print(f'Decrypted text: {decrypted_text}')
            print("Remove X's and piece together the text where necessary to form words")
            
            
        except KeyboardInterrupt:
            print()
            return
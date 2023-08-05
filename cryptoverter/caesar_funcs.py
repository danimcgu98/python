from constants import LOWERCASES, UPPERCASES, UPPERCASE_START, LOWERCASE_START, TOTAL_LETTERS, DEC, ENC, ONE_KEY, MULTIPLE_KEYS


def apply_shift_with_multiple_keys(text, key_list, mode):
    
    encrypted_text = ''
    if mode == DEC:
        multiplicative = -1
    elif mode == ENC:
        multiplicative = 1
        
    for index in range(len(text)):
        
        letter = text[index]
        key = key_list[index] * multiplicative
        
        if not letter.isalpha():
            encrypted_text += letter
        
        elif letter.isupper():
            char_index = ord(letter) + key - UPPERCASE_START
            
            char_index %= TOTAL_LETTERS
                
            encrypted_text += UPPERCASES[char_index]
            
        elif letter.islower():
            char_index = ord(letter) + key - LOWERCASE_START
            
            char_index %= TOTAL_LETTERS
                
            encrypted_text += LOWERCASES[char_index]
    
    return encrypted_text 


def apply_shift_with_one_key(text, shift_key, mode):
    
    encrypted_text = ''
    if mode == DEC:
        shift_key *= -1
    
    for char_index in range(len(text)):
        
        letter = text[char_index]
        
        if not letter.isalpha():
            encrypted_text += letter
        
        elif letter.isupper():
            index = ord(letter) + shift_key - UPPERCASE_START
            
            index %= TOTAL_LETTERS
                
            encrypted_text += UPPERCASES[index]
            
        elif letter.islower():
            index = ord(letter) + shift_key - LOWERCASE_START
            
            index %= TOTAL_LETTERS
                
            encrypted_text += LOWERCASES[index]
    
    return encrypted_text


def get_encrypted_text():
    
    while True:

        text = input('Enter encrypted text: ')

        if not text:
            print('You did not enter any text')
        else:
            break

    return text


def get_multiple_keys(text):
    
    text_len = len(text)
    key_list = []
    
    for key_num in range(text_len):
        
        while True:
        
            shift_key = input(f'Enter shift key for character {key_num + 1}: ')
            
            if not shift_key:
                print('You cannot leave this field empty')
                continue
                
            try:
                shift_key = int(shift_key)
                
            except ValueError:
                print('You did not enter an integer value')
                
            else:
                if shift_key != 0:
                    key_list.append(shift_key)
                    break
                else:
                    print('You cannot shift by the value 0')
                    
    return key_list


def get_caesar_key():
    
    while True:
        
        shift_key = input('Enter number to shift by: ')
        
        if not shift_key:
            print('You cannot leave this field empty')
            continue
            
        try:
            shift_key = int(shift_key)
            
        except ValueError:
            print('You did not enter an integer value')
            
        else:
            if shift_key != 0:
                return shift_key
            else:
                print('You cannot shift by the value 0')
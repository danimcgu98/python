def print_title():
    print('--------------------------------------')
    print('            Cryptoverter              ')
    print('  An ASCII Based Encryptor/Decryptor  ')
    print('         By: Daniel McGuire           ')
    print('--------------------------------------')
    print()


def print_mode(mode):
    print('----------------------------------------------------')
    print(f'          Current mode: {mode}')
    print('----------------------------------------------------')
    print('Press Ctrl + C to return to main menu\n')


def get_option_from_list(list, message=0):
    
    valid_options = []
    print('Options:')
    
    for i, option in enumerate(list):
        option_num = i + 1
        print(f'{option_num}. {option}')
        valid_options.append(str(option_num))
        
    if message != 0:
        print(message) 
        print()   
        
    while True:
        
        option = input('Enter number here: ')
        
        if not option:
            print('You cannot leave this field empty')
        elif option not in valid_options:
            print('You did not enter a valid option')
        else:
            break
        
    print()
    
    return list[int(option) - 1]


def get_plain_text():
    
    while True:

        text = input('Enter Plain text: ')

        if not text:
            print('You did not enter any text')
        else:
            break

    return text
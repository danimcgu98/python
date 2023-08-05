import encrypter
import decrypter
from general_funcs import print_title, get_option_from_list
from constants import ENC, DEC, AES, CAESAR, PLAYFAIR, EXIT_MESSAGE, RETURN_MENU_MESSAGE

def main():

    while True:
        try:
            menu()
        except KeyboardInterrupt:
            print('\nYou have pressed Ctrl + C\nThe program will now exit...\n')
            break
    

def menu():
    print_title()

    algorithm = get_option_from_list([AES, CAESAR, PLAYFAIR], EXIT_MESSAGE)

    try:
        mode = get_option_from_list([ENC, DEC], RETURN_MENU_MESSAGE)
        
    except KeyboardInterrupt:
        print()
        return


    if mode == ENC:
        if algorithm == AES:
            encrypter.advanced_encryption_system()
        elif algorithm == CAESAR:
            encrypter.caesar()
        elif algorithm == PLAYFAIR:
            encrypter.playfair()

    elif mode == DEC:
        if algorithm == AES:
            decrypter.advanced_encryption_system()
        elif algorithm == CAESAR:
            decrypter.caesar()
        elif algorithm == PLAYFAIR:
            decrypter.playfair()


if __name__ == '__main__':
    main()
# Cryptoverter
# An Ascii CLI application
## By: Daniel McGuire

#### Video Demo: https://youtu.be/TQsEfL07hys

#### Description: This project is a Command Line interface for plain text encryption and decryption. This program has 3 different ciphers: AES, Caesar Cipher, and the Playfair Cipher. It takes a plain text for encryption in all scenarios and encrypts it with the desired encryption. In the decryption phase it requires the encrypted value be it Hexadecimal in AES, or strings in Caesar Cipher or Playfair Cipher. While it would have been much easier to use a library to code the AES encryptor and decryptor I chose to do it from scratch to learn one of the most widely used encryptions to date. I chose to separate all the functions for each process into helper files that way it would be easier to understand. 

#### Files:

##### aes_funcs.py: This file contains all the functions related to aes that the encryptor.py file will call when it needs to access certain functions for encryption/decryption

##### caesar_funcs.py: This file contains all the functions related to caesar cipher that the encryptor.py file will call when it needs to access certain functions for encryption/decryption

##### constants.py: This file contains constants that are shared between all the different files so I could streamline the process instead of redeclaring the same value

##### decryptor.py: This file contains all the main functions by which all of the different decryptions are called and allows for the functions to be more sortable and readable for understandings sake

##### encryptor.py: This file contains all the main functions by which all of the different encryptions are called and allows for the functions to be more sortable and readable for understandings sake

##### general_funcs.py: This file contains functions that are shared across all the files, similar to the constants yet being functions instead. Again this allows for me not to declare multiple of the same function

##### main_py: This file calls every other file. Since I like my main file to be clean I opted for it to only displaythe title and then call the functions from other files where all the messy work could be sorted out

##### playfair.py: This file contains all the functions related to playrfair cipher that the encryptor.py file will call when it needs to access certain functions for encryption/decryption

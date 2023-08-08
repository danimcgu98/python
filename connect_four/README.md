# Connect 4
## A Command Line version of the classic Connect 4 game

####Video Demo: https://youtu.be/kAZTgGEzQhs

####Description: The player's in this game play on a 6 by 7 column board in which they must drop pieces 1 by 1 and try to get 4 of their pieces in a row. Either by matching them horizontal, vertical or diagonal. The first player to do this wins the game. There are 2 players in this game, one is red (🔴) and the other is yellow (🟡).

####Files:

#####project.py: This contains the code for the connect 4 game. It contains 10 different functions which work together.

#####test_project.py: This contains the pytest cases for testing the different match cases of the game. This checks for diagonal matches, vertical matches or horizontal matches.

####Functions:

#####main(): the function that calls other the other functions within the game. Also regulates the game loop via a while True loop.

#####print_board(board): outputs the board in it's current state to the players at the beginning of each round. This function takes the current board as an array and outputs the board in a prettier state.

#####get_column(): this function ensures the player enters a valid column within the columns 1-7 and returns the value to main. This function also checks if the current column is fully occupied.

#####get_row(board, player, column): taking the current board, the player and the chosen column determines the row at which the piece will fall and returns it to main

#####is_four(row, col, board): this function calls 4 other functions in order to determine if there is a connect 4 that the current player has got after the piece was placed

#####horizontal_match(row, col, board, matches): this function scans left and right of the latest dropped piece to determine if there were any horizontal matches

#####vertical_match(row, col, board, matches): this function scans up and down from the latest dropped piece to determine if there were any vertical matches

#####diagonal_left_match(row, col, board, matches): this function scans up-right and down-left from the latest dropped piece to determine if there was a diagonal match

#####diagonal_right_match(row, col, board, matches): this function scans up-left and down-right from the latest dropped piece to determine if there was a diagonal match

#####get_answer(): this gets a valid answer from the user in the for of y or n in order to continue the game or not
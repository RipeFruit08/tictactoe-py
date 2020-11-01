# set BOARD_DIM value to determine size of tic tac toe board (3 is default)
BOARD_DIM = 3
BOARD = [
    ['-']*BOARD_DIM for _ in range(BOARD_DIM)
]

def print_board(board):
    board_dim = len(board)
    for row in range(board_dim):
        for col in range(board_dim):
            print(board[row][col], end=" ")
        print()

"""
(R)ead (E)val (P)rint (L)oop for the tic tac toe game
:return: None
"""
def repl():
    player_one = True
    while True:
        print_board(BOARD)
        playerTurnStr = "Player " + ("one (X)" if player_one else "two (O)") + "'s turn "
        cmd = input(playerTurnStr + "Enter command > ")
        valid_move = process_cmd(cmd, player_one)
        determine_winner()
        player_one = not player_one if valid_move else player_one


"""
Processes player command for the tic tac toe game
:param cmd: string representing the player command
:param player_one: boolean determining whether or not it is currently Player 1's turn
"""
def process_cmd(cmd, player_one):
    if cmd == "q":
        print("Quit signal received, exiting...")
        exit()
    else:
        # processes command to place piece. this command should be in the form
        # of two numbers separated by spaces For example the command "0 0" would 
        # place the player's piece on the board at (0,0)
        res = sanitize_input(cmd)
        if res:
            row, col = res[0], res[1]
            BOARD[row][col] = "X" if player_one else "O"
            return True
        else:
            # should be returning false 
            return res

"""
validates tic tac toe input 

:param cmd: the raw command from tic tac toe game 
:returns: tuple containing row and column coordinates if input is valid
          otherwise returns False
:raises ValueError: # todo handle this exception among any others 
"""
def sanitize_input(cmd):
    cmd_split = cmd.split()
    try:
        row = int(cmd_split[0])
        col = int(cmd_split[1])
        if row >= BOARD_DIM or col >= BOARD_DIM:
            print(f'({row}, {col}) is not a valid coordiante.', end=" ")
            print(f'Board is {BOARD_DIM}x{BOARD_DIM}')
            return False
        if BOARD[row][col] == "X" or BOARD[row][col] == "O":
            print(f'Cannot make move at {row, col} because a move has already been made there. Try again')
            return False
        return (row, col)
    except (ValueError, IndexError):
        print("Problem parsing command, try again")
        return False

"""
checks either all rows or all cols for a winning condition

:param flag: True if checking rows, False if checking cols
:return: None
"""
def checkRowsOrCols(flag):
    # check rows
    for row in range(BOARD_DIM):
        x_count = 0
        o_count = 0
        for col in range(BOARD_DIM):
            if flag:
                val = BOARD[row][col]
            else:
                val = BOARD[col][row]
            if val == "X":
                x_count += 1
            elif val == "O":
                o_count += 1
        win_cond(x_count, o_count)

"""
Checks boards row, columns, and diagonals to determine if there is a winner
"""
def determine_winner():
    checkRowsOrCols(True)
    checkRowsOrCols(False)
    # check diagonals
    # diagonals are either [(0,0), (1,1), (2,2)]
    #         or           [(2,0), (1,1), (0,2)]

    # first diagonal (back slash)
    x_count = 0
    o_count = 0
    for coord in range(BOARD_DIM):
        val = BOARD[coord][coord]
        if val == "X":
            x_count += 1
        elif val == "O":
            o_count += 1
    win_cond(x_count, o_count)

    # second diagonal (forward slash)
    x_count = 0
    o_count = 0
    for coord in range(BOARD_DIM):
        val = BOARD[(BOARD_DIM-1)-coord][coord]
        if val == "X":
            x_count += 1
        elif val == "O":
            o_count += 1
    win_cond(x_count, o_count)

"""
Determines whether or not a player has won the game
:param x_count: a number corresponding to how many matches Player 1 (X) has
:param o_count: a number corresponding to how many matches Player 2 (O) has
:return: function returns if no player has won, otherwise a winner is printed
         the program exits
"""
def win_cond(x_count, o_count):
    playerNumStr = ""
    if x_count == BOARD_DIM:
        playerNumStr = "One"
    elif o_count == BOARD_DIM:
        playerNumStr = "Two"
    else:
        return
    print_board(BOARD)
    print("Player " + playerNumStr + " wins!")
    exit()
    
if __name__ == "__main__":
    repl()
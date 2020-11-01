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

def repl():
    player_one = True
    while True:
        print_board(BOARD)
        foo = "Player " + ("one (X)" if player_one else "two (O)") + "'s turn "
        cmd = input(foo + "Enter command > ")
        valid_move = process_cmd(cmd, player_one)
        determine_winner()
        player_one = not player_one if valid_move else player_one


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
            BOARD[row][col] = val
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
    row = int(cmd_split[0])
    col = int(cmd_split[1])
    if row >= BOARD_DIM or col >= BOARD_DIM:
        print("This was not a valid move, try again")
        return False
    val = "X" if player_one else "O"
    if BOARD[row][col] == "X" or BOARD[row][col] == "O":
        print("This was not a valid move, try again")
        return False
    return (row, col)

def determine_winner():
    # check rows
    for row in range(BOARD_DIM):
        x_count = 0
        o_count = 0
        for col in range(BOARD_DIM):
            val = BOARD[row][col]
            if val == "X":
                x_count += 1
            elif val == "O":
                o_count += 1
        win_cond(x_count, o_count)
    # check columns
    for col in range(BOARD_DIM):
        x_count = 0
        o_count = 0
        for row in range(BOARD_DIM):
            val = BOARD[row][col]
            if val == "X":
                x_count += 1
            elif val == "O":
                o_count += 1
        win_cond(x_count, o_count)
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
    

def main():
    repl()

if __name__ == "__main__":
    main()
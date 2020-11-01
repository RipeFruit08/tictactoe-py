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
        cmd_split = cmd.split()
        board_dim = len(BOARD)
        row = int(cmd_split[0])
        col = int(cmd_split[1])
        if row >= board_dim or col >= board_dim:
            print("This was not a valid move, try again")
            return False
        val = "X" if player_one else "O"
        if BOARD[row][col] == "X" or BOARD[row][col] == "O":
            print("This was not a valid move, try again")
            return False
        else:
            BOARD[row][col] = val
            return True

def determine_winner():
    board_dim = len(BOARD)
    # check rows
    for row in range(board_dim):
        x_count = 0
        o_count = 0
        for col in range(board_dim):
            val = BOARD[row][col]
            if val == "X":
                x_count += 1
            elif val == "O":
                o_count += 1
        win_cond(x_count, o_count)
    # check columns
    for col in range(board_dim):
        x_count = 0
        o_count = 0
        for row in range(board_dim):
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
    for coord in range(board_dim):
        val = BOARD[coord][coord]
        if val == "X":
            x_count += 1
        elif val == "O":
            o_count += 1
    win_cond(x_count, o_count)

    # second diagonal (forward slash)
    x_count = 0
    o_count = 0
    for coord in range(board_dim):
        val = BOARD[(board_dim-1)-coord][coord]
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
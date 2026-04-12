def tic_tac_toe():
    board = [" "] * 9

    def print_board():
        print(board[0], "|", board[1], "|", board[2])
        print("--+---+--")
        print(board[3], "|", board[4], "|", board[5])
        print("--+---+--")
        print(board[6], "|", board[7], "|", board[8])

    def check_winner(p):
        return (
            (board[0]==board[1]==board[2]==p) or
            (board[3]==board[4]==board[5]==p) or
            (board[6]==board[7]==board[8]==p) or
            (board[0]==board[3]==board[6]==p) or
            (board[1]==board[4]==board[7]==p) or
            (board[2]==board[5]==board[8]==p) or
            (board[0]==board[4]==board[8]==p) or
            (board[2]==board[4]==board[6]==p)
        )

    player = "X"

    for i in range(9):
        print_board()

        move = int(input(player + " move (0-8): "))

        if move < 0 or move > 8:
            print("Enter number between 0 and 8 only")
            continue

        if board[move] != " ":
            print("Already filled, try again")
            continue

        board[move] = player

        if check_winner(player):
            print_board()
            print(player, "wins!")
            return

        # switch player
        if player == "X":
            player = "O"
        else:
            player = "X"

    print_board()
    print("Draw!")


tic_tac_toe()

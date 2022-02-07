board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

gamestatus = True
win_status = True
gamerun = 1
winteam = "what"
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

#player turn
def p_turn():
    position = int(input("Choose position : "))
    if board[position - 1] == "X" or board[position - 1] == "O":
        print("Please select other space")
        p_turn()
    else:
        board[position-1] = "X"

#com turn
def c_turn():
    import random
    position = random.randint(1, 9)
    #condition
    def dup_check():
        global dup
        if board[position-1] == "X":
            dup = True
        elif board[position-1] == "O":
            dup = True
        else:
            dup = False

    dup_check()
    while dup == True:
        position = random.randint(1, 9)
        dup_check()

    board[position - 1] = "O"
    print("Com position = ", position)



#win condition
def check_win():
    global gamerun
    global winteam
    #row 1
    if (board[0] == "X") and (board[1] == "X") and (board[2] == "X"):
        gamerun = 0
        winteam = "X Win!"
    elif (board[0] == "O") and (board[1] == "O") and (board[2] == "O"):
        gamerun = 0
        winteam = "O Win!"

    #row 2
    if (board[3] == "X") and (board[4] == "X") and (board[5] == "X"):
        gamerun = 0
        winteam = "X Win!"
    elif (board[3] == "O") and (board[4] == "O") and (board[5] == "O"):
        gamerun = 0
        winteam = "O Win!"

    #row 3
    if (board[6] == "X") and (board[7] == "X") and (board[8] == "X"):
        gamerun = 0
        winteam = "X Win!"
    elif (board[6] == "O") and (board[7] == "O") and (board[8] == "O"):
        gamerun = 0
        winteam = "O Win!"


    #column 1
    if (board[0] == "X") and (board[3] == "X") and (board[6] == "X"):
        gamerun = 0
        winteam = "X Win!"
    elif (board[0] == "O") and (board[3] == "O") and (board[6] == "O"):
        gamerun = 0
        winteam = "O Win!"

    #column 2
    if (board[1] == "X") and (board[4] == "X") and (board[7] == "X"):
        gamerun = 0
        winteam = "X Win!"
    elif (board[1] == "O") and (board[4] == "O") and (board[7] == "O"):
        gamerun = 0
        winteam = "O Win!"

    #column 3
    if (board[2] == "X") and (board[5] == "X") and (board[8] == "X"):
        gamerun = 0
        winteam = "X Win!"
    elif (board[2] == "O") and (board[5] == "O") and (board[8] == "O"):
        gamerun = 0
        winteam = "O Win!"

    #cross \
    if (board[0] == "X") and (board[4] == "X") and (board[8] == "X"):
        gamerun = 0
        winteam = "X Win!"
    elif (board[0] == "O") and (board[4] == "O") and (board[8] == "O"):
        gamerun = 0
        winteam = "O Win!"

    #criss /
    if (board[2] == "X") and (board[4] == "X") and (board[6] == "X"):
        gamerun = 0
        winteam = "X Win!"
    elif (board[2] == "O") and (board[4] == "O") and (board[6] == "O"):
        gamerun = 0
        winteam = "O Win!"






#check if game end
def game_going():
    global gamerun
    for x in board:
        if x == "-":
            gamerun += 1

    check_win()
    if gamerun > 0:
        gamestatus = True
    else:
        gamestatus = False


def play_game():
    game_going()
    while gamestatus == True:
        game_going()
        if gamerun == False:
            break
        display_board()
        game_going()
        if gamerun == False:
            break
        p_turn()
        game_going()
        if gamerun == False:
            break
        display_board()
        game_going()
        if gamerun == False:
            break
        c_turn()

    display_board()
    print("GAME END")
    print(winteam)

play_game()


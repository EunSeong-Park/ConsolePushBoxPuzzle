import sys
import os
import keyboard



def init():
    '''
    Load board
    Check the validity of game board:
        - uniqueness of player(@)
        - matching number of boxes(B) and holes(O)
    Find player and record its coordinate
    '''
    global board
    global RC

    board_load()


    isUnique = False
    Bcount = 0
    Ocount = 0

    for i in range(len(board)):
        tmp1 = board[i].find("@")
        if tmp1 != -1:
            if isUnique:
                sys.stderr.write("ERROR: Invalid game board(non-unique player), abort.\n")
                exit(1)
            isUnique = True
            RC = [i, tmp1]
        Bcount += board[i].count("B")
        Ocount += board[i].count("O")

    if Bcount != Ocount:
        sys.stderr.write("ERROR: Invalid game board(unmatched box and hole), abort.\n")
        exit(2)
    elif Bcount == 0:
        sys.stderr.write("ERROR: Invalid game board(no box or hole), abort.\n")
        exit(3)


def board_replace(char, coor):
    global board
    board[coor[0]] = "".join((board[coor[0]][:coor[1]], char, board[coor[0]][coor[1]+1:]))
    return


def coordinate(coor, R, C):
    return [coor[0] + R, coor[1] + C]


def key_handler(key_input):
    global board
    global command_history
    global RC

    key = key_input.lower()
    temp = RC

    if key == "w":
        temp = coordinate(temp, -1, 0)
    elif key == "s":
        temp = coordinate(temp, 1, 0)
    elif key == "a":
        temp = coordinate(temp, 0, -1)
    elif key == "d":
        temp = coordinate(temp, 0, 1)
    elif key == "q":
        exit(0)

    if temp[0] < 0 or temp[1] < 0: # invalid move
        return 0

    temp_map = board[temp[0]][temp[1]]

    if temp_map == "." or temp_map == "O": # just move
        board_replace(".", RC)
        board_replace("@", temp)
        RC = temp

    elif temp_map == "B": # box
        box_temp = [-1, -1]
        if key == "w":
            box_temp = coordinate(temp, -1, 0)
        elif key == "s":
            box_temp = coordinate(temp, 1, 0)
        elif key == "a":
            box_temp = coordinate(temp, 0, -1)
        elif key == "d":
            box_temp = coordinate(temp, 0, 1)

        if box_temp[0] < 0 or box_temp[1] < 0:  # invalid move
            return 0
        if board[box_temp[0]][box_temp[1]] == "#":  # invalid move
            return 0







def display_nav():
    sys.stdout.write("\n%-Manual" + "-" * 31 + "%\n"
                     "| WASD: Move | Q: Quit | R: Restart    |\n"
                     "| Put all of box(B) into holes(O).     |\n"
                     "| Have a good game :-)                 |\n"
                     "%" + "-" * 38 + "%\n")


def display_board():
    global board
    sys.stdout.write("\n".join(board))

def board_load():
    global board
    if len(sys.argv) >= 2:
        with open(os.path.dirname(os.path.realpath(__file__)) + "/" + sys.argv[1]) as f:
            board = f.read().split("\n")
    else:
        with open(os.path.dirname(os.path.realpath(__file__)) + "/map.txt") as f:
            board = f.read().split("\n")

# << MAIN >>


board = []


boxes = []
holes = []
clear_command = ""


init()

while 1:
    display_nav()
    display_board()
    key_handler(keyboard.read_hotkey())
    keyboard.stash_state()

    os.system('cls')

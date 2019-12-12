class Score():
    def __init__(self, playerX, playerO):
        self.Xscore = playerX
        self.Oscore = playerO

    def storescore(self, playerX, playerO):
        self.Xscore += playerX
        self.Oscore += playerO

    def coloration(self, colorcode, player):
        return colorcode + str(player) + "\33[0m"

    def printscore(self):
        print("Player X has " + score.coloration("\33[31m" , self.Xscore) + " points")
        print("Player O has " + score.coloration("\33[34m" , self.Oscore) + " points")



table = [[" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]]

def print_table():# Print the game's Table
    x = 0
    for i in table:
        for j in i:
            if x != 2: print(j, end=('|'))
            else: print(j)
            x += 1
        x = 0
        print('-----')

def check_combi():# Return True if a combination is found otherwise Return False
    x_l = 0
    x_c1 = 0
    x_c2 = 0
    x_c3 = 0
    x_d1 = 0
    x_d2 = 0
    o_l = 0
    o_c1 = 0
    o_c2 = 0
    o_c3 = 0
    o_d1 = 0
    o_d2 = 0
    X = "\33[31mX\33[0m"
    O = "\33[34mO\33[0m"
    l = 1
    c = 1
    # for i in range (len(table)):
    #     for j in range (len(table[i])):
    #         cell=table[i][j]
    #         if cell==X :
    #             x_l += 1
    #             if l == 1 or l == 2 or l == 3:
    #                 x_c1 += c==1
    #                 x_c2 += c==2
    #                 x_c3 += c==3
    #             if (l == 1 and c == 1) or (l == 2 and c == 2) or (l == 3 and c == 3): x_d1 += 1
    #             if (l == 3 and c == 1) or (l == 2 and c == 2) or (l == 1 and c == 3): x_d2 += 1
    #         elif cell == O:
    #             o_l += 1
    #             if l == 1 or l == 2 or l == 3:
    #                 o_c1 += c==1
    #                 o_c2 += c==2
    #                 o_c3 += c==3
    #             if (l == 1 and c == 1) or (l == 2 and c == 2) or (l == 3 and c == 3): o_d1 += 1
    #             if (l == 3 and c == 1) or (l == 2 and c == 2) or (l == 1 and c == 3): o_d2 += 1

    #         if x_l == 3 or x_c1 == 3 or x_c2 == 3 or x_c3 == 3 or x_d1 == 3 or x_d2 == 3:
    #             print("\33[31mPlayer X won!\33[0m")
    #             score.storescore(playerX=1, playerO=0)
    #             return True
    #         if o_l == 3 or o_c1 == 3 or o_c2 == 3 or o_c3 == 3 or o_d1 == 3 or o_d2 == 3:
    #             print("\33[34mPlayer O won!\33[0m")
    #             score.storescore(playerX=0, playerO=1)
    #             return True        
    #     c += 1
    #     c = 1
    #     l += 1
    #     x_l = 0
    #     o_l = 0
    # return False




    for i in table:
        for j in i:
            if j == X: x_l += 1
            if j == O: o_l += 1
            if j == X and (c == 1 and (l == 1 or l == 2 or l == 3)): x_c1 += 1
            if j == X and (c == 2 and (l == 1 or l == 2 or l == 3)): x_c2 += 1
            if j == X and (c == 3 and (l == 1 or l == 2 or l == 3)): x_c3 += 1
            if j == O and (c == 1 and (l == 1 or l == 2 or l == 3)): o_c1 += 1
            if j == O and (c == 2 and (l == 1 or l == 2 or l == 3)): o_c2 += 1
            if j == O and (c == 3 and (l == 1 or l == 2 or l == 3)): o_c3 += 1
            if j == X and ((l == 1 and c == 1) or (l == 2 and c == 2) or (l == 3 and c == 3)): x_d1 += 1
            if j == X and ((l == 3 and c == 1) or (l == 2 and c == 2) or (l == 1 and c == 3)): x_d2 += 1
            if j == O and ((l == 1 and c == 1) or (l == 2 and c == 2) or (l == 3 and c == 3)): o_d1 += 1
            if j == O and ((l == 3 and c == 1) or (l == 2 and c == 2) or (l == 1 and c == 3)): o_d2 += 1
            if x_l == 3 or x_c1 == 3 or x_c2 == 3 or x_c3 == 3 or x_d1 == 3 or x_d2 == 3:
                print("\33[31mPlayer X won!\33[0m")
                score.storescore(playerX=1, playerO=0)
                return True
            if o_l == 3 or o_c1 == 3 or o_c2 == 3 or o_c3 == 3 or o_d1 == 3 or o_d2 == 3:
                print("\33[34mPlayer O won!\33[0m")
                score.storescore(playerX=0, playerO=1)
                return True
            c += 1
        c = 1
        l += 1
        x_l = 0
        o_l = 0
    return False

def check_input_value(value):# Check if value between 1 and 3 included
    if value > 3 or value < 1: return 1
    return 0

def no_more_space():# If every cells are full Return True otherwise Return False
    full = 0
    for i in table:
        for j in i:
            if j != ' ': full += 1
    if full == 9: return True
    return False

def reset_table():# Set every cell to an empty one
    for i in range(0 ,len(table)):
        for j in range(0, len(table[i])): table[i][j] = ' '

def again_or_not(string):# Play again or quit the game
    score.printscore()
    while 1:# Loop till value is equal to 'y' or 'n'
        try:
            play = str(input(string))
            if play == 'y':
                reset_table()
                print("\33[1;4;32;100mWelcome back to Tic Tac Toe!\33[0m")
                return False
            elif play == 'n':
                print("See y'a!")
                return True
        except ValueError:
            print("Error: Bad input, use 'y' for yes or 'n' for no")
        except KeyboardInterrupt:
            return True

def check_victory():# Return 1 if Table is full, 2 if someone won otherwise Return 0
    if no_more_space(): return 1
    elif check_combi(): return 2
    return 0

def print_when_cell_full(unvalid_position):# Print message if cell is full
    if unvalid_position == True:
        print("\33[1;35m\nThis cell is full!\nPlay again:\n\33[0m")
        print_table()
        return True
    return False

def modif_in_table(l, c, player):# If the cell is empty Return False otherwise Return True
    if table[l][c] == " ": table[l][c] = player
    else: return True
    print_table()
    return False

def value_picked(player, type):# Loop while input is not an int or is out of range [0:3] then Return the value-1
    loop = True
    while loop:
        try:
            value = int(input(f"Which {type} have you picked?: "))
            while check_input_value(value) != 0:
                print(f"Error: {type} value must be between 1 and 3 included")
                print(f"Player {player}:")
                value = int(input(f"Which {type} have you picked?: "))
            loop = False
        except ValueError:
            print(f"Error: {type} value must be an Int type")
            print(f"Player {player}:")
            loop = True
        except KeyboardInterrupt: exit(0)
    return value-1

def player(type):# While nobody won, still playing
    if not(no_more_space() or check_combi()):
        print(f"Player {type}:")
        return print_when_cell_full(modif_in_table(value_picked(type, "Line"), value_picked(type, "Column"), type))

def game():# Player X move then Player O move till you can't play or someone won
    print_table()
    X_turn = True
    O_turn = True
    while 1:
        if X_turn:
            if player("\33[31mX\33[0m"):
                O_turn = False
            else:
                O_turn = True
                X_turn = False
        whowon = check_victory()
        if whowon != 0: return whowon
        if O_turn:
            if player("\33[34mO\33[0m"):
                X_turn = False
            else:
                X_turn = True
                O_turn = False
        whowon = check_victory()
        if whowon != 0: return whowon

def init():
    while 1:
        whowon = game()
        if whowon == 1:
            if again_or_not("Nobody won! Do you want to play again?[y/n]:"): return 0
        elif whowon == 2:
            if again_or_not("Do you want to play again?[y/n]:"): return 0
        else: return 0

score = Score(playerX=0, playerO=0)
print("\33[1;4;32;100mWelcome to Tic Tac Toe!\33[0m")
init()

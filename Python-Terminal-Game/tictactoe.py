ttt_ply_rnd = 0.0 
ttt_glst = ['1','2','3','4','5','6','7','8','9']

#start in-progress
class Game:
    board = []
    rcount_game = 0
    def __init__(self):
        pass

    def update(self, ply_ipt, id):
        if id == 1:
            Game.board[ply_ipt-1] = "X"
# end in-progress

def upd_game(lst):
    # if len(lst) % 3 == 0:
    #    print("Teilbar durch 3! Länge: " + str(len(lst)))
    print(lst[0:3])
    print(lst[3:6])
    print(lst[6:9])

def ttt_update(player, player_input, lst):
    if player == 1:
        lst[player_input-1] = "X"
    else:
        lst[player_input-1] = "O"

print("""
    TTTTTTTTT III    CCCCCC     TTTTTTTTT   AAAA      CCCCCC     TTTTTTTTT  OOOOOO   EEEEEE
       TTT    III   CCC            TTT     AA  AA    CCC            TTT    OO    OO  EEE
       TTT    III  CCC             TTT    AA    AA  CCC             TTT    00    00  EEEEE
       TTT    III   CCC            TTT    AA----AA   CCC            TTT    OO    OO  EEE
       TTT    III    CCCCCC        TTT    AA    AA    CCCCCC        TTT     OOOOOO   EEEEEE
""")
print("")
print("This is a simple 2 Player Tic-Tac-Toe Game. Each Player will be asked for a number from 1 to 9.")
print("")

upd_game(ttt_glst)

while ttt_ply_rnd != 4.5:
    ply_inpt = 0
    # Player 1:
    player1 = input("Choose a number, player 1: ")
    while player1.isdigit() == False:
        player1 = input("Choose a number between 1 and 9, player 1: ")
    ply_inpt = int(player1)
    ttt_update(1, ply_inpt, ttt_glst)
    upd_game(ttt_glst)
    # Rounds counter +0.5
    ttt_ply_rnd += 0.5
    # Player 2:
    if ttt_ply_rnd < 4.0:
        player2 = input("Choose your number, player 2: ")
        while player2.isdigit() == False:
            player2 = input("Choose a number between 1 and 9, player 1: ")
        ply_inpt = int(player2)
        ttt_update(2, ply_inpt, ttt_glst)
        upd_game(ttt_glst)
        # Rounds counter +0.5
        ttt_ply_rnd += 0.5

print("Game End")

# Open to develop:
# Add function to identify the winner.
# Add check to prevent players from playing a number twice.
# Replacing game function by a class



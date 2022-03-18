# Final Project of the module "CS101: Introduction to Programming" from the Codecademy Computer Scienc course.
# Coded by Florian Langguth

# Funktion für das Spiel
# In einer Liste wird die vom Spieler gegebene Zahl mit X oder O ersetzt.
# Spieler 1 ist X und Spieler 2 ist O
# Das Spiel ist zu Ende, wenn 9 Runden gespielt wurden.

ttt_ply_rnd = 0.0 
ttt_glst = ['1','2','3','4','5','6','7','8','9']

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
    print(ttt_ply_rnd)

print("Game End")

# Add function to identify the winner.



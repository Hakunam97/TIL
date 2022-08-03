# Get input from player(events) -> Update the game based off the player's actions -> Draw the Game's images on the screen => 다시 처음으로 : Game Loop 

from game import Game   # game.py에서 class game() 불러오기

g = Game()

# two loop
# 먼저 outer loop
while g.running:
    g.curr_menu.display_menu()
    g.game_loop()   # game.py에서 불러오기
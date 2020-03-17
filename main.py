from board import Board 
from player import Player
from tools import typewriter, player_winning
import copy

player_1 = Player(1)
player_2 = Player(2)

def main():
    typewriter('Generating board...\n')
    player_1.s_board.generate()
    player_2.s_board.generate()
    player_1.e_board.board = player_2.s_board.board
    player_2.e_board.board = player_1.s_board.board

    while True:
        player_1.make_step()
        player_2.make_step()
    
if __name__ == '__main__':
    main()
from board import Board
from tools import typewriter
from my_exception import Wrong_move, Hit_move, Destroy_move

class Player (object):
    def __init__(self, id):
        typewriter('Enter player ' + str(id)  + ' name: ')
        self.name = input()
        self.id = id
        self.s_board = Board()
        self.e_board = Board()
    
    def make_step(self):
        print('Your board: ')
        self.s_board.show_own_board()
        print('Enemy board: ')
        self.e_board.show_enemy_board()

        step_status = True

        while step_status:
            step = input(self.name + ', enter attack point (9C, 3A...): ')

            while not self.check_input(step):
                print('Error! Incorrect input.')
                step = input(self.name + ', enter attack point (9C, 3A...): ')

            try:
                self.e_board.make_step(int(step[:-1]) - 1, ord(step[-1]) - 65)
                step_status = False
            except Wrong_move as ex:
                print(ex)
            except Hit_move as ex:
                self.e_board.show_enemy_board()
                if self.e_board.winning_arrangement():
                    print('You won!')
                    exit(0)
                print(ex)
            except Destroy_move as ex:
                self.e_board.show_enemy_board()
                if self.e_board.winning_arrangement():
                    print('You won!')
                    exit(0)
                print(ex)

    def check_input(self, step):
        if len(step) == 2:
            if step[0].isdigit():
                if int(step[0]) not in range(1, 11):
                    return False
            else:
                return False
            if step[1].isalpha():
                if step[1] not in 'ABCDEFGHIJ':
                    return False
            else:
                return False
        elif len(step) == 3:
            if step[0].isdigit() and step[1].isdigit():
                if step[0] != '1' or step[1] != '0':
                    return False
            else:
                return False
            if step[2].isalpha():
                if step[2] not in 'ABCDEFGHIJ':
                    return False
        else:
            return False
        return True

if __name__ == '__main__':
    print('You turned on this module directly')
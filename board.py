import random

class Board:
    def __init__(self):
        self.board = [0] * 10
        for i in range(10):
            self.board[i] = [0] * 10

    def set_ship(self, coordinates):
        """
        setting ship on the board, excluding its borders
        :input coordinates: - list of coordinates (i, j) of ship points on border
        """

        for i, j in coordinates:
            self.board[i][j] = 2
        
        for i, j in coordinates:
            if j != 9:
                if self.board[i][j + 1] != 2:
                    self.board[i][j + 1] = 1
                if i != 0:
                    if self.board[i - 1][j + 1] != 2:
                        self.board[i - 1][j + 1] = 1
                if i != 9:
                    if self.board[i + 1][j + 1] != 2:
                        self.board[i + 1][j + 1] = 1
            
            if j != 0:
                if self.board[i][j - 1] != 2:
                    self.board[i][j - 1] = 1
                if i != 0:
                    if self.board[i - 1][j - 1] != 2:
                        self.board[i - 1][j - 1] = 1
                if i != 9:
                    if self.board[i + 1][j - 1] != 2:
                        self.board[i + 1][j - 1] = 1

            if i != 0:
                if self.board[i - 1][j] != 2:
                    self.board[i - 1][j] = 1

            if i != 9:
                if self.board[i + 1][j] != 2:
                    self.board[i + 1][j] = 1

            

    def get_possible_pos(self, ship_len):
        """
        returns possible positions for ship of size = size
        :input ship_len:    ship size
        :return:            list of possible coordinates
        """

        pos = list()

        for i in range(10):
            for j in range(ship_len, 11):
                #print(self.board[i][j - ship_len:j])   # получили значения клеток для корабля
                if 1 not in self.board[i][j - ship_len:j] and 2 not in self.board[i][j - ship_len:j]:
                    tmp_pos = list()
                    if ship_len != 1:
                        for k in range(ship_len):
                            tmp_pos.append((i, j - ship_len + k))
                    else:
                        tmp_pos = list()
                        tmp_pos.append((i, j - ship_len))
                    if tmp_pos not in pos:
                        pos.append(tmp_pos)

        for j in range(10):
            for i in range(10 - ship_len + 1):
                tmp = list()
                for k in range(ship_len):
                    tmp.append((i + k, j))

                is_free = True

                for m, n in tmp:
                    if self.board[m][n] == 1 or self.board[m][n] == 2:
                        is_free = False
                
                if is_free and tmp not in pos:
                    pos.append(tmp)
        return pos
            
    def generate_board(self):
        """ 
        generating board
        2 - ship
        1 - engaged
        :return:    matrix 10x10
        """
        
        for ship_len in range(1, 5):
            for count in range(5 - ship_len):
                possible_pos = self.get_possible_pos(ship_len)
                new_ship = random.choice(possible_pos)
                self.set_ship(new_ship)
                print(new_ship)
        
    def show_board(self):
        """
        printing board
        """
        print('-----------------------------------------')
        for i in self.board:
            print('|', end=' ')
            for j in i:
                if j != 0:
                    if j == 1:
                        print('O', '|', end = ' ')
                    elif j == 2:
                        print('#', '|', end=' ')
                    else:
                        print(' ', '|', end=' ')
                else:
                    print(' ', '|', end=' ')
            print('\n-----------------------------------------')
    
    def make_step(self):
        pass
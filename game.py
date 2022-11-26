import sys
from time import sleep

class Game:
    
    def __init__(self):
        self._board = []
            
    def createBoard(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self._board.append(row)
    
    def _showBoard(self):
        for i in self._board:
            print('\t\t    ', i)
        
    @classmethod
    def location(cls, loc: int) -> int:
        if loc >= 1 and loc <= 3:
            board_row = 0
        elif loc >= 4 and loc <= 6:
            board_row = 1
        else: 
            board_row = 2
        return board_row
    
    def _play(self, char) -> bool:
        input_ = input('Choose a number between 1-9: ')
        if input_ == 'q':
            print('Game has been terminated.')
            sys.exit()
        elif int(input_) > 9 or int(input_) < 1:
            raise IndexError('Input is out of range')
        else:
            input_ = int(input_)
            board_row = Game.location(input_)
            idx = (input_  % 3) - 1 if (input_ % 3) - 1 != 0 else (input_ - 1) % 3 
            if self._board[board_row][idx] != '-':
                raise IndexError('''Current position has already been marked.
Choose an appropriate location''')
            self._board[board_row][idx] = char
            return self._checkWinner(board_row, char, idx)
    
    def _checkWinner(self, board_idx, char, idx) -> bool: 
        point = self._board[board_idx]
        coord = self._board
        if (point[0] == point[1] == point[2]):
            self._won(char)
            sys.exit()
        elif (coord[0][idx] == coord[1][idx] == coord[2][idx] == char):
            self._won(char)
            sys.exit()
        elif (coord[0][0] == coord[1][1] == coord[2][2] == char):
            self._won(char)
            sys.exit()
        elif (coord[0][2] == coord[1][1] == coord[2][0] == char): 
            self._won(char)
            sys.exit()
        return True
    
    def turns(self):
        print('''======================= TIC TAC TOE GAME =======================''')
        print('Press \'q\' to quit.')
        self._showBoard()
        print('\n1st Player\'s Turn:')
        output = self._play('X')
        while output != False:
            self._showBoard()
            print('\n2nd Player\'s Turn:')
            output = self._play('O')
            self._showBoard()
            output = self._play('X')
    
    def _won(self, char):
        for i in range(20):
            print('*' * i)
            sleep(0.1)
        print(f'''======================= {char} HAS WON! =======================''')
        sleep(0.4)
        print('\n\n')
        self._showBoard()
        sleep(0.4)
        print('\n\n')
        print(f'''======================= {char} HAS WON! =======================''')


game = Game()
game.createBoard()
game.turns()
# -*- coding: utf-8 -*-
"""
Created on Tue May  4 16:21:44 2021

@author: nki
"""

import numpy as np
import re
from itertools import cycle

class Board:
    def __init__(self, xdim=10, ydim=10, ships=range(1,6)):
        self.x, self.y = xdim, ydim
        self.board = np.matrix(np.zeros((self.y, self.x)), dtype=np.int32)
        self.ships = ships
        self.setup()

    def setup(self):
        for ship in self.ships:
            incomplete = True
            while incomplete:
                try:
                    direction = np.random.choice(('horizontal', 'vertical'))
                    xi = np.random.randint(0, self.x - ship if direction=='horizontal' else self.x)
                    yi = np.random.randint(0, self.y - ship if direction=='vertical' else self.y)
                    self.insert_battleship(xi, yi, length=ship, direction=direction)
                    incomplete = False
                except AssertionError as e:
                    print(e)

    def get_random(self):
        direction = np.random.choice(('horizontal', 'vertical'))
        xi = np.random.randint(0, self.x - ship if direction=='horizontal' else self.x)
        yi = np.random.randint(0, self.y - ship if direction=='vertical' else self.y)
        return xi, yi, direction

    def guess(self, x, y):
        assert x <= self.x
        assert y <= self.y
        self.board[x,y] = -1 if self.board[x,y] > 0 else -2



    def __getitem__(self, item):
        return self.board.__getitem__(item)

    def __setitem__(self, item, value):
        self.board[item] = value


    def __repr__(self):
        rep = re.sub('(?<!\d|-)\d{1,}', '*', str(repr(self.board))).replace('-1',' ▲').replace('-2',' .')
        return re.sub(',| |[a-z]|\(|\[|\]|\)', '', rep).replace('-1',' X').replace('-2',' .')

    def insert_battleship(self, x, y, length=5, direction='horizontal'):
        assert 1 <= length <= 5, f'Length must be in (1, 2, 3, 4, 5)'
        assert direction in ('horizontal', 'vertical')
        if direction == 'horizontal':
            assert x + length <= self.x
        elif direction == 'vertical':
            assert y + length <= self.y
        x_sel, y_sel = (range(x,x+length), y) if direction=='horizontal' else (x, range(y,y+length))
        assert self.board[x_sel,y_sel].sum() == 0
        self.board[x_sel,y_sel] = length




class Battleship:
    def __init__(self, *players):
        self.players = players
        self.player_iterator = cycle(self.players)
        self.current_player = None
        [self.next_player() for _ in range(np.random.randint(1,3))][-1]
        self.setup()
        # self.game()

    def setup(self):
        self.boards = {}
        for player in self.players:
            self.boards[player] = Board()

    def next_player(self):
        self.current_player = next(self.player_iterator)
        return self.current_player

    def isvalid(self, guess):
        if isinstance(guess, str) and ' ' in guess and len(guess.split()) == 2 and guess.split()[0].isdigit() and guess.split()[1].isdigit():
            return True
        return False

    def game(self):
        while any([board[:,:].max() > 0 for board in self.boards.values()]):
            print(chr(27) + "[2J")
            prev_player, player = self.current_player, self.next_player()
            board = self.boards[prev_player]
            print(player)
            print(board)
            guess = ''
            while self.isvalid(guess) is False:
                try:
                    guess = input(f"{self.current_player}'s guess X? Y?: ")
                except Exception as e:
                    print(e)
            if guess == 'q':
                break
            x, y = guess.split()
            x, y = int(x), int(y)
            board.guess(y, x)
            print(board)
            input('Done?')





if __name__ == '__main__':
    b = Board()
    # b.insert_battleship(0, 5, length=5, direction='vertical')
    bs = Battleship('NK', 'Hannibal')
    bs.game()
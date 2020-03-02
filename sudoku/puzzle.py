from collections import deque
from sys import intern
import re
from time import sleep

class Puzzle:

    pos = ""

    goal = ""

    def __init__(self, pos=None):
        if pos: self.pos = pos
        
    def __repr__(self):
        return repr(self.pos)
        
    def canonical(self):
        return repr(self)

    def isgoal(self):
        return self.pos == self.goal
    
    def __iter__(self):
        if 0: yield self
    
    def solve(self, depthFirst=False):
        queue = deque([self])
        trail = {intern(self.canonical()): None}
        solution = deque()
        load = queue.append if depthFirst else queue.appendleft
        
        while not self.isgoal():
            for m in self:
                sleep(.1)
                print(m)
                c = m.canonical()
                if c in trail:
                    continue
                trail[intern(c)] = self
                load(m)
            self = queue.pop()
        
        while self:
            solution.appendleft(self)
            self = trail[self.canonical()]
        return list(solution)


class LeftToRight(Puzzle):
    pos  = [1,0,0,0,0]
    goal = [0,0,0,0,1]
    
    def __iter__(self):
        for move in range(2):
            pos = deque(self.pos)
            pos.rotate(-1) if move else pos.rotate()
            yield LeftToRight(pos=list(pos))
        
        
p = LeftToRight()
results = p.solve()
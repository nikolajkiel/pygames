# from collections import deque
# from sys import intern
# import re

# class Puzzle:

#     pos = ""                    # default starting position

#     goal = ""                   # ending position used by isgoal()

#     def __init__(self, pos=None):
#         if pos: self.pos = pos

#     def __repr__(self):         # returns a string representation of the position for printing the object
#         return repr(self.pos)

#     def canonical(self):        # returns a string representation after adjusting for symmetry
#         return repr(self)

#     def isgoal(self):
#         return self.pos == self.goal

#     def __iter__(self):         # returns list of objects of this class
#         if 0: yield self

#     def solve(pos, depthFirst=False):
#         queue = deque([pos])
#         trail = {intern(pos.canonical()): None}
#         solution = deque()
#         load = queue.append if depthFirst else queue.appendleft

#         while not pos.isgoal():
#             for m in pos:
#                 c = m.canonical()
#                 if c in trail:
#                     continue
#                 trail[intern(c)] = pos
#                 load(m)
#             pos = queue.pop()

#         while pos:
#             solution.appendleft(pos)
#             pos = trail[pos.canonical()]

#         return list(solution)


#####

from numpy import matrix as m

grid = m([[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]])

def possible(row, col, n):
    for i in range(9):
        if grid[row,i] == n or grid[i,col] == n:
            return False
    row0 = row//3*3
    col0 = col//3*3
    for i in range(3):
        for j in range(3):
            if grid[row0+i,col0+j] == n:
                return False
    return True


def solve(grid):
    for row in range(9):
        for col in range(9):
            if grid[row,col] == 0:
                for n in range(1,10):
                    if possible(row,col,n):
                        grid[row,col] = n
                        solve(grid)
                        grid[row,col] = 0
                return
    print(grid)

if __name__ == '__main__':
    solve(grid)
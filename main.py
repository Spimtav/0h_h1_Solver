#main.py
#Maximillian Tinati
#February 2, 2015
"""Script to run the 0h_h1 solver by instantiating a board and solver."""

import board
import local_solver

if __name__ == "__main__":
  b= board.Board(4)
  s= local_solver.LocalSolver(b)

  print s.board.matrix

  s.solve()
  s.printSolution()

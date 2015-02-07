#solver.py
#Maximillian Tinati
#February 2, 2015
"""Template class for all solvers."""

import board

class Solver(object):
  """Class solver represents a template class for a solver of a game of
       0h_hi.  Contains stubs for methods needed by all solvers.
     Data Members:
       board: an instance of class <Board>."""

  def __init__(self, board, algo):
    """Constructor: initializes an instance of class Solver.
       Precondition: board is a valid instance of class Board,
         algo is a string representing a valid solving algorithm."""
    self.board= board
    self.algo= algo
    self.iterations= 0
  
  def solve(self):
    """Solves the board in self.board and updates its self.matrix."""
    pass
  
  def printSolution(self):
    """Prints the completed board using ANSI terminal coloring."""
    pass

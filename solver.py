#solver.py
#Maximillian Tinati
#February 2, 2015
"""Template class for all solvers."""

class Solver(object):
  """Class solver represents a template class for a solver of a game of
       0h_hi.  Contains stubs for methods needed by all solvers.
     Data Members:
       board: an instance of class <Board>."""

  def __init__(self, board):
    """Constructor: initializes an instance of class Solver.
       Precondition: board is a valid instance of class Board."""
    self.board= board
  
  def solve(self):
    """Solves the board in self.board and updates its self.matrix."""
    pass
  
  def printSolution(self):
    """Prints the completed board using ANSI terminal coloring."""
    pass

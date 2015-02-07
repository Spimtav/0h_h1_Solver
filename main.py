#main.py
#Maximillian Tinati
#February 2, 2015
"""Script to run the 0h_h1 solver by instantiating a board and solver."""

import board
import local_solver

#List of implemented algorithms to choose from:
ALGO_LIST= ["hill_climbing"]


#Useful functions for input
def printAlgos():
  """Prints all algorithms in <ALGO_LIST> neatly, one per line."""
  print "Available algorithms:"
  for i in ALGO_LIST:
    print "  " + i


def chooseAlgo():
  """Returns: string containing a valid algorithm from <ALGO_LIST>.
     Note: asks user for input."""
  print ""
  printAlgos()
  algo= raw_input("Choose an algorithm from the above list: ")
  if algo not in ALGO_LIST:
    print "That is not a valid choice."
    chooseAlgo()
  else:
    return algo


def chooseSize():
  """Returns: int >= 4.
     Note: asks user for input."""
  print ""
  size= raw_input("Pick a board size (an integer >= 4): ")
  if not size.isdigit():
    print "That is not a valid integer."
    chooseSize()
  elif int(size) < 4:
    print "That is not an integer > 4."
  else:
    return int(size)


if __name__ == "__main__":
  size= chooseSize()
  algo= chooseAlgo()
  b= board.Board(size)
  s= local_solver.LocalSolver(b, algo)
  s.solve()
  s.printSolution()

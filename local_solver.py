#local_solver.py
#Maximillian Tinati
#February 2, 2015
"""Class that solves an 0h_h1 game using local search techniques."""

import random, sys
import solver, board

class LocalSolver(solver.Solver):
  """Class to solve a game of 0h_h1 using local search strategies."""
  
  def __init__(self, board, algo):
    """Initialize the solver using parent class method.
       Data Members:
         board: an instance of class Board to be solved.
         algo: string representing the algorithm to be used to solve.
         iterations: int for number of steps the algo takes to reach
           a solution."""
    super(LocalSolver, self).__init__(board, algo) 

  def fillBoard(self):
    """Randomly fill the empty squares in <self.board>."""
    for row in self.board.matrix:
      for i in range(self.board.size):
        if row[i] == board.EMPTY:
          row[i]= random.choice([board.RED, board.BLUE])

  def hillClimb(self):
    """Attempts to solve the board using a hill climbing tactic (ie. a 
         greedy local search).  Mostly as a baseline for a later simulated
         annealing implementation that will def be better.
       Returns: True if an improvement was found and made; False otherwise"""
    #Pick random square, see if color change will improve it IF IT"S MUTABLE
    #IF doesnt improve, rem from list and try diff square.
    #Generate list of mutable squares and choose a random one to improve
    pre_score= self.board.score()
    post_score= sys.maxint
    l= [(x,y) for y in range(self.board.size) for x in range(self.board.size) if self.board.mutable[x][y]]
    while len(l) > 0 and not self.board.isSolved():
      squ= random.choice(l)
      self.board.switchColor(squ)
      post_score= self.board.score()
      if post_score > pre_score:
        l.remove(squ)
        self.board.switchColor(squ)
      else:
        break
    if len(l) > 0 or (len(l) == 0 and (post_score < pre_score or self.board.isSolved())):
      return True
    else:
      return False

  def algoStep(self):
    """Performs a single step of a local search algorithm, according to 
         the algorithm specified in <self.algo>."""
    if self.algo == "hill_climbing":
      self.hillClimb()

  def solve(self):
    """Attempts to solve the given 0h_h1 board using local search tactics.
         All algorithms follow this basic format:
           1)Randomly fill board.
           2)Make local modification to progress to a sol'n.
           3)Repeat 2) until sol'n (or local extrema) found."""
    self.fillBoard() #Step 1
    iterations= 0
    move_made= True
    #Step 2
    while move_made:
      self.iterations+= 1
      move_made= self.algoStep() 
      if self.board.isSolved():
        break
      print "Number of iterations: " + str(self.iterations)
    #Step 3: Print either the sol'n or an error message if failed to find one
    if self.board.isSolved():
      print "Success!"
      print "The algorithm found a solution in " + str(self.iterations) + " iterations."
      print "Here is the solved board."
      self.printSolution()
    else:
      print "The chosen algorithm failed to find a solution after " + str(self.iterations) + " iterations."
      print "Here is the closest it got:"
      self.printSolution()

  def printSolution(self):
    """Prints the solved board in nice ANSI color format."""
    print self.board.matrix

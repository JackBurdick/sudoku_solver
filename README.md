# Diagonal Sudoku Solver

### Strategy: Constraint Propagation
> Constraint propagation is used to solve the naked twins problem by
> _constraining_ (reducing) our problem set -- in this case, the number of options
> available in each box.  The term `naked twins` refers to pairs of two numbers,
> in the sudoku puzzle, that are within the same unit (same row | same column | same 3x3)
> (or diagonal, depending on the problem).  However, the naked twins principal 
> can be generalized -- as done in the included solution -- to include groups larger
> than only 2.  Constraint propagation is also used to solve the diagonal sudoku 
> problem by further constraining the problem's potential solutions for certain 
> units; in this case, the two included units are the diagonals from the
> upper left to lower right (A1 -> I9) and the diagonal from the upper right to 
> the lower left (A9 -> I1).


### Code
* `solution.py`
    * Solution script.
* `solution_test.py`
    * Test the solution by executing `python solution_test.py`.
* `PySudoku.py`
    * Code for visualizing your solution.
    * to visualize the attempts, install pygame [here](http://www.pygame.org/download.shtml) then run `python solution.py`
* `visualize.py`
    * Code for visualizing the solution (attempt by attempt).

### Resources
* Udacity [materials](https://classroom.udacity.com/nanodegrees/nd889/)

# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
> A: Constraint propagation is used to solve the naked twins problem by
> _constraining_ (reducing) our problem set -- in this case, the number of options
> available in each box.  The term `naked twins` refers to pairs of two numbers
> in the sudoku puzzle that are within the same unit (same row | same column | same 3x3)
> (or diagonal, depending on the problem).  However, the naken twins principal 
> can be generalized -- as done in the included solution -- to include groups larger
> than only 2.

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
> A: Simmilar in principal to question 1, constraint propagation is used to solve
> the diagonal sudoku problem by further constraining the problem potential solutions
> for certain units. In this case, the two included units are the diagonals from the
> upper left to lower right (A1 -> I9) and the diagonal from the upper right to 
> the lower left (A9 -> I1).


##### Pygame
Pygame is used for attempt visualization.
> please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code
* `solution.py`
    * Solution script.
* `solution_test.py`
    * Test the solution by executing `python solution_test.py`.
* `PySudoku.py`
    * Code for visualizing your solution.
* `visualize.py`
    * Code for visualizing the solution (attempt by attempt).

### Resources
* Udacity [materials](https://classroom.udacity.com/nanodegrees/nd889/)
* GitHub [Repo](https://github.com/mghods/AIND-Sudoku)
    * Read for comparison. Inspiration for reverse dictionary -> list creation
* [Slack](https://ai-nd.slack.com)

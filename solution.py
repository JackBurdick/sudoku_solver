assignments = []

# set up
rows = 'ABCDEFGHI'
cols = '123456789'
def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [s+t for s in A for t in B]
boxes = cross(rows, cols)
row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
unitlist = row_units + column_units + square_units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)


def assign_value(values, box, value):
    """
    Update values dictionary by assigning a value to a given box. 
    """

    # don't append actions that don't change any values
    if values[box] == value:
        return values

    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def naked_twins(values, n=2):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """
    # Find all instances of naked twins
    for unit in unitlist:
        #print(unit_val)
        rev_dict = {}
        # unit > ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9']
        for i in unit:
            #print(values[i], len(values[i]))
            if len(values[i]) == n:
                rev_dict.setdefault(values[i], list())
                rev_dict[values[i]].append(i)

        # if (rev_dict):
        #     print(rev_dict)
        #print(rev_dict)
        naked_group_list = [rev_dict[digits] for digits in rev_dict if len(rev_dict[digits]) == n]
        #print(naked_group_list)
        
        # eliminate naked_group values from peers
        for group in naked_group_list:
            # peers at the intersction of the naked_group's
            intersect_peers = peers[group[0]]
            for g in group:
                intersect_peers = intersect_peers & peers[g]

            for digit in values[group[0]]:
                # all digits w/in the group are the same,`0` in `group[0]` is 
                # selected since this group will always be present
                for box in intersect_peers:
                    if digit in values[box]:
                        values = assign_value(values, box, values[box].replace(digit, ''))
    
    return values



def grid_values(grid):
    """Convert grid string into {<box>: <value>} dict with '123456789' value for empties.

    Args:
        grid: Sudoku grid in string form, 81 characters long
    Returns:
        Sudoku grid in dictionary form:
        - keys: Box labels, e.g. 'A1'
        - values: Value in corresponding box, e.g. '8', or '123456789' if it is empty.
    """
    vals = []
    all_digits = '123456789'
    for c in grid:
        if c == '.':
            vals.append(all_digits)
        elif c in all_digits:
            vals.append(c)
    assert len(vals) == 81
    return dict(zip(boxes, vals))

def display(values):
    """
    Display the values as a 2-D grid.
    Input: The sudoku in dictionary form
    Output: None
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF':
            print(line)
    return

def eliminate(values):
    """Eliminate values from peers of each box with a single value.

    Iterate all boxes - eliminate boxes with a single value,
    from the set of values of all its peers.

    Args:
        values: Sudoku in dictionary form.
    Returns:
        Resulting Sudoku in dictionary form after eliminating values.
    """
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    for box in solved_values:
        digit = values[box]
        for peer in peers[box]:
            #values[peer] = values[peer].replace(digit,'')
            values = assign_value(values, peer, values[peer].replace(digit, ''))
    return values

def only_choice(values):
    """Finalize values that are the only choice for a unit.

    Iterate all units, assign the value boxes where a unit only has one value

    Input: Sudoku in dictionary form.
    Output: Resulting Sudoku in dictionary form after filling in only choices.
    """
    for unit in unitlist:
        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                values = assign_value(values, dplaces[0], digit)
    return values

def reduce_puzzle(values):
    stalled = False
    while not stalled:
        # check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])

        # implement strategies
        values = eliminate(values)
        values = only_choice(values)
        groups = [2,3]
        for i in groups:
            values = naked_twins(values, n=i)
        
        # check how many boxes have a determined value, and compare
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        stalled = solved_values_before == solved_values_after
        
        # sanity check, return False if there is a box with zero available values:
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values

def search(values):
    # reduce puzzle
    values = reduce_puzzle(values)
    if values is False:
        return False ## Failed earlier

    if all(len(values[s]) == 1 for s in boxes): 
        return values ## Solved!
   
    # choose an unfilled squares with the fewest possibilities
    n,s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
    
    # use recurrence to solve each resulting sudoku
    for value in values[s]:
        new_sudoku = values.copy()
        new_sudoku[s] = value
        attempt = search(new_sudoku)
        if attempt:
            return attempt

def solve(grid, DIAGONAL=False):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    global unitlist

    if DIAGONAL:
        unitlist += [['A1','B2','C3','D4','E5','F6','G7','H8','I9'],['A9','B8','C7','D6','E5','F4','G3','H2','I1']]

    values = grid_values(grid)
    values = search(values)
    return values


if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'


    vals = []
    vals.extend(diag_sudoku_grid)
    unsolved = dict(zip(boxes, vals))
    display(unsolved)

    print(2*"\n--------------------------------------------------")

    solved = solve(diag_sudoku_grid, DIAGONAL=True)
    display(solved)


    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')

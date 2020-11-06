'''
Software Carpentry, Fall 2020
Lazors project
Submitted by
Vamsi Reddy <vreddy17@jhu.edu>
Emad Mohammed Naveed <enaveed1@jhu.edu>
'''
# Import packages
from itertools import combinations
from PIL import Image, ImageDraw

class Input:
    '''
    This class handles reading and extraction of lazor test file information
    Step 1: Read the .bff extension files only.
    Step 2: Extract specific information about different blocks and positions
            [positions of (o, x), flexible and fixed blocks (A,B,C)]
    Step 3: Extract lazer positions, directions & points of intersections(POI)
    Step 4: Transformation of coordinates of lazors and POIs
    '''

    def __init__(self, file):
        '''
            The __init__ method will initialize the object’s state.
            Initializes the function of the class when
            an object of class is created.
            In this case, the file name of the lazor test file
            **Input Parameters**
                file: *str*
                    The filename to read and extract information
                    The filename to save the output image with solution
            **Returns**
                None
        '''
        self.filename = file
        # Initializing position variables
        self.x = 0
        self.y = 0

    def __call__(self):
        '''
        The __call__ method will read and extract the specific .bff file

        **Input Parameters**
            None
        **Returns**
            dataset1: *dict*
                The dictionary with following attributes
                size of the grid, lazors, points of intersection,
                blocks (A, B, C)
            dataset2: *dict*
                The dictionary with following attributes
                size of the grid, and individual lists of blocks
                and no-movement positions
        '''
        # If the file extension is not .bff file
        if not self.filename.lower().endswith('.bff'):
            raise SystemExit("Invalid File type, try with .bff files")
        # Initializing position variables and block list
        A, B, C = 0, 0, 0
        o_l, x_l, A_l, B_l, C_l, lazers, points = (
            [] for i in range(7))

        # Open the file with .bff extensions
        file = open(self.filename, 'r')
        # Read the information line by line
        lines = file.read().splitlines()
        # Defining the start and stop for extracting positions
        try:
            start = lines.index("GRID START")
            stop = lines.index("GRID STOP")
        except BaseException:
            raise SystemExit("No grid start or stop indicated in test file")
            # Iterating through each line to extract grid
        for line in lines[start + 1: stop]:
            # split by tab/space
            pos = line.split()
            # Within the grid
            # Position information appends to each list based
            # on the alphabet matching
            for i in range(0, len(pos)):
                if pos[i] == 'o':
                    o_l.append([i, self.y + 1])
                elif pos[i] == 'x':
                    x_l.append([i, self.y + 1])
                elif pos[i] == 'A':
                    A_l.append([i, self.y + 1])
                elif pos[i] == 'B':
                    B_l.append([i, self.y + 1])
                elif pos[i] == 'C':
                    C_l.append([i, self.y + 1])
                else:
                    continue
            self.y += 1
        self.x = i + 1

        # If no positions 'o' in the grid
        if len(o_l) == 0:
            raise SystemExit("No open positions to move the block")

        # Initalizing the grid
        grid = [o_l, x_l, A_l, B_l, C_l]
        # transforming the grid positions [x,y]
        grid_update = self.grid_transformation(grid)

        # After the grid
        for inputs in lines[stop + 1:]:
            # In case of lines with comments or empty line
            if inputs == "" or inputs[0] == '#':
                continue
            # Number of blocks
            else:
                # split by tab/space
                pos = inputs.split()
                if inputs[0] == 'A':
                    A = int(pos[-1])
                elif inputs[0] == 'B':
                    B = int(pos[-1])
                elif inputs[0] == 'C':
                    C = int(pos[-1])
                # Lazor positions and directions
                elif inputs[0] == 'L':
                    # Executes only if both the positions and
                    # direction of lazors is specified
                    try:
                        lazers.append([int(pos[1]), int(pos[2]),
                                       int(pos[3]), int(pos[4])])
                    except BaseException:
                        raise SystemExit(
                            "Position or direction not specified for lazors")
                # Points for Intersection
                elif inputs[0] == 'P':
                    try:
                        points.append([int(pos[1]), int(pos[2])])
                    except BaseException:
                        raise SystemExit(
                            "Invalid coordinates for intersection points")

        # if there are no blocks to move
        if A == 0 and B == 0 and C == 0:
            raise SystemExit("No blocks available to solve the lazor")
        # If no lazor info is provided
        elif len(lazers) == 0:
            raise SystemExit("No lazors info is provided in test file")

        # Transformation the positions of given lazors
        lazers, points = self.position_transformation(lazers, points)
        # Creating dictionaries with extracted information
        dataset1 = ({"Size": [self.x,
                              self.y],
                     "o_l": grid_update[0],
                     'Lazers': lazers,
                     'Points': points,
                     "A": A,
                     "B": B,
                     "C": C})
        dataset2 = ({"Size": [self.x,
                              self.y],
                     "x_l": grid_update[1],
                     "A_l": grid_update[2],
                     "B_l": grid_update[3],
                     "C_l": grid_update[4]})

        # closing the  .bff file
        file.close()
        return dataset1, dataset2

        def grid_transformation(self, lists):
        '''
        This function will transform the y-coordinates
        of the given lists

        **Input Parameters**
            lists: *list, int*
                The list with specific positions [x,y]
        **Returns**
            lists: *list, int*
                The updated grid system
        '''
        for listi in lists:
            for listj in listi:
                # Update y values
                listj[1] = self.y - listj[1]
        return lists

    def position_transformation(self, lazers, points):
        '''
        This function will transform the POIs and directions
        of the given lazors

        **Input Parameters**
            lazers: *lists*
                The positions and directions of lazors
            points: *lists*
                The positions of points of intersection

        **Returns**
            lazers: *lists*
                The updated positions and directions of lazors
            points: *lists*
                The updated positions of points of intersection
        '''
        for li in lazers:
            li[0] = 0.5 * li[0]
            li[1] = self.y - li[1] * 0.5
            li[2] = 0.5 * li[2]
            li[3] = - 0.5 * li[3]
        for pi in points:
            pi[0] = 0.5 * pi[0]
            pi[1] = self.y - pi[1] * 0.5
        return lazers, points

class Lazor:
    '''
        This class estimates all possible combinations to find the solution
        Step 1: Sorting A blocks in possible 'o' positions to get all
                combinations
        Step 2: With leftover 'o' positions, do similar combination search
                for B, C
        Step 3: Create possible combinations of A, B, C with available
                'o' positions and locked blocks within the grid
    '''

    def __init__(self, dataset1, dataset2):
        '''
        The __init__ method will utilize the dictionaries created from
        class Input and initialize all the extracted information as variables

        **Input Parameters**
            dataset1: *dict*
                The dictionary with following attributes
                size of the grid, lazors, points of intersection,
                and number of blocks (A, B, C)
            dataset2: *dict*
                The dictionary with following attributes
                size of the grid, individual lists of blocks
                and no-movement positions
        **Returns**
            None

        '''
        self.o_l = dataset1['o_l']
        self.size = dataset1['Size']
        self.lazers = dataset1['Lazers']
        self.points = dataset1['Points']
        self.A = dataset1['A']
        self.B = dataset1['B']
        self.C = dataset1['C']
        self.dataset2 = dataset2

    def __call__(self):
        '''
        The __call__ method will return the right combination
        of coordinates of different blocks

        **Input Parameters**
            None
        **Returns**
            sel_comb: *dict, list, int*
                The right combination of coordinates of different blocks
        '''
        # All possible combinations of A in 'o' positions
        o_lA = list(combinations(self.o_l, self.A))
        # For every A block
        for i_a in o_lA:
            # Sorting the available 'o' positions, A combinations
            o_l, a_comb = self.new_sort("a_comb", self.o_l, list(i_a))
            # Possible combinations of B with new o positions
            # (after A block is fixed)
            o_lB = list(combinations(self.o_l, self.B))
            # For every B block
            for i_b in o_lB:
                # Sorting the available 'o' positions, B combinations
                o_l, b_comb = self.new_sort("b_comb", self.o_l, list(i_b))
                # Possible combinations of C with new 'o' positions
                # (after A, B blocks fixed)
                o_lC = list(combinations(self.o_l, self.C))
                # For every C block
                for i_c in o_lC:
                    # Sorting the available 'o' positions, C combinations
                    o_l, c_comb = self.new_sort("c_comb", self.o_l, list(i_c))

                    # Selecting a set of different coordinates amongst
                    # all possible combinations
                    sel_comb = self.set_abc(
                        [a_comb, b_comb, c_comb], ['A', 'B', 'C'])

                    # Testing the selected combination under class Solution
                    test_comb = Solution(
                        sel_comb,
                        self.lazers,
                        self.points,
                        self.dataset2,
                        self.size)

                    # If true, return the right combination
                    # of coordinates of different blocks
                    if test_comb():
                        return sel_comb
                    # Else test the next possible combination
                    o_l, c_comb = self.rearrange(
                        c_comb, o_l, self.C, list(i_c), "C")
                o_l, b_comb = self.rearrange(
                    b_comb, o_l, self.B, list(i_b), "B")
            o_l, a_comb = self.rearrange(a_comb, o_l, self.A, list(i_a), "A")

    def set_abc(self, block_positions, name):
        '''
        This function will create a new dictionary with A, B, C
        combinations

        **Input Parameters**
            block_positions: *list, int*
                The list with positions of a specific block
            name: *list, int*
                The name of the specific block
        **Returns**
            sel_comb: *dict, list, int*
                An updated dictionary with A, B, C combinations
        '''
        sel_comb = {}
        for j in range(len(block_positions)):
            # Accessing each position
            block_position = block_positions[j]
            for i in block_position:
                # Creating a key, value pair
                sel_comb[(i[0], i[1])] = name[j]
        return sel_comb


class Solution:
    '''
        This class has functions to solve the lazor puzzle based on
        the generated combinations of blocks, lazors, points of intersection
        Criteria: List of points of intersection is empty

    '''

    def __init__(self, sel_comb, lazers, points, dataset2, size):
        '''

        The __init__ method will initialize the previously generated dictionaries,
        lazors' information, size of the grid etc.

        **Input Parameters**
            sel_comb: *dict*
                The dictionary with following attributes
                size of the grid, and blocks (A, B, C)
            lazers: *list, int*
                The list of lazor positions and directions
            points: *list, int*
                The list of positions of points of intersections
            dataset2: *dict*
                The dictionary with following attributes
                size of the grid, and individual lists of blocks
                (A,B.C) and no-movement positions
            size:*list, int*
                The size of the grid for the lazor
        **Returns**
            None

        '''
        self.size = size
        self.sel_comb = sel_comb
        self.lazers = lazers
        self.points = points
        self.x = 0
        self.y = 0
        self.vx = 0
        self.vy = 0
        self.A_l = dataset2['A_l']
        self.B_l = dataset2['B_l']
        self.C_l = dataset2['C_l']
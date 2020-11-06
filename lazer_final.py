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

class Lazor:
    '''
        This class estimates all possible combinations to find the solution
        Step 1: Sorting A blocks in possible 'o' positions to get all
                combinations
        Step 2: With leftover o positions, do similar combination search
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
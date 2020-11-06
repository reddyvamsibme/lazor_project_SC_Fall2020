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

    def set_abc(self, block_positions, name):
        
        sel_comb = {}
        for j in range(len(block_positions)):
            # Accessing each position
            block_position = block_positions[j]
            for i in block_position:
                # Creating a key, value pair
                sel_comb[(i[0], i[1])] = name[j]
        return sel_comb
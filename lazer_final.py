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
        
        self.o_l = dataset1['o_l']
        self.size = dataset1['Size']
        self.lazers = dataset1['Lazers']
        self.points = dataset1['Points']
        self.A = dataset1['A']
        self.B = dataset1['B']
        self.C = dataset1['C']
        self.dataset2 = dataset2
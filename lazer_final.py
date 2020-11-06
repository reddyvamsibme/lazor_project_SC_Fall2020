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
    
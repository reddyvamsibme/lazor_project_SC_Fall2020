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

def read():
	if not filename.lower().endswith('.bff'):
            raise SystemExit("Invalid File type, try with .bff files")
        # Initializing position variables and block list
        A, B, C = 0, 0, 0
        o_l, x_l, A_l, B_l, C_l, lazers, points = (
            [] for i in range(7))

        # Open the file with .bff extensions
        file = open(filename, 'r')
        # Read the information line by line
        lines = file.read().splitlines()
### Lazor Group Project
**Authors: Vamsi Reddy, Emad Mohammed Naveed**  
**Course: EN.540.635 “Software Carpentry”**  
**Johns Hopkins University, MD**

<p style='text-align: justify;'> This repository has the python code and test files that will automatically find solutions to the “Lazors” game on Android and iPhone. 
The code is documented and designed to be easy to extend. If you use it in your research, please consider citing this repository.
</p>

## Testfiles
The code is exclusively programmed for reading '.bff' files as input and extracting the necessary information. 
The directory [testfiles](https://github.com/reddyvamsibme/lazor_project_SC_Fall2020/tree/master/testfiles/) 
in this repository has 7 '.bff' files for getting trained. If you intend to use your own test file with
different extension, you need to make the following adjustments
   1. Comment the following code in __call__() of Class Input:  
   ```python
        # If the file extension is not .bff file
         if not self.filename.lower().endswith('.bff'):
            raise SystemExit("Invalid File type, try with .bff files")
   ```
    
## Installation
1. Clone this repository
    ```bash
    git clone https://github.com/reddyvamsibme/lazor_project_SC_Fall2020.git
    ```
2. Install dependencies
   ```bash
   pip3 install -r requirements.txt
   ```
3. Open lazor_final.py and change the file names with extensions, 
   if you wish apply the code on your custom file
4. Run lazor_final.py from the repository root directory
    ```bash
    python3 lazor_final.py
    ``` 
5. Redirect to the root folder and check the saved .png files for solutions

## Blocks and positions on lazor grid
* x = No block allowed
* o = Blocks allowed
* A = Fixed reflect block
* B = Fixed opaque block
* C = Fixed refract block

## Color Scheme - Solution
![alt text](https://github.com/reddyvamsibme/lazor_project_SC_Fall2020/blob/master/pics/color.png "Colors for specific blocks and positions")

## Code Architecture

* **Class Input**  
   This class handles reading and extraction of lazor test file information  
   + Step 1: Read the .bff extension files only.  
   + Step 2: Extract specific information about different blocks and positions 
   + Step 3: Extract lazer positions, directions & points of intersections(POI)  
   + Step 4: Transformation of coordinates of lazors and POIs

* **Class Lazor**  
   This class estimates all possible combinations to find the solution  
   + Step 1: Sorting A blocks in possible 'o' positions to get all
                combinations  
   + Step 2: With leftover o positions, do similar combination search
                for B, C  
   + Step 3: Create possible combinations of A, B, C with available
                'o' positions and locked blocks (A, B, C)

* **Class Solution**  
     This class has functions to solve the lazor puzzle
     + Criteria: Lazer intersection with given points 
     + Input: Possble combinations of blocks, lazors, points of intersection  
     + Handles the functions for refract, reflect, hitting the block, moving lazor, position and lazor encounters
         
 * **Class Visulization**  
    This class defines various operations for plotting the final solution for a given lazor test case  
    + Step 1: Creating a grid with blocks
    + Step 2: Assigning the colors as per the above color scheme
    + Step 3: Retracing the lazor path
    + Step 4: Draw the grid lines and intersection points
    + Step 5: Save the solution as .png file in the root file




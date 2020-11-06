---
layout: single
classes: wide
---

## Lazor Group Project
**Authors: Vamsi Reddy, Emad Mohammed Naveed**
**EN.540.635 “Software Carpentry”**

<p style='text-align: justify;'> This repository has the python code and test files that will automatically find solutions to the “Lazors” game on Android and iPhone
</p>

The code is documented and designed to be easy to extend. If you use it in your research, please consider citing this repository (bibtex below).
```bash
git clone https://github.com/reddyvamsibme/lazor_project_SC_Fall2020.git
```

## Installation
1. Clone this repository
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
5. Redirect to the root folder and check the saved .png files

** Blocks and positions on lazor grid**
x = no block allowed
o = blocks allowed
A = fixed reflect block
B = fixed opaque block
C = fixed refract block

![alt text](https://github.com/reddyvamsibme/lazor_project_SC_Fall2020/blob/master/pics/color.png "Colors for specific blocks and positions")

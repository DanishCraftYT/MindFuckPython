# MindFuck

MindFuck is a improved version of BrainFuck.

# 0. Overview

* [MindFuck](#mindfuck)<br>
* [Overview](#0-overview)<br>
* [Installing MindFuck](#1-installing-mindfuck)<br>
  [Creating Your First Script](#11-creating-your-first-script)<br>
  [Using MindFuck as a Module](#12-using-mindfuck-as-a-module)<br>
  [The MindFuck Compiler](#13-the-mindfuck-compiler)<br>
* [Features](#2-features)<br>
* [Documentation](#3-documentation)<br>
* [How The MindFuck Compiler Works](#4-how-the-mindfuck-compiler-works)<br>

# 1. Installing MindFuck

drag the `MindFuck.py` and the `Files.txt` file into a folder.<br>

### 1.1. Creating Your First Script

make a text file that ends in `.mfs`. make sure to copy the path to the script.<br>
now open the `Files.txt` file and paste the path to the script inside the file and save the file.<br>
now open the `MindFuck.py` file and type the line where the path to the script is (in the `Files.txt` file) into the console and hit enter.<br>
now your done. your script should run.<br>

### 1.2. Using MindFuck as a Module

go inside the `Modules` folder and find the file called `MindFuckModule.py`.<br>
drag the python script into the folder of your own python script.<br>
open your own python script and type `import MindFuckModule`.<br>
to run a MindFuck script call the function `run()` and pass the path to the MindFuck script through the function. example: `run(file_path)`.<br>

### 1.3. The MindFuck Compiler

to use the mindfuck compiler. you will need `py2exe`. use `pip install py2exe` in command prompt to install py2exe.<br>
after you have installed `py2exe`. open `MindFuckCompiler.py`.<br>
after opening the script it will ask you what file to compile in the `Files.txt` file. type the line where the path to the script is.<br>
then it will ask you if you want a icon for the exe file. either paste the file path the image file or type `no` to not use a icon.<br>
then it will start creating the .exe file. once it is done. it will ask you if you want to delete the `<script_name>.py` file.
this script contains the code for the .exe file. most of the time you don't need this file. for now. type `yes` to delete the file.<br>
now hit enter to exit the script. go into the `dist` folder to find the .exe file.

# 2. Features

* quality of life improvements to BrainFuck (added multiplication, division and more).
* compatible with BrainFuck code.
* has support for if statements.
* has unicode support.
* has a compiler.

# 3. Documentation

* [Text Documentation](Docs/Mind%20Fuck%20Text%20Docs.txt)<br>

# 4. How The MindFuck Compiler Works

the mindfuck compiler creates a new script. this script contains a list with all lines in a mindfuck script.<br>
the script also contains the mindfuck interpreter. this interpreter interprets the list that contains all the lines from a mindfuck script.<br>
then the mindfuck compiler compiles the script to a .exe file.<br>

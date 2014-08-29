# Android Logcat Filter (in Python) #


## Use case ##
You have a logcat exported to a text file and you want to filter out some of the irrelevant lines programmatically.


## Usage ##
1. Install Python 2 (and add to path).
2. Put `read-file.py` in the same directory as the text file.
3. Run the Python program.

There will then be an input required for file name, then filter string. When done with those two, a new text file will be created with `-filtered` appended.

Protip: Instead of having to input the file name and filter individually, they can be added as arguments via command line:

    python read-file.py test-file.txt test


## Limitations / TODOs ##
* Filters use only a basic String.contains(String); No regex.
* All filters are currently case-sensitive.
* This is only marketed for "Android Logcat" when it could actually be used for any file.


## Background ##
Problem: I had long exported logcat files to go through to figure out some bugs. Going through all of it by hand would be too arduous. Android DDMS is too limited.

Requirement (for me): I wanted to refresh myself in Python.

Solution: Create a text filter in Python.


## About ##
This project was a quick refresher on Python I/O and can be used as such. And, here's two of the main webpages that I used to help remember all the correct syntaxes:
* http://hetland.org/writing/instant-python.html
* http://www.stavros.io/tutorials/python/

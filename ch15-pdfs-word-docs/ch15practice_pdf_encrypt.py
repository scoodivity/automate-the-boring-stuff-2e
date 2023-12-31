#! python3

# Using the os.walk() function from Chapter 10, write a script that will 
# go through every PDF in a folder (and its subfolders) and encrypt the 
# PDFs using a password provided on the command line. Save each 
# encrypted PDF with an _encrypted.pdf suffix added to the original 
# filename. Before deleting the original file, have the program attempt 
# to read and decrypt the file to ensure that it was encrypted correctly.
# Then, write a program that finds all encrypted PDFs in a folder (and 
# its subfolders) and creates a decrypted copy of the PDF using a 
# provided password. If the password is incorrect, the program should 
# print a message to the user and continue to the next PDF.

import PyPDF2
import sys

from pathlib import Path

# TODO take sysargv password

# TODO using pathlib instead, find all PDFs in folder and recursively

# TODO encrypt PDFs using password in command line

# TODO test password before deleting original file and moving on to next file

# TODO make the mirror program to decrypt
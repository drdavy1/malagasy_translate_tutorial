"""
Simple python script. Execute it and see how it uses your Windows :)

Exercises:
1. This program prints a list of all files in this directory. Change it so the names are printed in separated lines:
'.git'
'.gitignore'
'1_os_operations.py'
...

"""


import os #library for doing stuff related to the operatin system

#Greeting
print("This is a simple script")
print("Fiovana farany")

currentDirectory = os.getcwd() #same as `dir` in windows and `pwd` in linux
print("We are in directory:", currentDirectory)
print("The following is a list of files in a current directory:")

ListOfDirs = os.listdir()
for dir in ListOfDirs:
    print(dir)

	
print("Here it ends")

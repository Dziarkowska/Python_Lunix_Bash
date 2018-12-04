
import os
import sys


def directory_tree(dir):
    dir_content = os.listdir(dir)
    for i in range(len(dir_content)):
        if os.path.isdir(dir + dir_content[i]):
            directory_tree(dir + dir_content[i])
        else:
            print(dir +"/"+ dir_content[i]) 

# uruchamiamy z commanda jako argument podajac sciezke do interesujacego nas folderu
# np. 5.py C:\Users\User\Documents\JPO
def main():
    dir = sys.argv[1]
    directory_tree(dir)

main()
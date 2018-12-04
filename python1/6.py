
import os
import sys

# uruchamiamy program w konsoli podajac nazwe pliku,
# w ktorym chcemy zmienic rozszerzenie jako argument.
# przykladowo w commandline: 6.py 2.JPG 
# tutaj akurat komenda dla windowsa "move",
# mozna zmienic na "mv", zeby dzialalo na linuxie

jpg_file = sys.argv[1]
png_file = jpg_file[:-3]+"png"

os.system("move " + jpg_file + " " + png_file)
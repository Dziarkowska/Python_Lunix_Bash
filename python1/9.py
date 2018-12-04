import re
import sys

file = "text.txt"
old_text=[]
new_text=[]

with open(file) as f:
	text = f.readlines()

for line in text:
	old_text.append(line)
	line = re.sub('sie','',line)
	line = re.sub(' i ','  ',line)
	line = re.sub('oraz','',line)
	line = re.sub('nigdy','',line)
	line = re.sub('dlaczego','',line)
	new_text.append(line)

print("Stary tekst:\n")
for line in old_text:
	print(line)

print("Nowy tekst:\n")
for line in new_text:
	print(line)
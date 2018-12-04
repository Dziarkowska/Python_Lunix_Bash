
with open ("text.txt", "r") as file_read:
	with open ('output.txt', 'w') as file_write:
		for line in file_read:
			file_write.write("z pliku wejsciowego: " + line)
print("done")
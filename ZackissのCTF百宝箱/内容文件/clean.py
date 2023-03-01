import os
import re

path = "./"

files = os.listdir(os.getcwd())
for file in files:
	if "md" in file and " " in file:
		# os.rename(file, )
		print(file)
		os.rename(file, file.split(" ")[0] + ".md")

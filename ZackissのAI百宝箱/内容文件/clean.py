import os
import re

path = "./"

files = os.listdir(os.getcwd())
for file in files:
	if ".md" in file and " " in file:
		# os.rename(file, )
		print(file)
		os.rename(file, file.split(" ")[0] + ".md")

for file in files:
	if ".md" in file:
		filename = file
		with open(filename, "r") as f:
			lines = f.readlines()

		# remove the first and third lines and modify the second line
		for i in range(len(lines)):
			if i+2 < len(lines):
				if "$$" in lines[i] and "$$" in lines[i+2].strip():
					content_line = lines[i+1].strip()
					if "      $$" in lines[i]:
						lines[i+1] = "      $$" + content_line + "$$"
					elif "    $$" in lines[i]:
						lines[i+1] = "    $$" + content_line + "$$"
					elif "  $$" in lines[i]:
						lines[i+1] = "  $$" + content_line + "$$"
					elif "$$" in lines[i]:
						lines[i + 1] = "$$" + content_line + "$$"
					lines.pop(i)
					lines.pop(i+1)
					print(content_line)

		# write the modified lines back to the file
		with open(filename, "w") as f:
			f.writelines(lines)
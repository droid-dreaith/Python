#assign importfie to the name of the text file that contains the security log file

import_file = "data/login.txt"

#use with statement and open() to import security log file and store it as a string
with open(import_file, "r") as file:
    text = file.read()
print(text.split())

#what is the purpose of split()?The split() method splits a string into a list. 
# You can specify the separator, default separator is any whitespace.
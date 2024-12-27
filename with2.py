# assign importfile to the name of the text file that contains the security log file
import_file = "login.txt"

# use with statement
# use open() to import security log file and store it as a string

try:
    with open(import_file, "r") as file:
        text = file.read()
    print(text)
except FileNotFoundError:
    print(f"The file {import_file} does not exist.")
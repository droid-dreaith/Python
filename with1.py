#assign importfile to the name of the text file that contains the security log file
import_file = "login.txt"

#we are using try and except to handle the error that occurs when the file does not exist
try:
#first line of the try block reads the contents of the file and assigns it to the variable log_data
    with open(import_file, "r") as file:
        log_data = file.read()
        
    #error handling code:
except FileNotFoundError:
    print(f"The file {import_file} does not exist.")
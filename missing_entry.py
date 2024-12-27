import_file = "data/login.txt"

#assign missingentry toa  log that was not recorded in the log file

missing_entry ="jrafael,192.168.243.140,4:56:27,2022-05-09"

#use open() to import security log file and store it as a string
#pass in "a" as the second argument to append the missing entry to the log file OR INDICATE THAT THE FILE IS BEING OPENED
with open(import_file,"a") as file:
    file.write("\n"+missing_entry)

#use open() w/parametyer "r" to import security log file for reading purposes
with open(import_file,"r") as file:
    text = file.read()
print(text)
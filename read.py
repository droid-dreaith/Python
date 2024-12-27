import_file = "allow_list.txt"

#assign REMOVE_LIST to a list of ip addresses that are no longer allowed  to access the restricted information

remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]
# Build `with` statement to read in the initial contents of the file
with open(import_file,"r") as file:
    #use ".read()" to read the imported file and store it ina variable named ip_address
    ip_addresses = file.read()
print(ip_addresses)
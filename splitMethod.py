import_file = "allow_list.txt"

#assign REMOVE_LIST to a list of ip addresses that are no longer allowed  to access the restricted information
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

# Build `with` statement to read in the initial contents of the file
with open (import_file, "r") as file:
    ip_addresses = file.read()
    
#use split() to convert ip addresses froma string to a list
ip_addresses = ip_addresses.split()
print(ip_addresses)
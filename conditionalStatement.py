import_file = "allowq_list.txt"

remove_list ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

# Build `with` statement to read in the initial contents of the file
with open(import_file,"r") as file:
    #use ".read()" to read the imported file and store it ina variable named ip_address
    ip_addresses = file.read()
ip_addresses = ip_addresses.split()

for element in ip_addresses:
    #build a conditional statement
    if element in remove_list:
        ip_addresses.remove(element)
print(ip_addresses)
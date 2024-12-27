import_file = "allow_list.txt"

remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

with open(import_file,"r")as file:
    
    #use read() to read the imported file and store it in a variable named ip_addresses
    ip_addresses = file.read()
    
#use split() to convert ip_addresses from a string to a list
ip_addresses = ip_addresses.split()

#build iterative statement
#name loop variable element
#loop through ip_addresses

for element in ip_addresses:
    #build conditional statement
    #if current element is in remove_list
    if element in remove_list:
        #then current element should be removed from ip_addresses
        ip_addresses.remove(element)
        
#convert ip_addresses back to a string so that it can be written into the text file
ip_addresses = " ".join(ip_addresses)

#build WITH statement to rewrite the original file
with open (import_file, "w") as file:
    #rewrite the file, replacing its contents with ip_addresses
    file.write(ip_addresses)
#build WITH statement to read the updated file
with open(import_file, "r") as file:
    #use read() to read the updated file and store it in a variable named ip_addresses
    text = file.read()
print(text)
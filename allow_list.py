#The next task you're responsible for is creating a text file. This text file should include a list of IP addresses that are allowed to access restricted information. Documenting this in a text file will help you communicate your findings to your security team.
#Start by creating a variable named import_file that stores the name of the file, which should be "allow_list.txt".
#You're also given a variable named ip_addresses that stores a string containing the IP addresses that are allowed.
#Run the code to display the two variables and explore what they contain. Be sure to replace the ### YOUR CODE HERE ### with your own code before you run the following cell.

import_file = "data/allow_list.txt"

#assign ip adresses to a list of IP ADDRESSES THAT ARE ALLOWED TO ACCESS
ip_addresses = "192.168.218.160 192.168.97.225 192.168.145.158 192.168.108.13 192.168.60.153 192.168.96.200 192.168.247.153 192.168.3.252 192.168.116.187 192.168.15.110 192.168.39.246"

print(import_file)
print(ip_addresses)
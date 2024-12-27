#define a function named "update_file" that takes 2 parameters and combines the steps you wirtten in this lab leading up to this
def update_file(import_file,remove_list):
    with open(import_file,"r") as file:
        ip_addresses = file.read()
    ip_addresses = ip_addresses.split()
    for element in ip_addresses:
        if element in remove_list:
            ip_addresses.remove(element)
    ip_addresses = " ".join(ip_addresses)
    with open(import_file, "w") as file:
        file.write(ip_addresses)
  
  
  #What are the benefits of incorporating the algorithm into a single function?
  #Incorporating the algorithm into a single function helps organize the code and make it reusable. If you want to execute the algorithm more than once, all you have to do is call the function that contains it.
  
  
  
# Description: This program takes a string as input and returns the reverse of the string.  
def reverse_string(s):
    return s[::-1]

if __name__ == "__main__":
    s_string = "tapat"
    print("Original String:", s_string)
    print("Reversed String:", reverse_string(s_string))
    print("\n")
    
if __name__ == "__main__":
    s_string = "make things more meaningful and be addicted to learning"
    print("Original String:", s_string)
    print("Reversed String:", reverse_string(s_string))
    print("\n")
    
#reverse the string of what the user input's
user_input = input("Hello User! Enter a string to reverse:")
print("Reversed User Input:", reverse_string(user_input))


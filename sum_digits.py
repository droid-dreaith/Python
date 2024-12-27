#create a program that takes a number as input and returns the sum of the digits of the number.

def sum_digits(n):
    return sum([int(i) for i in str(n)])
print("\n")

print(sum_digits(1234)) 
print("\n")

print(sum_digits(2743238))
print("\n")

print(sum_digits(23472374237472347234789))
print("\n")

print(sum_digits(678))
print("\n")

print(sum_digits(345345))
print("\n")

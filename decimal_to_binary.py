def decimal_to_binary(n):
    return bin(n)[2:]

num = int(input("Enter a decimal number: "))
binary = decimal_to_binary(num)
print(f"Binary representation of {num} is {binary}")

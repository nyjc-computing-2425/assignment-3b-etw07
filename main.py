stdform = input('Enter a number in scientific notation: ')
stdform = stdform.strip()

# Type your code below
pos = stdform.find("x")
mantissa = stdform[0:pos]
exponent = stdform[pos+4:]
number = mantissa + "E" + exponent
print(f"This number in E notation is {number}.")
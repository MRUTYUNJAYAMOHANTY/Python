# 4 primitive data types : Integers, Float, Strings, Boolean

# Strings : subscripting(pulling out a particular element from a string)
print("Hello"[0])

# Integer(All whole numbers , including +ve & -ve)
# 123456789 is same as 123_456_789 (used '_' instead of ',')

# Float(decimal numbers)
# 3141.59

# Boolean
# True & False

# Type check
name_int = len(input('what is your name?\n'))  # class int
name_str = input('what is your name?\n')  # class string
# print('len is' + name_int) will through type error
print(type(name_int))

# Type conversion or Type casting
convert_int_to_str = str(name_int)
print(type(convert_int_to_str))
# can be used float,int depending on requirement








# Example Input 1
# 2400
# Example Output 1
# Leap year.
# Example Input 2
# 1989
# Example Output 2
# Not leap year.

# e.g. The year 2000:
#
# 2000 รท 4 = 500 (Leap)
#
# 2000 รท 100 = 20 (Not Leap)

# ๐จ Don't change the code below ๐
year = int(input("Which year do you want to check? "))
# ๐จ Don't change the code above ๐

# Write your code below this line ๐

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year.")
        else:
            print("Not Leap Year")
    else:
        print("Leap Year")
else:
    print("Not Leap Year")


# Example Input
# weight = 80
# height = 1.75
# BMI = w / h ** 2

# Example Output
# 80 รท (1.75 x 1.75) = 26.122448979591837
# 26


# ๐จ Don't change the code below ๐
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# ๐จ Don't change the code above ๐

# Write your code below this line ๐

bmi = float(weight) / float(height) ** 2
bmi_whole_num = int(bmi)
print(bmi_whole_num)

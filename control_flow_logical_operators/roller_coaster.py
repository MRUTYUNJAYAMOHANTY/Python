print("Welcome to the roller coaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride roller coaster!")
    age = int(input("what is your age?"))
    if age < 12:
        bill = 5
        print("please pay ₹5")
    elif age <= 18:
        bill = 7
        print("please pay ₹7")
    elif 45 <= age <= 55:
        print("Enjoy a free ride!")

    else:
        bill = 12
        print("please pay ₹12")
    want_photo = input("Do You want to taken a photo? Y or N. ")
    if want_photo == 'Y':
        bill += 3
    print(f"Your final bill is ₹{bill}")

else:
    print('Sorry You have to be taller to rider!')

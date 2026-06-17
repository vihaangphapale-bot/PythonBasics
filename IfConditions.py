import sys
# age = int(input("What is your age? "))
# if age < 16 and age > 0:
#     print("You have", 16-age , "more years to drive.")
# elif age >= 16:
#     print("You can drive!")
# else:
#     print("Incorrect age.")


# discount = 0
# price = int(input("What's the price? "))
# if price <= 10 and price > 0:
#     discount = 10
# elif price > 10:
#     discount = 20
# else:
#     print("ERROR.")
#     sys.exit()
# print("Including your" , discount , "% Discount, your total cost is $" + str(price*((100-discount)/100)))


year = int(input("What's the current year? "))
if year % 4 == 0:
    if not year % 100 == 0:
        print("It's a leap year!")
    if year % 400 == 0:
        print("It's a leap year!")


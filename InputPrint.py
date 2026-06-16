# name = input("What's your name: ")
# print(name)
# age = int(input("What's your age: "))
# print(age) 
# print("You're going to be" , age + 4 , "in 2030")


# temp = int(input("Please give the current Tempreture in Farenheit: ")) 
# print(temp , "Converted to Celsius is" , round(5/9* (temp-32), 2) , "!")


# q = 25 * int(input("How many Quarters do you have? "))
# d = 10 * int(input("How many Dimes do you have? "))
# n = 5 * int(input("How many Nickels do you have? "))
# p = int(input("How many Pennies do you have? "))
# print("The total amount of cents you have is", q+d+n+p, "and, the number of the dollars you have are, $" + str((q+d+n+p)/100))

speed = int(input("What is the speed you spaceship in Miles Per Hour? "))
dis = 384400.0
time = dis/speed
days = time//24
hrs = time % 24
print("You have" , days , "days and" , hrs , "hours until you reach the moon.")
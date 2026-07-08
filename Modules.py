# import time 
# long = int(input("How many seconds will the timer be? "))
# for i in range(long, 0, -1):
#     print(i)
#     time.sleep(1)
# print("BLASTOFF")
# time.sleep(5)
# yn = input("Do you want to refresh the page(y/n)? ").lower
# if yn == 'y':
#     print("Please wait, your page is loading.")
#     time.sleep(2)
#     print("There is very high traffic. Please try agian later.")
# elif yn == 'n':
#     print("Thank you for visiting our website.")
# else:
#     print("ERROR")
# import random
# num = random.randint(1, 30)
# if num % 6 == 0:
#     print(f"{num} is divisible by 2 and 3")
# else:
#     print(f"{num} is not divisible by 2 and 3")

# import math
# nums = [169, 81, 256, 4]
# for i in nums:
#     print(math.sqrt(i))
# print(30*math.pi)

# import webbrowser

# options = input("Games, Youtube, or Study? ").lower()
# if options == "games":
#     webbrowser.open_new_tab("https://poki.com")
# elif options == "youtube":
#     webbrowser.open_new_tab("https://youtube.com")
# elif options == "study":
#     webbrowser.open_new_tab("https://khanacademy.org")
# else:
#     print("ERROR")

# import calendar

# year = int(input("What year were you born? "))
# month = int(input("What month were you born(1-12)? "))
# date = int(input("What date were you born?" ))
# print(calendar.month(year, month))
# print(calendar.weekday(year, month, date))

import datetime

print(datetime.datetime.now())
print(datetime.date.today())
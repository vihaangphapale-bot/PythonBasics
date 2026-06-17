# def correct(program):
#     works = True
#     while works:
#         try:
#             program = float(program)
#             works = False
#         except: 
#             program = input('''Not a Valid Answer ''')

# def sf():
#     days = [" Monday? ", " Tuesday? ", " Wednesday? ", " Thursday? ", " Friday? "]
#     total = 0
#     bars = 0
#     for i in days:
#         bars = int(input("How many Chocolate Bars were sold on" + i))
#         correct(bars)
#         total += bars
#         bars = 0
#     return total

# def est():
#     done = False
#     end = 4
#     score = 0
#     total = 0
#     while not done:
#         score = int(input("Whats the score? "))
#         correct(score)
#         total += score
#         score = 0
#         end = input("Are you entering more scores(y/n)? ")
#         if end != "y":
#             done = True
#     return total 

# def gsr():
#     works = False
#     end = 4
#     score = 0
#     total = 0
#     while not works:
#         score = input("Whats the price? ")
#         works = True
#         try:
#             score = float(score)
#             works = False
#         except: 
#             score = input('''Not a Valid Answer ''')
#         total += score
#         score = 0
#         end = input("Are you entering more prices(y/n)? ")
#         if end != "y":
#             works = True
#     return total 

# def stc():
#     total = 0
#     bars = 0
#     works = True
#     while works:
#         bars = int(input("How many miles did you run? " ))
#         correct(bars)
#         total += bars
#         bars = 0
#         end = input("Are you entering more? ")
#         if end != "y":
#             works = False
#     return total


# program = input('''Please choose one of the following programs(1-5)
# 1: School Fundraiser
# 2: Exam Score Tracker
# 3: Grocery Shopping Receipt
# 4: Sports Training Challenge
# 5: Reading Challenge ''')
# works = True
# while works:
#     try:
#         program = int(program)
#         works = False
#     except: 
#         program = input('''PLEASE ENTER A NUMBER ''')

# print(stc())

# phone = float(input("What's the Screen Size of your phone? "))
# if phone >= 5.0 and 10 >= phone:
#     print("$5")
# elif phone >= 3.5 and 5 > phone:
#     print("$2.50")
# else:
#     print("No protector available for this screen size")

for i in range(0, 50//7):
    print((i+1)*7)

v = 7
while v < 50:
    print(v)
    v += 7
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

# for i in range(0, 50//7):
#     print((i+1)*7)

# v = 7
# while v < 50:
#     print(v)
#     v += 7

import sys
def grade():
    mark = 0
    marks = 0
    subjects = ['Math? ', 'English? ', 'History? ', 'Science? ', 'PE? ', 'Elective? ']
    name = input("What is the name of the student: ")
    for i in subjects:
        mark += int(input("What marks did they get for " + str(i)))
        marks = round(mark/6, 2)
    grade = 'F'
    if marks >= 85:
        grade = 'A'
    elif marks >=70 and marks <= 84:
        grade = 'B'
    elif marks >= 55 and marks <= 69:
        grade = 'C'
    elif marks >= 40 and marks <=54:
        grade = 'D'
    print(name , "got total marks of" , mark, ", an avarage mark of" , marks, "and a grade of" , grade + "!")
    
def donation():
    money = 0
    part = []
    while True:
        money = int(input("How much is donated? $"))
        part.append(money)
        enter = input("Are you entering more(y/n)? ")
        if enter == 'n':
            break
        elif enter == 'y':
            continue
        else:
            print("Error")
            sys.exit()
    print("The total amount of donors were:" , len(part) , "and, the total amount earned was:" , sum(part) , "and, the avarage donation was:" , sum(part)/len(part) , "and the most amount of money donated was:" , str(max(part)) + "!")
    if sum(part) > 5000:
        print(f'''Good evening everyone,

When we started this fundraiser, we had a goal. Some people thought we'd reach it. Some people hoped we'd reach it. And some people were probably thinking, "We'll see."

Well, tonight, I am proud to announce that we didn't just raise money—we raised an incredible ${sum(part)}

Now, ${sum(part)} may just sound like a number, but it represents something much bigger. It represents generosity, teamwork, and a community willing to come together for a great cause.

To everyone who donated: thank you. To everyone who volunteered: thank you. To everyone who spread the word, encouraged others, or supported us in any way: thank you.

Because of you, what started as an idea became a reality.

And let's be honest—raising ${sum(part)} isn't easy. If it were, I'd be standing here announcing my retirement from school and my new life on a private island.

But seriously, this achievement belongs to all of you. Every dollar made a difference, and every contribution helped us reach this amazing milestone.

So please give yourselves a round of applause. You earned it.

Thank you for your support, thank you for believing in this cause, and thank you for helping make this fundraiser a huge success!''')


def groceries():
    total = 0
    discount = 0
    tax = 0
    subtotal = 0
    done = False
    while not done:
        input("Whats the name of the item? ")
        total += int(input("Whats is the cost of the item? $")) * int(input("How much of this are you going to buy? "))
        if input("Do you want to enter more(y/n)? ").lower() != 'y':
             done = True
    subtotal = total
    if total > 150:
        discount = total*0.10
    elif total > 300:
        discount = total*0.15
    total = total - discount
    tax = round(total*0.06, 2)
    total += tax
    print(f"Your base total is ${subtotal} and your discount off is ${discount} and your tax is ${tax}. Your final payment will be ${total}")

def fitness():  
    steps = 0
    all = []
    for i in range(1, 8):
        steps = int(input(f"How many steps did you walk on day {i}? "))
        all.append(steps)
        steps = 0
    
    print(f"Your total amount of steps are {sum(all)}, the avarage amount of steps per day is {sum(all) / 7}, the most amount of steps was {max(all)}, and the lowest amount of steps was {min(all)}. ")
    if sum(all) > 10000:
        print("Congratulations! You walked more than 10000 steps!")

def library():
    total = 0
    student = 0
    more = 0
    most = "bob"
    amount = 0
    name = ""
    while True:
        name = input("Name: ")
        student += 1
        book = int(input("Books: "))
        total += book
        if book > 3:
            more += 1
        if book > amount:
            amount = book
            most = name
        if input("Press enter for more: ") != "":
            break
    print(f'''{total} amount of books were borrowed
{student} amount of students were served
{round(total/student,2)} was the average amount of books per student
{most} got the most amount of books with {amount} books
{more} students borrowed more than 3 books
          ''')
    if total > 100:
        print("Today was a busy day.")
import math


def classroom():
    row = int(input("Seats per row: "))
    students = int(input("Number of students: "))

    names = []
    for i in range(students):
        names.append(input("Name: "))

    rows = math.ceil(students / row)
    if students % row != 0:
        for i in range(rows, 0, -1):
            if students % i == 0 or students % i == 1:
                rows = i
                break

    per_row = students // rows
    for n in range(rows):
        start = per_row * n
        end = per_row * (n + 1)
        print(names[start:end])

    if students % rows == 1:
        print(f"['{names[-1]}']")



        
def bus():
    row = int(input("Seats per bus: "))
    students = int(input("Number of people: "))

    names = []
    for i in range(students):
        names.append(input("Name: "))
    rows = math.ceil(students / row)
    per_row = math.ceil(students / rows)
    for n in range(rows):
        start = per_row * n
        end = per_row * (n + 1)
        print(names[start:end])

    if students % rows == 1:
        print(f"['{names[-(students%row):]}']")
    print(f"{math.ceil(students/row)} buses were used.")
    print(f"{row-(students%row)} seats were empty.")

def box():
    b = input("What is the weight that 1 box can hold? ")
    while True:
        try:
            b = int(b)
            break
        except:
            b = input("What is the weight that 1 box can hold? ")
    total = int(input("How many weights will you use? "))
    while True:
        try:
            total = int(total)
            break
        except:
            total = int(input("How many weights will you use? "))
    w = []
    for i in range(total):
        while True:
            l = input("What is the weight? ")
            try: 
                l = int(l)
                w.append(l)
                break
            except:
                l = input("What is the weight? ")
    box = []
    extra = []
    w.sort(reverse=True)
    for x in w:
        # wlen = len(box)
        # if wlen > 0:
        space = False
        if x > b:
            extra.append(x)
        else: 
            for i in box:
                if sum(i) + x <= b: 
                    i.append(x)
                    space = True

            if space == False:
                box.append([x])
    f = 0
    for i in box:
        if sum(i) < b:
            print(f"Unnused Space: {b-sum(i)} pounds for box {box.index(i) + 1}")
        if f < sum(i):
            f = sum(i)

    print(box)
    print(f"These are the weights that couldn't be placed: {extra}")
    print(f"The fillest weight in a box was {f}!")
box()
# check if a number is in the range of 10 and 25


# num = int(input("Enter the number to check if it lies betweenn 10 to 25: "))
# if 10 <= num <=25:
#     print("Yes it lies!!!!")
# else:
#     print("No it doesntttt!")


# you got some marks, marks>=90 fall in grade A, marks>=75 fall in grade B , marks <75 falls in grade c, find the grade.

# marks = int(input("Enter the marks you got: "))
# print("You entered:", marks)

# if marks >= 90:
#     print("Woooh, You passed with first division with grade 'A'")
# elif marks >= 75:
#     print("Good, You passed with second division with grade 'B'")
# elif marks >= 35:
#     print("Satisfactory, You passed with third division with grade 'C'")
# else:
#     print("You failed, do hard work!!!")


# take radius as inuput from user and print area of a circle having that radius

# radius = int(input("Enter the radius of the circle: "))
# area = 3.14 * radius * radius
# print("Area of a given circle", area)

# take length of 3 side of triangle from user and check what type of triangle it is

# triangleOne = int(input("Enter first triangle side"))
# triangleTwo = int(input("Enter second triangle side"))
# triangleThree = int(input("Enter third triangle side"))

# if triangleOne == triangleTwo == triangleThree:
#     print("Triangle is Equilateral triangle")
# elif triangleOne == triangleTwo or triangleOne == triangleThree or triangleTwo == triangleThree:
#     print("Triangle is Isosceles triangle")
# else:
#     print("Triangle is Scalene triangle")

# check if a number is in between 1 and 90 without using any logical operator

# num = int(input("Enter a number: "))

# if num >= 1:
#     if num <= 90:
#         print("Number lies between 1 to 90")
#     else:print("Number is greater than 90")
# else:
#     print("Number is not greater than 1")


# print numbers from 1 to n , take n from user as integer input

# startNumber = 1
# n = int(input("Enter number: "))

# while n >= startNumber:
#     print(startNumber)
#     startNumber += 1

# print numbers from n to 0 (Decreasing order) , take n from user as integaer input

# n = int(input("Enter number: "))

# while n >= 0:
#     print(n)
#     n -= 1

# print all the even numbers between 1 and n.

# n = int(input("Enter number: "))
# startNumber = 1
# while n >= startNumber:
#     if startNumber % 2 == 0:
#         print(startNumber)
#     startNumber += 1

# correct password is "skillians", ask user for the password untill he/she enters "skillians"

# password = input("Enter Password: ")

# while password != "skillians":
#     print("Your entered password is wrong")
#     password = input("Enter Password: ")

# print("Access granted!")


# print the sum from integers 1 to n

# intStart = 1
# n = int(input("Enter number: "))
# total = 0

# while intStart <= n:
#     total += intStart
#     intStart += 1

# print("Sum from 1 to", n, "is:", total)

# print multiplication of numbers from 1 to n.

# startInt = 1
# n = int(input("Enter number: "))
# total = 1

# while startInt <= n:
#     total *= startInt
#     startInt += 1
# print("Multiplication from 1 to", n, "is:", total)

# print all the numbers from 1 to n which are divisible by 5 and 3

# startingNumber = 1
# n = int(input("Enter number: "))

# while startingNumber <= n:
#     if startingNumber % 5 == 0 and startingNumber % 3 == 0:
#         print(startingNumber)
#     startingNumber += 1


# miniGoal = ["getMarriedToPranjali", "Buy a own luxury house", "Always follow truth and dharm marg", "Helping the needy one"]

# for goal in miniGoal:
#     print(goal)


# pass12 = input("Enter password: ")

# while pass12 != "Abhi":
#     print("Access denied")
#     pass12 = input("Enter password: ")
# print("Access Granted")

# a=0
# b = int(input("Enter till when you want to print: "))
# while a < b:
#     print(a)
#     a += 1
# print(f"Loops break when value of a becomes {a}, which is not smaller than {b}")

# a = 10

# while a >= 0:
#     if(a == 5):
#         break
#     print(a)
#     a -=1
# print("Loops break as a == 5")



# ------------------------------------------------------------------------------------------------------------------------

# Print * into 4 rows and 5 columns using nested loops

# rows = 4
# column = 5

# while rows > 0:
#     tempColumn = column
#     while tempColumn > 0:
#         print("*", end="")
#         tempColumn = tempColumn - 1
#     print()
#     rows = rows - 1

# take row and columns from user to print matrix

# row = int(input("Enter number of rows: "))
# col = int(input("Enter number of columns: "))

# while row > 0:
#     tempCol = col
#     while tempCol > 0:
#         print("*", end="")
#         tempCol -= 1
#     print()
#     row -= 1

# rows = int(input("Enter number of rows: "))


# initialStar = 1

# while rows > 0:
#     tempStar = initialStar
#     while tempStar > 0:
#         print("*", end="")
#         tempStar -= 1
#     print()
#     rows -= 1
#     initialStar += 1


# 1
# 12
# 123
# 1234
# 12345

# 1
# 23
# 456
# 78910
# 1112131415
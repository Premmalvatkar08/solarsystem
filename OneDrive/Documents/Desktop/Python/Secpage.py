
# String - IT IS DATA TYPE THAT STORES A SEQUENCE OF CHARACTERS. ------------------------------------------------------------------------
# str1 = "This is a string."
# str2 = 'My name'
# str3 = """String"""

# Escape sequence characters - Special Characters used for formating (for next line, space, tab, etc.)

# str10 = "This is a sentence.\nWe are writing it."
# print(str10)
# Final_str = str1+"  "+str2
# print(Final_str)   ..............................................{ Concatenation - Adding of two string}
# print(len(Final_str)) ...........................................{ Length of string }

#INDEXING (position of character) ------------------------------------------------------------------------------------------------
# str = "Prem Malvatkar"
# ch = str[5]
# print(ch)
# print(str[8])

#SLICING - Accessing the parts of the string -----------------------------------------------------------------------------------------
#format :- str[Starting_index : Ending_index]
# str = "Prem Malvatkar"
# print(str[5:len(str)])

# print(str[-8 : len(str)]) .......(special case of slicing i.e., Negative slicing(backward counting))

#STRING FUNCTIONS ----------------------------------------------------------------------------------------------------------------

# str = "i am a engineer. i am proud of it."
# print(str.endswith("it."))
# print(str.capitalize())
# print(str.replace("i","We"))
# print(str.find("of"))

#practice set :- WAP to input users first name & print its length --------------------------------------------------------------

# name = input("Enter User's name :-")
# print("length of your name is ", len(name))


# CONDITIONAL STATEMENT :------------------------------------------------------------------------------------------------------

"""
light = input("Enter the color of the light :- ")

if(light == "red"):
    print("stop")
elif(light == "yellow"):
    print("wait")
elif(light == "green"):
    print("go")
else:
    print("Light is broken")
print("Drive Safe !!")
"""
#indentation - Proper spacing between elements .......................................

#Practice set - WAP to check if the entered number is odd or even --------------------------------------------------------------------------------------

# num = int(input("Enter the number :-"))

# rem = num % 2
# if(rem == 0):
#     print(num, " is the Even number.")
# else:
#     print(num, " is the Odd number.")

#Practice Set - WAP to find the greatest of the three numbers entered by the user ------------------------------------------------------------------

a = int(input("Enter the first number :-"))
b = int(input("Enter the second number :-"))
c = int(input("Enter the third number :-"))

if(a >= b and a >= c):
    print(a, "is the largest number.")
elif(b >= a and b >=c):
    print(b, "is the largest number.")
elif(C >= a and c >= b):
    print(c, "is the largest number.")

    
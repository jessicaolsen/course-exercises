#Exercise 1 Print Hello World
#print('Hello World')

#Exercise 2 Creating a Shape
#print("   /|")
#print("  / |")
#print(" /  |")
#print("/___|")

#Exercise 3 Using Variables and Data Types
#character_name = "John"
#character_age = "35"
#print("There once was a man named "+ character_name + ",")
#print("he was " + character_age + " years old.")
#Changing the name half way through the story
#character_name = "Mike"
#print("He really liked the name " + character_name + ", ")
#print("but didn't like being " + character_age + ".")

#Exercise 4 Working with Strings
#phrase = "Giraffe Academy"
#print(phrase.replace("Giraffe", "lion").upper())

#Exercise 5 Working with Numbers
#my_num = 7
#Converting number from string
#print(str(my_num) + " is my favorite number")
#Most common functions used on numbers
#my_num = -5
#print(abs(my_num))
#print(pow(my_num, 2))

#from math import *
#num = floor(3.7)
#print(num)

#Exercise 6 Getting Input from Users
#name = input("Enter your name: ")
#print("Hello " + name + "!" )

#Exercise 7 Building a Basic Calculator
#num1 = int(input("Enter a Number: "))
#num2 = float(input("Enter a number: "))
#result = num1 + num2 
#print(result)

#Exercise 8 Mad Lib Game
#color = input("Enter a color: ")
#plural_noun = input("Enter a plural noun: ")
#celebrity = input("Enter a celebrity: ")

#print("Roses are " + color)
#print(plural_noun + " are blue")
#print("I love " + celebrity)

#Exercise 9/10 Lists
#lucky_numbers = [6, 5, 7, 23, 45, 6, 7]
#friends = ["Kevin", "Karen", "Jim", "Amy", "Oscar", "Nick", "Jessica"]
#friends.extend(lucky_numbers)
#print(friends)

#Exercise 11 Functions
#def say_hi(): 
   # print("Hello")

#say_hi()

#Exercise 12 BNuilding a more advance Calculator
num1 =  float(input("Enter First Number: "))
operator = input("Enter operator: ")
num2 = float(input("Enter second Number: "))

if operator == '+' : 
    print(num1 + num2)
elif operator == '-' : 
    print(num1 - num2)
elif operator == '/' : 
    print(num1/num2)
elif operator == '*' : 
    print(num1*num2)
else : 
    print("Invalid Operator")
    

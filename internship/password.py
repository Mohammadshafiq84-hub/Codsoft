import random
import string
import sys

print("Welcome to password generator")

while True:
    try:
        length=int(input("Enter the length of the password:"))
        if length<=0:
             raise ValueError("Please enter a positive number!!")

        break
    except ValueError:
        print("Invalid input. Please enter a number")
      
character=[]  

print("1.Uppercase letters")
print("2.Lowercase letters")
print("3.Digits")
print("4 Special characters")
print("5.Exit")


while True:
    choice=input("Enter your choice:")

    if "1" in choice:
        character.extend(list(string.ascii_uppercase))

    if "2" in choice:
        character.extend(list(string.ascii_lowercase))

    if "3" in choice:
        character.extend(list(string.digits))

    if"4" in choice:
        character.extend(list(string.punctuation))

    if character:
        break

    else:
        print("Select at least one type of characters!!!")
       

password="".join(random.choices(character, k=length))

print(f"Password generated is: {password}")      









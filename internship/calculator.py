import sys

print("------------------------")
print("SIMPLE CALCULATOR")
print("------------------------")
print("1.ADDITION")
print("2.SUBTRACTION")
print("3.MULTIPLICATION")
print("4.DIVISION")
print("5.EXIT")


num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))


choice=int(input("Enter your choice to perform an action:"))


def add():
    result=num1+num2
    print(num1,"+",num2,"=",result)

def sub():
    result=num1-num2
    print(num1,"-",num2,"=",result)

def mul():
    result=num1*num2
    print(num1,"*",num2,"=",result)

def div():
    result=num1/num2   
    print(num1,"*",num2,"=",result)  


if choice==1:
    add()  
        

elif choice==2:
    sub()

elif choice==3:
    mul()

elif choice==4:
    div()

elif choice==5:
    print("End of program.....")
    sys.exit(0)   

else:
    print("Invalid input!!!!")                  
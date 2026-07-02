#Functions and recursion in python
#Function is a block of statement tha performs a specific task  
#function defination
def sum(a,b):# a and b are parametres
    s=a+b
    print(s)
    return s

print(sum(2,3)) #callin function,argument

#average of three numbers
def avg1 (a,b,c):
    s=(a+b+c)/3
    return s
print(avg1(2,3,6))

#tyoes of functions
#1)built in function : print(),len(), type(),range()
#2)user definde function : functions defined by the users 

#default parameters: assining the defult values to parameters , which is used when no agument is passed
def sum(a=1,b=1):
    s=a+b
    print(s)
    return s
sum()

print("------------------------------")
#Recursion : When a function calls itself repeatedly
def show(n):
    if(n==0): #base case
        return
    print(n)
    show(n-1) #recurtion

show(5)
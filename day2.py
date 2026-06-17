#strings and Conditional statements, conccation, indexing and sclicing

#concation
str1="\tHi "
str2="\nHow are you"
str3=str1+str2
len(str3)#lenght of string
#indexing
print(str3)
ch =str1[2]
print(ch)
print(str1[2])
#sclicing
str="Abhiraj Mangire"
print(str[2:7])
print(str[2:len(str)])
print(str[:4])
print(str[4:])

#string function
print(str.endswith("ire"))#check if true or not
print(str.capitalize() )#capatlize first function
print(str.replace("A","o"))
print(str.find("o"))#finds the word and returns index ,if doesnt exit returns -1
print(str.find("a"))

#conditional Statements
#if-elif-else
age=int(input("Enter Your age"))
if(age>=18):
    print("Can apply for driving licence")
elif(age<18):
    print("can't apply for licence" )
else:
    print("invalid age")
    
#nested loop
if(age>=18):
    if(age!=0):
        print("Can apply for driving licence")
else:
    print("invalid age")
    
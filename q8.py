#to find the gretes of 3 number entered by user.
a = int(input("Entere the number"))
b = int(input("Entere the number"))
c = int(input("Entere the number"))

if(a>=b and a>=c):
    print("Greatest number is",a)
elif(b>=a and b>=c):
     print("Greatest number is",b)
else:
      print("Greatest number is",c)
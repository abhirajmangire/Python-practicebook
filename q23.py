#print numbers from 1 to 100

for i in range(1,101,+1):
    print(i)

#print number fromm 100 to 1
i=100
for i in range(100,0,-1):
    print(i)

#print the multipliction table of a number n
n=int(input("enter the number: "))
for i in range(1,11):
    print(n,"*",i,"=",n*i)

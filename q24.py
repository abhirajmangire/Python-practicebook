#to find the sum of first n naturla numbers (using while loop)

n=4
i=1
sum =0
while i<=n:
    sum+=i
    i+=1
print("The sum of ",n," natural number is: ",sum)



#to fing the factorial of first n numbers.(using for loop)
fact =1
for i in range(n,0,-1):
    fact*=i
print("the factorial of ",n,"is:",fact)
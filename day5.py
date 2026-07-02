# Loops in pyhton
#loops are used to repeat instuctions

#while loop

count= 0 #iterators
while count<=5:
    print("hello")
    count+=1
i=0
while i<=5:
    print(i)
    i+=1
print("the end")

#break :- used to tr=erminate the loop when encountered
#continue : terminates execution i the current iteration and continues execution of loop whit the next iteration

i=0
while i<6:
    if i==3:
        break
    print(i)
    i+=1

i=0
while i<6:
    i+=1
    if i==3:
        continue
    print(i)
   

#for loop
#loopare used for sequentil traversal . for traversing list string tuple
list =[1,2,3,4,5,]
for val in list:
    print(val)

a=("a","b","c","d")
for i in a:
    print(i)

#we can use optional else with for , where we will use break.

#range function : it returns a sequence of numbers , starting from 0 by default , and increments by 1 and stops before a sepcific number.
#range(start, stop,step)
print("-----------------")
for val in range(3):
    print(a[val])

print("-----------------")
for val in range(2,3):
    print(a[val])

print("-----------------")
for val in range(2,4,2):
    print(a[val])



#pass Statement :- pass is a null statement that does nothing .it is used as a placeholder for future code
for el in range(10):
    pass
print("Next Work ")
#pass in used in for loop, if else while, exception handling etc


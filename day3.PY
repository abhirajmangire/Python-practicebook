#List
marks=[99,92,93,98,88,97,67,78]
print(marks)
print(len(marks))
print(type(marks))
print(marks[3])
#lists are mutable but string are immutable
marks[3]=00
print(marks[3])
print(marks)


#list slicing 
print(marks[3:7])
print(marks[:6])
print(marks[4:])
print(marks[-8:-4])


#list methods (mutation)
print(marks.append(30))#prints the output as null for all th e majr list methods

marks.append(91) #add the element at the end of list
print(marks)

marks.reverse #reverse the list
print(marks)

marks.sort #sorts the lis in ascending order
print(marks)

marks.sort(reverse=True)#sorts the lis in descending order
print(marks)

marks.insert(4,55) #inser the element at any index
print(marks)

marks.remove(93)# remove the first occurance of the given element
print(marks)

marks.pop(5) #removes the element at specifc index provided
print(marks)



#Tuples in python
#a built in data tuoe that lets us create immutable list just use perenthisis ()
marks=(20,22,26,28,21)
print(marks)
print(type(marks))
a=()
print(a) #prints empty list
b=(1) #it take b as variable
print(type(b))
c=(1,)#it takes c as tuple due to presence of ',' in
print(type(c))

#slicing in tuple works similar to list or strings 
print(marks[1:3])
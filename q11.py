#to check if a list contains a palindrome of elements 
#palindrome is a word that is same when read from front and back
list = []
n=int(input("Enter the number of elements to be stored in list: "))
for i in range(n):
    element =input("Enter the element of the list:  ")
    list.append(element)
print(list)
list_copy= list.copy()
list.reverse()
if list == list_copy:
    print("this list is a palindrome")
else:
    print("this list is not a palindrome")
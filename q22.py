#print and search the elements of following list
nums = [1,4,9,16,25,36,49,64,81,100]
for i in nums:
    print(i)
    

x=int(input("Enter the number you want to search: "))
for i in nums:
    if x== i:
        print(x, " found at ", i)
        break
    else:
        print("not found")

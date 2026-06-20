#search for a number x in this tuple using loop
nums = (1,4,9,16,25,36,49,64,81,100)
i = 0
while i<=len(nums)-1:
    print(nums[i])
    i+=1

x=int(input("Enter the number you want to search "))
j=0
while j< len(nums):
    if x == nums[j]:
        print("found at ",j)
        break
    else:
        print("searching")
    j+=1

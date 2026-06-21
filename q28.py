#write a recursive function to calcullate the sum of first n natural numbers

def add(n):
    if(n==0):
        return 0
    return add(n-1)+n
print(add(10))

# wrute a recursive function to print all elememts of list
nums=[1,2,3,4,5,6,7]
def show(list,idx=0):
    if(idx==len(list)):
        return 0
    print(list[idx])
    show(list,idx+1)
show(nums)
    
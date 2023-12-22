def binsearch(arr,n,target):
    result=0
    low=0
    high=n-1
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]==target):
            return mid
        elif(target<mid):
            high=mid-1
        else:
            low=mid+1



arr=[]
n=int(input("Enter Size:"))
for i in range(n):
    b=int(input())
    arr.append(b)
t=int(input("Enter the target:"))
# print(arr)
print("Target found at index: ",binsearch(arr,n,t))
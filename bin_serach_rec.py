def binsearch(arr,l,h,target):
    mid=(l+h)//2
    if(l>h):
        return -1
    elif(arr[mid]==target):
        return mid
    elif(target>arr[mid]):
        return binsearch(arr,mid+1,h,target)
    else:
        return binsearch(arr,l,mid-1,target)


n=int(input("Enter the range:"))
N=[]
for i in range(n):
    m=int(input("Enter element: "))
    N.append(m)

low=0
high=n-1
t=int(input("Enter the target: "))
print("Resulted Index: ",binsearch(N,low,high,t))

    
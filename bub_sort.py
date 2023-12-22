arr=[4,5,6,7,8,5,43,3,67,9,98]
n=len(arr)
for i in range(n):
    swapp=False
    for j in range(0,n-i-1):
        if(arr[j]>arr[j+1]):
            arr[j],arr[j+1]=arr[j+1],arr[j]
            swapp=True
    if(swapp==False):
        break

print(arr)

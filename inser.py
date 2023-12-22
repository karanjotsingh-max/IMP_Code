arr=[4,5,6,7,8,5,43,3,67,9,98,90]
n=len(arr)
for i in range(0,n):
    j=i
    while(j>0 and arr[j-1]>arr[j]):
        arr[j-1],arr[j]=arr[j],arr[j-1]
        j-=1

print(arr)


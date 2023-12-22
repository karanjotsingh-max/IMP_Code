arr=[4,5,6,7,8,5,43,3,67,9,98]
n=len(arr)
for i in range(0,n-1):
    mini=i
    for j in range(i,n):
        if(arr[mini]>arr[j]):
            mini=j
    arr[i],arr[mini]=arr[mini],arr[i]

print(arr)
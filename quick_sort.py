def qs(arr,low,high):
    if(low<high):
        partind= pindex(arr,low,high)
        qs(arr,low,partind-1)
        qs(arr,partind+1,high)
    return arr


def pindex(arr,low,high):
    pivot=arr[low]
    i=low
    j=high
    while(i<j):
        while(arr[i]<=pivot and i<=high-1):
            i+=1
        while(arr[j]>pivot and j>=low+1):
            j-=1
        if(i<j):
            arr[i],arr[j]=arr[j],arr[i]
    arr[low],arr[j]=arr[j],arr[low]
    return j


arr=[5,4,5,3,2,6,4,8,9,23,56,21]
low=0
n=len(arr)-1
high=n
print(qs(arr,low,high))
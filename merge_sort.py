def mergsort(arr,low,high):
    if(low==high):
        return 
    mid=(low+high)//2
    mergsort(arr,low,mid)
    mergsort(arr,mid+1,high)
    merge(arr,low,mid,high)
    return arr

def merge(arr,low,mid,high):
    arr2=[]
    left=low
    right=mid+1
    while(left<=mid and right<=high):
        if(arr[left]<=arr[right]):
            arr2.append(arr[left])
            left+=1
        else:
            arr2.append(arr[right])
            right+=1

    while(left<=mid):
        arr2.append(arr[left])
        left+=1
    while(right<=high):
        arr2.append(arr[right])
        right+=1
    for i in range(low,high+1):
        
        arr[i]=arr2[i-low]
    


arr=[5,4,6,7,2,9,8]
n=len(arr)
print(mergsort(arr,0,n-1))





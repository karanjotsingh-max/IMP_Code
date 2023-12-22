#HASHING
arr2=[]
print("Enter Range of array:")
d=int(input())
hsh=[0]*(1000000)
for i in range(d):
    n=input()
    arr2.append(n)

for i in range(d):
    hkey=arr2[i]
    hsh[ord(hkey)-ord('a')]+=1
print("Enter char:",end="")
charr=input()
print("Frequnecy of ", charr," is: ",hsh[ord(charr)-ord('a')])
    
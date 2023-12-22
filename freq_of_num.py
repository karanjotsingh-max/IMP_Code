#HASHING
arr2=[]
print("Enter Range of array:")
d=int(input())
hsh=[0]*(1000000)
for i in range(d):
    n=int(input())
    arr2.append(n)

for i in range(d):
    hkey=arr2[i]
    hsh[hkey]+=1
print("Enter number:",end="")
num=int(input())
print("Frequnecy of ", num," is: ",hsh[num])
    
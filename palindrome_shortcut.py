s = "karak"

def pal(i, j):
    if i < 0 :
         return False
    return s[i:j] == s[i:j][::-1] #main palindrome check
n=len(s)
print(pal(0,n))

# class Solution:
#     def maxPalindromes(self, s: str, k: int) -> int:
#         n=len(s)
#         sum=0
#         i=0
#         while(i<(n-k)+1):
#             for j in range(i+k-1,n):
#                 if(s[i]==s[j] and (j-i)>=k-1):
#                     s2=s[i:j+1]
#                     s3=s2[::-1]
#                     if(s2==s3):
#                         print(s2)
#                         i=j
#                         sum=sum+1
#                         break
#             i=i+1  
#             print("Next I:",i)      
#         return sum
        
                
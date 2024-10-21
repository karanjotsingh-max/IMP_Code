from collections import defaultdict
import heapq
arr = [1,1,2,2,2,3,4,5,6,6,6,6,6,6]
k=3
heap=[]
hash_map=defaultdict(int)
for i in range(len(arr)):
    hash_map[arr[i]]+=1
print(hash_map)
for key, values in hash_map.items():
    heapq.heappush(heap,(values,key))
    if len(heap)>k:
        print(heapq.heappop(heap))
ans=heapq.heappop(heap)
print("Ans: ", ans[1])

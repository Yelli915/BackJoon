import sys

arr = list(range(1,31)) 

for _ in range(28) :
    b = int(sys.stdin.readline().strip())  
    if b in arr :
        arr.remove(b)  

arr.sort()
print(arr[0])
print(arr[1])
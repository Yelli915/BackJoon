import sys
N,M = map(int, sys.stdin.readline().split())
arr=[]

for a in range(1,N+1) :
    arr.append(a)

for _ in range(M):
    i,j = map(int, sys.stdin.readline().split())
    arr[j-1],arr[i-1] = arr[i-1],arr[j-1]
print(*arr)
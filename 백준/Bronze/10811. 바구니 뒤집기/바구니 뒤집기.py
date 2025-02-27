import sys
N,M = map(int, sys.stdin.readline().split())

array = list(range(1,N+1))

for _ in range(M):
    i,j = map(int, sys.stdin.readline().split())
    array[i-1:j] = array[i-1:j][::-1] #역순으로 적는 방법
    
print(*array)
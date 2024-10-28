import sys
N,X = map(int,sys.stdin.readline().split())
data=list(map(int,sys.stdin.readline().strip().split()))
number = []

for num in data :
    if num < X :
        print(num, end=" ")
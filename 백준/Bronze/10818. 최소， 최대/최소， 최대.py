import sys
N= int(sys.stdin.readline())

data = list(map(int,sys.stdin.readline().split()))
    
maximum = max(data)
minimum = min(data)

print(minimum, maximum)
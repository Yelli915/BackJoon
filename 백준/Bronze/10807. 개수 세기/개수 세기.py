import sys
N = int(sys.stdin.readline())
data = sys.stdin.readline().split()
v = int(sys.stdin.readline())
count = 0

for i in range(N):
    if int(data[i]) == v:
        count += 1

print(count)

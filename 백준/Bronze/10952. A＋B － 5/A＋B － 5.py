import sys

data = []
while True:
    a, b = map(int, sys.stdin.readline().strip().split())
    if a == 0 and b == 0:
        break
    data.append(a + b)

for index in data:
    print(index)
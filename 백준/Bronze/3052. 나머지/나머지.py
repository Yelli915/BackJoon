import sys
arr = []
for _ in range(10) :
    a = int(sys.stdin.readline().strip())
    a = a%42
    arr.append(a)
arr = list(set(arr))
print(len(arr))
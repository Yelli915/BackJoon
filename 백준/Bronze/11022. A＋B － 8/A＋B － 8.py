import sys
T = int(sys.stdin.readline())

for i in range(1, T + 1):
    a, b = map(int, sys.stdin.readline().split())
    total = a + b
    print(f"Case #{i}: {a} + {b} = {total}")
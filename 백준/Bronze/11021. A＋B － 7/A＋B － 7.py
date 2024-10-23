import sys
T = int(sys.stdin.readline())
i = 0
total=[]
for i in range(1,T+1) :
    a,b = map(int, sys.stdin.readline().strip().split())
    add = a+b
    total.append(add)
      
for j in range(0,T) :
    print(f"Case #{j+1}:",total[j])
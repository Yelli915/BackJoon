import sys
data = []

for i in range(0,9) :
    num = int(sys.stdin.readline())
    data.append(num)
    i+=1
    
maximum = max(data)
print(maximum)


print(data.index(maximum)+1)
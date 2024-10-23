n = int(input())  
for number in range(n):
    a,b = map(int, input().split())
    if (a!='' and b!='') :
        print (a+b)
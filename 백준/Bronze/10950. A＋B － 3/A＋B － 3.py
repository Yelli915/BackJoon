n = int(input())  
for number in range(n):
    a,b = map(int, input().split())
    if (a!='' and b!='') :
        print (a+b)

n 줄의 순서쌍을 처리하겠다는 의미로 해석 

사람들은 import sys 많이 했네 
sys : 명령형 인자를 받아올 때 주로 사용

import sys
n = int(input())
for i in range(n) :
    a,b = map(int, sys.stdin.readline().strip().split())
    print(a+b)

<import sys : input 대신 sys.stdin.readline() 사용>
sys.stdin.readline() 사용법
-- 한 개의 정수를 받을 때 
    int(sys.stdin.readline()) 개행문자 제거를 위해 붙이는 strip()
-- 정해진 개수의 정수를 받을 때 
    map(int, sys.stdin.readline().strip().split())
-- 임의의 개수의 정수를 한 줄에 입력받아 리스트에 저장할 때
    data = list(map(int, sys.stdin.readline().strip()))
★ 2차원 리스트에 저장할 때 (임의의 개수의 정수를 n줄 입력받아서) ★
    data = []
    n=int(sys.stdin.readline())
    for i in range(n) :
        data.append(list(map(int, sys.stdin.readline().split())))
★ 문자열 n줄을 입력받아 리스트에 저장할 때 ★
    n=int(sys.stdin.readline())
    data = [sys.stdin.readline().strip() for i in range(n)]

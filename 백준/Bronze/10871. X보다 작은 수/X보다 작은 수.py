import sys
N,X = map(int,sys.stdin.readline().split())
data=list(map(int,sys.stdin.readline().strip().split()))
number = []

for num in data :
    if num < X :
        print(num, end=" ")

나열하는 방법
end = " " ; 줄바꿈 없이 공백으로 끝
sep = " " ; 줄바꿈 없이 나열하기 << 응용가능

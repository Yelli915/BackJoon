import sys
N = int(sys.stdin.readline())
data = sys.stdin.readline().split()
v = int(sys.stdin.readline())
count = 0

for i in range(N):
    if int(data[i]) == v:
        count += 1

print(count)


1. sys.stdin.readlind() -> 사용 결과는 문자열이므로 정수 변환이 필요함
2. Java나 C언어와 달리 +=를 추가적으로 해야한다는 점 
3. print(count)를 바로 할 수 있는 것은 정수형 변수의 나열로 만들었기에
-- 배열이라면 len(count)였을텐데 

import sys

data = []
while True:
    a, b = map(int, sys.stdin.readline().strip().split())
    if a == 0 and b == 0:
        break
    data.append(a + b)

for index in data:
    print(index)

while에서 break문 사용하기 (for보다는 while에 써야겠다)
while True:
    a, b = map(int, sys.stdin.readline().strip().split())
    if a == 0 and b == 0:
        break  # a와 b가 모두 0이면 반복을 종료
    data.append(a + b)
while True라는 무한 반복에서 조건이 달성하면 break - 끝나고 다음으로 넘어가겠다는 의미 (while 해당되는 것은 안하겠다)

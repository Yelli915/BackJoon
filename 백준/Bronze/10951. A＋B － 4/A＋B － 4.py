import sys

while True:
    try:
        a, b = map(int, sys.stdin.readline().split())
        print(a + b)
    except:
        break 
문제에서 명시된 추가적인 종료 조건이 없기 때문에 **EOF(End of File)**가 입력의 끝을 나타내는 것으로 간주됩니다. 
입력이 끝날 때까지 각 줄의 A와 B를 받아 더한 값을 출력하면 됩니다.

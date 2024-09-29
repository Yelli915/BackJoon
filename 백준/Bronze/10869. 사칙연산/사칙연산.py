A, B = map(int, input().split())
addition = A + B
subtraction = A - B
multiplication = A * B
division = A // B  
modulus = A % B 
print(addition, '\n', subtraction, '\n', multiplication, '\n', division, '\n', modulus, sep="")

<줄바꿈 방법>
1. /n : 숫자열과 혼합 불가 -- 문자열로만 쓰임
-> 문자열로 변환 후에 붙여야 함 

2. sep (seperate) : 문자열과 숫자열 혼합 모음을 구분 짓기 가능 
- 매개변수는 무조건 문자열로 설정, 기본 값은 '' (공백)

<연산>
1. 나눗셈은 //
2. 나머지는 %

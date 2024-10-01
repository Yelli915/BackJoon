year = int(input())
if (year%4==0 and year%100!=0) or (year%400==0) :
    print(1)
else : print(0)

# 논리 연산자 : and, or, not  ()
# 배열이나 데이터프레임에서는 & | 사용 (비트 연산자, (앞에서 언급한 조건에서)논리 연산자)

import sys
data = []

for i in range(0,9) :
    num = int(sys.stdin.readline())
    data.append(num)
    i+=1
    
maximum = max(data)
print(maximum)


print(data.index(maximum)+1)



1. max() 함수
2. index() 함수
3. 리스트 컴프리핸션 
(보다 간단하게 쓰기 : 불필요한 변수(여기서는 반복변수를 말함) 쓰지 않기 위해서)
data = [int(sys.stdin.readline().strip()) for _ in range(9)]

------------------------------------
arr = []
for i in range(1,101) :
    if i%2 == 0 :
        arr.apend(1)
print(arr)
------------------------------------
arr = [i for i in range(1,101) if i%2==0]
print(arr)
------------------------------------
list = [수행할 작업 for 아이템 in 객체]
------------------------------------

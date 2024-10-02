a,b,c=map(int, input().split())
list = [a, b, c]
list.sort()

if (list[0]==list[1] and list[1]==list[2]) :
    print(10000+1000*list[0])
if (list[0]==list[1] and list[1]!=list[2]) or (list[0]==list[2] and list[1]!=list[2]) or (list[0]!=list[1] and list[1]==list[2]) :
    print(1000+list[1]*100)
if (list[0]!=list[1] and list[1]!=list[2] and list[0]!=list[2]) :
    print(list[2]*100)
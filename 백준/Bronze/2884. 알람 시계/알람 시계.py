h,m = map(int, input().split())
if h<1 :
    if m<45 :
        print(str(23)+' '+str(60-(45-m)))
    else : print(str(h)+' '+str(m-45))
else : 
    if m<45 :
        print(str(h-1)+' '+str(60-(45-m)))
    else : print(str(h)+' '+str(m-45))
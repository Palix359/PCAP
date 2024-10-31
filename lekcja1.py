klocki = int(input("podaj liczbe klockow"))
floor = 0
height = 0

while klocki > 0:
    floor+=1
    if klocki>=floor:
        height+=1
        klocki-=height
    else:
        break
    
print(height)
    
L=["tekst",'Ala',[1,2],(1,2),3.5]
L=[1,2,3,4,5]
L=[i for i in range(1,11)]
print(L)
print(*L) #print(*L,sep='')
#list slicing
L1=L[:]
L1=L[5:]
L1=L[:5] # 1 2 3 4 5
L1=L[::2] # 1 3 5 7 9 
L1=L[1::2] # 2 4 6 8 10
L1=L[3:6:2] # 4 6
print(*L1)

for i in L:
    print(i,end=' ')
print()
for i in range(len(L)):
    print(L[i],end=' ')
for i in L[:]:
    i=-i
print(L)
N=[-i for i in L]
print(N)

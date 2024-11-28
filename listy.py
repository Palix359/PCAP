import math

L=[x for x in range(1,10)]
print(L)
L.append(999)
print(L)
L.insert(0,111)
L.insert(5,555)
print(L)
print(len(L))
del L[6]
print(L)
print(len(L))
del L
'''
print('Podaj dane ucznia')
D=[x for x in input().split()]
print(D)
print('Podaj liczby')
liczby=[int(x) for x in input().split()]
print(liczby)
'''
#Sortowanie list
# a) metoda sort()
# b) funkcja sorted()
L=[12,0,43,15,22]
#L.sort(reverse=True)
#print(L)
L1=sorted(L)
L1=sorted(L, reverse=True)
print(L1)
L1=L[::-1]
M=['asa','diff','www','ala','zzz','aasa']
print(sorted(M))
print(M)
M.sort()
print(M)
N='aaaswertyzawzs'
#N.sort() --> Nie da się!
print(sorted(N))
print(sorted(M,key=len))
print(sorted(M, reverse=True))
M.sort(key=len, reverse=True)
print(M)
L2=[3,-1,0,-2,1,-3]
#L2.sort()
L2.sort(key=abs)
print(L2)
L3=[[1,2],[-2,4],[0,5],[2,3],[0,1]]
print(sorted(L3))

def dist(A):
    return math.sqrt(A[0]**2+A[1]**2)
print(sorted(L3,key=dist))

try:
    liczba=int(input("Podaj liczbe: "))
    print('Podano liczbe: ',liczba)
    print('Odwrotnosc liczby: ',1/liczba)
    #prin('=-=-=-=-=-=-=-=-=-=') #NameError 
except ZeroDivisionError: #print(1/0)
    print('Nie dzielimy przez zero!')
except ValueError:
    print("Podano nieprawidlowa dana")
except:
    print("Cos poszlo nie tak")

L=[1,2,3,4,5]
# print(L[5]) #IndexError
#L.depend(3) #AttributeError
#print('Hello") #SyntaxError


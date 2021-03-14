



list1 = [1,3,5,7,9,11,13,15,17,19,101]               #tek sayılardan oluşan liste.
list2 = [2,4,6,8,10,12,14,16,18,20,100]              #çift sayılardan oluşan liste.

list = list1+list2                                    #tek sayılardan ve çift sayılardan oluşan listemizden yeni bir liste oluşturduk.
print(list)                                            #ekranda gösterdik.

liste = [i * 2 for i in list]                          #oluşan listedeki her bir değeri 2 ile çarptık.
print(liste)                                           #ekranda gösterdik.


for i in liste:
   print(type(i))                                 #hangi tipte olduğunu belirledik.









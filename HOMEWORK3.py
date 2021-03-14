print("ÖĞRENCİLERİN TÜM BİLGİLERİ AŞAGIDA YER ALMAKTADIR.")

ogrenciler= {'ogr1': 'Ad-Soyad:AYDIN AY '
                         "VİZE NOTU: 60 "
                         "FİNAL NOTU: 73 "
                         "PROJE NOTU: 50 " ,
          'ogr2': 'Ad-Soyad: SELMA VURGUN '
                         "VİZE NOTU: 70 "                           #öğrencilerin bilgilerinin yer aldığı sözlüğü oluşturduk
                         "FİNAL NOTU: 80 "
                         "PROJE NOTU: 63 ",
          'ogr3': 'Ad-Soyad: SUZAN SOYLU '
                         "VİZE NOTU: 90 "
                         "FİNAL NOTU: 59 "
                         "PROJE NOTU: 42 ",
          'ogr4': 'Ad-Soyad: ALİ TAŞ '
                         "VİZE NOTU: 78 "
                         "FİNAL NOTU: 66 "
                         "PROJE NOTU: 81 ",
          'ogr5': 'Ad-Soyad:KENAN ŞİMŞEK  '
                         "VİZE NOTU: 61 "
                         "FİNAL NOTU: 91 "
                         "PROJE NOTU: 73 "
                  }
print(ogrenciler)

ogr1=input("1. öğrenci ad")

try:
    ogr1=string(ogr1)

    print("devam edelim")

except:
    print("lütfen isminizi tam girin!")
    ogr1 = input("1. öğrenci ad")

vize1=float(input("1. ögrenci vize"))                              #5 öğrenciden vize final proje puanlarını istedik
final1=float(input("1. ögrenci final"))
proje1=float(input("1. öğrenci proje"))
passingGrade1= float(vize1*(0.3)+proje1*(0.3)+final1*(0.4))        #aldıkları puan için ortalama hesaplama fonksiyonu yazdık.
print(ogr1 , "yıl sonu notu= " , passingGrade1)

if passingGrade1 >= 60:                                            #dersten geçme notunu belirledik
    print(' dersi geçtiniz',ogr1)
else:                                                              #dersten geçme kalma durumunu sorguladık.
    print('dersten kaldınız',ogr1)

ogr2=input("2. öğrenci ad")

try:
    ogr2=string(ogr2)

    print("devam edelim")

except:
    print(" lütfen isminizi tam girin!")
    ogr2 = input("2. öğrenci ad")

vize2=float(input("2.ögrenci vize"))
final2=float(input("2. ögrenci final"))
proje2=float(input("2.öğrenci proje"))
passingGrade2= float(vize1*(0.3)+proje1*(0.3)+final1*(0.4))
print(ogr2 , "yıl sonu notu= " , passingGrade2)

if passingGrade2 >= 60:
    print(' dersi geçtiniz',ogr2)
else:
    print('dersten kaldınız',ogr2)

ogr3=input("3. öğrenci ad")

try:
    ogr3=string(ogr3)

    print("devam edelim")

except:
    print("lütfen isminizi tam girin!")
    ogr3 = input("3. öğrenci ad")

vize1=float(input("3. ögrenci vize"))
final1=float(input("3. ögrenci final"))
proje1=float(input("3. öğrenci proje"))
passingGrade3= float(vize1*(0.3)+proje1*(0.3)+final1*(0.4))
print(ogr3 , "yıl sonu notu= " , passingGrade3)

if passingGrade3 >= 60:
    print(' dersi geçtiniz',ogr3)
else:
    print('dersten kaldınız',ogr3)

ogr4=input("4. öğrenci ad")

try:
    ogr4=string(ogr4)

    print("devam edelim")

except:
    print("lütfen isminizi tam girin!")
    ogr4 = input("4. öğrenci ad")

vize1=float(input("4. ögrenci vize"))
final1=float(input("4. ögrenci final"))
proje1=float(input("4.öğrenci proje"))
passingGrade4= float(vize1*(0.3)+proje1*(0.3)+final1*(0.4))
print(ogr4 , "yıl sonu notu= " , passingGrade4)

if passingGrade4 >= 60:
    print(' dersi geçtiniz',ogr4)
else:
    print('dersten kaldınız',ogr4)

ogr5=input("5. öğrenci ad")

try:
    ogr5=string(ogr5)

    print("devam edelim")

except:
    print("lütfen isminizi tam girin!")
    ogr5 = input("5. öğrenci ad")

vize1=float(input("5. ögrenci vize"))
final1=float(input("5. ögrenci final"))
proje1=float(input("5. öğrenci proje"))
passingGrade5= float(vize1*(0.3)+proje1*(0.3)+final1*(0.4))
print(ogr5 , "yıl sonu notu= " , passingGrade5)

if passingGrade5 >= 60:
    print(' dersi geçtiniz',ogr5)
else:
    print('dersten kaldınız',ogr5)

list = []                                      #boş bir liste tanımladık
list.append(passingGrade1)                      #öğrencilerin geçme notunu tek tek listeye ekledik
list.append(passingGrade2)
list.append(passingGrade3)
list.append(passingGrade4)
list.append(passingGrade5)

list.sort()                                    #eklediğimiz geçme notlarını önce küçükten büyüğe sıraladık
list.reverse()                                 #geçme notlarını büyükten küçüğe sıraladık.
print(list)                                    #listeyi ekrana bastırdık.







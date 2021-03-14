sorular = ['Hangisi elmasıyla ile ünlü olan ilimizdir ?', 'Hangisi kaşar peyniriyle ile ünlü olan ilimizdir ?',

           'Hangisi etliekmeği ile ünlü olan ilimizdir ?', 'K hangi elementin simgesidir?', 'Hangisi bir Cem Karaca şarkısı değildir?',
           'Osmanlı İmparatorluğu nda Kanuni Sultan Süleyman ın babası?', 'Hangisi 11 in karesidir?', 'Dünyada kaç ülke vardır?', 'Japonların geleneksel güreşine ne ad verilir?',
           'Türkiyenin ilk başbakanı kimdir?']

soru_1_cevaplar = ['A) Mersin', 'B) Amasya', 'C) Yozgat', 'D) Bursa']
soru_2_cevaplar = ['A) Eskişehir', 'B) Konya', 'C) KahramanMaraş', 'D) Ardahan']
soru_3_cevaplar = ['A) Bursa', 'B) Konya', 'C) İstanbul', 'D) Ankara']
soru_4_cevaplar = ['A) Oksijen', 'B) Azot', 'C) Demir', 'D) Potasyum']
soru_5_cevaplar = ['A) Yarım Porsiyon Aydınlık', 'B) Rap Rap', 'C) Tamirci Çırağı', 'D) İstanbul']
soru_6_cevaplar = ['A) Yavuz Sultan Selim', 'B) Fatih sultan Mehmet ', 'C) Orhan Bey ', 'D) 1. Bayezid ']
soru_7_cevaplar = ['A) 111', 'B) 121 ', 'C) 169 ', 'D) 144 ']
soru_8_cevaplar = ['A) 123', 'B) 245 ', 'C) 208 ', 'D) 156 ']
soru_9_cevaplar = ['A) Sumo', 'B) Tekvando ', 'C) Karate ', 'D) Wushu ']
soru_10_cevaplar = ['A) Mustafa Kemal Atatürk', 'B) Fethi Okyar ', 'C) Celal Bayar ', 'D) İsmet İnönü ']
dogru_cevaplar = ['b', 'd', 'b', 'd', 'd', 'a', 'b', 'c', 'a', 'd']

print("10 SORULUK BİLGİ YARIŞMAMIZA HOŞGELDİNİZ...")
x = input("Başlamak için için 0'a basın. ")
if x == "0":
    print("Başlıyoruz...")
else:
    print("Lütfen 0'a basınız!!!")

def sor():
    puan = 0

    print('Soru 1:', sorular[0])

    for x in soru_1_cevaplar:
        print(x)

    cevap_1 = input('Cevabınız Nedir: ')
    try:
        cevap_1 = string(cevap_1)

        print("devam edelim")

    except:
        print("küçük harf  girmelisin!")
        cevap_1 = input("1. sorunun cevabı ")

    if (cevap_1 == dogru_cevaplar[0]):

        print('Tebrikler! Doğru Cevap.')

        puan += 1


    else:

        print('Cevabınız Yanlış. Doğru Cevap b Şıkkı.')

    print('-' * 50)

    print('Soru 2:', sorular[1])

    for x in soru_2_cevaplar:
        print(x)

    cevap_2 = input('Cevabınız Nedir: ')
    try:
        cevap_2 = string(cevap_2)

        print("devam edelim")

    except:
        print("küçük harf  girmelisin!")
        cevap_2 = input("2. sorunun cevabı ")

    if (cevap_2 == dogru_cevaplar[1]):

        print('Tebrikler! Doğru Cevap.')

        puan += 1

    else:

        print('Cevabınız Yanlış. Doğru Cevap d Şıkkı.')

    print('-' * 50)

    print('Soru 3:', sorular[2])

    for x in soru_3_cevaplar:
        print(x)

    cevap_3 = input('Cevabınız Nedir: ')
    try:
        cevap_3 = string(cevap_3)

        print("devam edelim")

    except:
        print("küçük harf  girmelisin!")
        cevap_3 = input("3. sorunun cevabı ")

    if (cevap_3 == dogru_cevaplar[2]):

        print('Tebrikler! Doğru Cevap.')

        puan += 1

    else:

        print('Cevabınız Yanlış. Doğru Cevap b Şıkkı.')

    print('-' * 50)

    print('Soru 4:', sorular[3])

    for x in soru_4_cevaplar:
        print(x)

    cevap_4 = input('Cevabınız Nedir: ')
    try:
        cevap_4 = string(cevap_4)

        print("devam edelim")

    except:
        print("küçük harf  girmelisin!")
        cevap_4 = input("4. sorunun cevabı ")

    if (cevap_4 == dogru_cevaplar[3]):

        print('Tebrikler! Doğru Cevap.')

        puan += 1

    else:

        print('Cevabınız Yanlış. Doğru Cevap d Şıkkı.')

    print('-' * 50)

    print('Soru 5:', sorular[4])

    for x in soru_5_cevaplar:
        print(x)

    cevap_5 = input('Cevabınız Nedir: ')
    try:
        cevap_5 = string(cevap_5)

        print("devam edelim")

    except:
        print("küçük harf  girmelisin!")
        cevap_5 = input("5. sorunun cevabı ")

    if (cevap_5 == dogru_cevaplar[4]):

        print('Tebrikler! Doğru Cevap.')

        puan += 1

    else:

        print('Cevabınız Yanlış. Doğru Cevap d Şıkkı.')

    print('-' * 50)

    print('Soru 6:', sorular[5])

    for x in soru_6_cevaplar:
        print(x)

    cevap_6 = input('Cevabınız Nedir: ')
    try:
        cevap_6 = string(cevap_6)

        print("devam edelim")

    except:
        print("küçük harf  girmelisin!")
        cevap_6 = input("6. sorunun cevabı ")

    if (cevap_6 == dogru_cevaplar[5]):

        print('Tebrikler! Doğru Cevap.')

        puan += 1

    else:

        print('Cevabınız Yanlış. Doğru Cevap a Şıkkı.')

    print('-' * 50)

    print('Soru 7:', sorular[6])

    for x in soru_7_cevaplar:
        print(x)

    cevap_7 = input('Cevabınız Nedir: ')
    try:
        cevap_7 = string(cevap_7)

        print("devam edelim")

    except:
        print("küçük harf  girmelisin!")
        cevap_7 = input("7. sorunun cevabı ")

    if (cevap_7 == dogru_cevaplar[6]):

        print('Tebrikler! Doğru Cevap.')

        puan += 1

    else:

        print('Cevabınız Yanlış. Doğru Cevap b Şıkkı.')

    print('-' * 50)

    print('Soru 8:', sorular[7])

    for x in soru_8_cevaplar:
        print(x)

    cevap_8 = input('Cevabınız Nedir: ')
    try:
        cevap_8 = string(cevap_8)

        print("devam edelim")

    except:
        print("küçük harf  girmelisin!")
        cevap_8 = input("8. sorunun cevabı ")

    if (cevap_8 == dogru_cevaplar[7]):

        print('Tebrikler! Doğru Cevap.')

        puan += 1

    else:

        print('Cevabınız Yanlış. Doğru Cevap c Şıkkı.')

    print('-' * 50)

    print('Soru 9:', sorular[8])

    for x in soru_9_cevaplar:
        print(x)

    cevap_9 = input('Cevabınız Nedir: ')
    try:
        cevap_9 = string(cevap_1)

        print("devam edelim")

    except:
        print("küçük harf  girmelisin!")
        cevap_9 = input("9. sorunun cevabı ")
    if (cevap_9 == dogru_cevaplar[8]):

        print('Tebrikler! Doğru Cevap.')

        puan += 1

    else:

        print('Cevabınız Yanlış. Doğru Cevap a Şıkkı.')

    print('-' * 50)

    print('Soru 10:', sorular[9])

    for x in soru_10_cevaplar:
        print(x)

    cevap_10 = input('Cevabınız Nedir: ')
    try:
        cevap_10 = string(cevap_10)

        print("devam edelim")

    except:
        print("küçük harf  girmelisin!")
        cevap_10 = input("10. sorunun cevabı ")

    if (cevap_10 == dogru_cevaplar[9]):

        print('Tebrikler! Doğru Cevap.')

        puan += 1

    else:

        print('Cevabınız Yanlış. Doğru Cevap d Şıkkı.')

    print('-' * 50)

    print('Yarışmamız bitmiştir. Toplamda {} Soruya Doğru Cevap Verdiniz.'.format(puan))
    input("Doğru sayınızı giriniz:")
    if puan >= 5 :
        print("Tebrikler yarışmayı kazandınız...")
    else:
        print("ÜZGÜNÜM BAŞARILI OLAMADINIZ...")


sor()
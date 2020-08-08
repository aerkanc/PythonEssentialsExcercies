#!/usr/bin/python3
# variables.py by A.Erkan ÇELİK
# Copyright 2020

# değişken ismi özel karakter içeremez
# Değişlken isimleri sadece _ özel karakterini içerebilir
# Değişken isimleri Türkçe karakter içeremez!!!
# değişken isimleri sayı ile  başlayamaz ancak sayı ile devam edebilir.

yok = None
type(yok)

tamsayi = 5
type(tamsayi)

ondalikli_sayi = 5.5
type(ondalikli_sayi)

metin = "Merhaba"
type(metin)

print(metin[0])
print(metin[1])
print(metin[0:2])
print(metin[::-1])
print(metin[3::-1])

ozel_karakterler = "Ekran da yazıldığında görünmeyen <enter> \n gibi karakterleri kullanmak için ters slash kullanılır."
ozel_karakterler2 = "Metin ifadeleri için çift tırnak kullanıyorsak metin içinte tek tırnak (') kullanabiliriz"
ozel_karakterler3 = 'Metin ifadeleri için tek tırnak kullanıyorsak metin içinte çift tırnak (") kullanabiliriz'

asal = [2, 3, 5, 7, 11, 13, 17]  # list
type(asal)

fibonacci = (1, 1, 2, 3, 5, 8, 13, 21, 34)  # tuple
type(fibonacci)

calisan = {
    "boy": 1.75,
    "kilo": 80,
    "adsoyad": "A.Erkan ÇELİK",
    "yetenekler": ["Python", "PHP", "Postgresql"]
}
type(calisan)

bu_gercek_mi = True
type(bu_gercek_mi)


# programlamada genellikte üç tip yazım standardı vardır:

# 1 snake_case
# 2 PascalCase
# 3 camelCase

# python ile yazarken fonksiyon ve değişkenler snake_case
# sınıf isimleri ise PascalCase standardında yazılır.



# 03-logical-operators.py by A.Erkan ÇELİK
# Copyright 2020
# Şart cümleleri, sadece doğru koşullar sağlandığında bir kod bloğunun çalışmasını sağlar

# mantıksal işleçler  boolean (True / False ) sonuç döndüren işleçlerdir.
sayi1 = 16
sayi2 = 7

# KARŞILAŞTIRMA İŞLEÇLERİ
# Eşit mi? ==
sayi1 == sayi2
# sonuç False olacaktır

# Eşit değil mi? !=
sayi1 != sayi2
# sonuç True olacaktır

#Büyük mü? >
sayi1 > sayi2
# sonuç True olacaktır

#Küçük mü? >
sayi1 < sayi2
# sonuç False olacaktır

#Büyük veya Eşit mü? >
sayi1 >= sayi2
# sonuç True olacaktır

#Küçük veya Eşit mü? >
sayi1 <= sayi2
# sonuç False olacaktır

# MANTIKSAL İŞLEM İŞLEÇLERİ
# VE işleci and
False and False # sonuç False
False and True # sonuç False
True and False # sonuç False
True and True # sonuç True

# VEYA işleci or
False or False # sonuç False
False or True # sonuç True
True or False # sonuç True
True or True # sonuç True

# DEĞİL işleci not
not False # sonuç True
not True # sonuç False

# aralığında olma durumu
sayi1 > 9 > sayi2 # sonuç True olacaktır.



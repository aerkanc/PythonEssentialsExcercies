# 02-conditions.py by A.Erkan ÇELİK
# Copyright 2020
# Şart cümleleri, sadece doğru koşullar sağlandığında bir kod bloğunun çalışmasını sağlar

sayi1 = 5
sayi2 = 2

if sayi1 > sayi2:
    print("sayi1, sayi2 den büyüktür")
else:
    print("sayi1, sayi2 den büyük değildir")


if sayi1 > sayi2:
    print("sayi1, sayi2 den büyüktür")
elif sayi2 > sayi1:
    print("sayi2, sayi1 den büyüktür")
else:
    print("sayi1 ve sayi2 eşittir")


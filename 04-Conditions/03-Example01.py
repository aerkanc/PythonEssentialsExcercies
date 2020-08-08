# verilen üç sayı içinden en büyüğünü ve en küçüğünü bulalım
sayi1 = 15
sayi2 = 7
sayi3 = 4
en_buyuk = None
en_kucuk = None

# en büyüğü bulalım
if sayi1 > sayi2 and sayi1 > sayi2:
    en_buyuk = sayi1
elif sayi2 > sayi1 and sayi2 > sayi3:
    en_buyuk = sayi2
else:
    en_buyuk = sayi3

# en küçüğü bulalım

if sayi1 < sayi2 and sayi1 < sayi2:
    en_kucuk = sayi1
elif sayi2 < sayi1 and sayi2 < sayi3:
    en_kucuk = sayi2
else:
    en_kucuk = sayi3

print("%d, %d , %d sayıları içinde en büyük: %d ve en küçük %d dir" % (sayi1, sayi2, sayi3, en_buyuk, en_kucuk))


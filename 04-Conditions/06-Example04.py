# İlk okuma ve son okuma sayaç işaretleri girildiğinde tüketim miktarını ve ödenecek fiyatı hesaplayıp bu bilgileri ekranda gösterecektir.
# Su faturası hesaplaması yapılırken
# 0-15 m3 tüketim için 3.75 TL
# 16-30m3 tüketim için 4.5 TL
# 31m3 ve üzeri tüketim için 5.2 TL
# Birim fiyatı kullanılacak çıkan sonuca %8 KDV eklenecektir.

ilk_okuma = 250
son_okuma = 300
t1, t2, t3 = 0, 0, 0
f1 = 3.75
f2 = 4.5
f3 = 5.2
kdv = .8
fatura = 0

tuketim = son_okuma - ilk_okuma

if tuketim >= 15:
    t1 = 15 * f1
    tuketim = tuketim - 15
else:
    t1 = tuketim * f1

if tuketim > 15:
    t2 = 15 * t2
    tuketim = tuketim - 15
else:
    t2 = tuketim * f2

if tuketim > 0:
    t3 = tuketim * f3

fatura = (t1 + t2 + t3) * (1 + kdv)

print("ilk işareti %d, son işareti %d olan abonenin fatura borcu %d Tl dir" % (ilk_okuma, son_okuma, fatura))

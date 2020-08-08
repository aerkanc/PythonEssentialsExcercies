# Bir sayının asal olup olmadığını bulalım.
# Asal sayı sadece kendisine ve 1’e tam bölünebilen sayıdır.

sayi = 999991

for bolen in range(2, sayi):
    if sayi % bolen == 0:
        print("%d sayısı asal değildir" % sayi)
        exit()

print("%d sayisi asaldır" % sayi)

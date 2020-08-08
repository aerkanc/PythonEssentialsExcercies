# Bir dizinin en büyük sayısını bulalım

dizi = [1, 6, 11, 655, 2, 12, 344, 21, 56, 122, 781, 233, 56, 121, 899, 211, 456, 111, 3]
en_buyuk = dizi[0]
for s in dizi:
    if s > en_buyuk:
        en_buyuk = s

print("Dizideki en büyük sayı: %d" % en_buyuk)

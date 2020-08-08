# 01-function.py by A.Erkan ÇELİK
# Copyright 2020
# aynı kodu tekrar tekrar kullanmamız gerekiyorsa bir kez yazıp tekrar tekrar kullanmak için yordam tanımlanır
def kare(sayi):
    return sayi ** 2


for i in range(1, 10):
    print("%d sayısının karesi %d" % (i, kare(i)))

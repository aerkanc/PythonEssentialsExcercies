import math


def asal_mi(x):
    if x < 2:
        return False
    en_buyuk_bolen = math.floor(math.sqrt(x)) + 1
    for n in range(2, en_buyuk_bolen):
        if x % n == 0:
            return False
    else:
        return True


def asal_sayi_uret(n=2, en_son=3):
    while n < en_son:
        if asal_mi(n):
            yield n
        n += 1


for s in asal_sayi_uret(2, 10000):
    print(s)
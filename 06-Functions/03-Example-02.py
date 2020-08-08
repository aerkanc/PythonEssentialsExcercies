# project euler soru 3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import math


def asal_mi(x):
    if x < 2: return False
    en_buyuk_bolen = math.floor(math.sqrt(x)) + 1
    for n in range(2, en_buyuk_bolen):
        if x % n == 0:
            return False
    else:
        return True


hedef = 600851475143
en_buyuk_asal_bolen = 0
for n in range(2, int(math.sqrt(hedef))):
    if hedef % n == 0 and asal_mi(n):
        en_buyuk_asal_bolen = n
print(en_buyuk_asal_bolen)

# project euler soru 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

bolenler = [ 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def bolunebilir_mi(n):
    for x in bolenler:
        if n % x != 0:
            return False
    return True


sayi = 21
while not bolunebilir_mi(sayi):
    sayi += 1

print(sayi)

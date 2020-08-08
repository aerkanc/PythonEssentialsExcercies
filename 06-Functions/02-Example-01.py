def asal_mi(sayi):
    for i in range(2, sayi):
        if sayi % i == 0:
            return False
    return True


print(asal_mi(158557))
print(asal_mi(585253))
print(asal_mi(2559891))
print(asal_mi(151458875131))

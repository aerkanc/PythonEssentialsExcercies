# Çekilmek istenen bir kredi için
# tutar, faiz ve süre bilgileri ile aylık taksit tutarını hesaplayalım

tutar = 10000
faiz = 1.5
vade = 24

taksit = (tutar * (faiz / 100)) / (1 - 1 / (1 + faiz / 100) ** vade)

print("Aytlık taksit tutarı : %d TL" % taksit)

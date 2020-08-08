# Fibonacci Sayı dizisinin ilk 10 elemanını yazalım

f0 = 1
f1 = 1

for i in range(0,10):
    print("%d. eleman %d" % (i,f0))
    f0, f1 = f1, f0 + f1
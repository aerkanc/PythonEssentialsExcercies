# bir yılın artık yıl olup olmadığını bulalım
# kural: Her 4 yılda bir artık yıl olur ancak 100 yılda bir artık yıl olmaz ancak 400 yılda bir 100 yıl kuralı çalışmaz
yil = 2002
if yil % 400 == 0 or (yil % 100 != 0 and yil % 4 ==0 ):
    print("%d yılı artık yıldır" % yil)
else:
    print("%d yılı artık yıl değildir" % yil)


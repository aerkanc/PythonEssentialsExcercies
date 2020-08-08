# yönü ve deracesi bilinen iki meridyen arasındaki zaman farkını saat ve dakika cinsinden hesaplayalım
import math

m1 = 26
m2 = 45
y1 = "Doğu"
y2 = "Doğu"
fark = None
zaman = None
saat = None
dk = None

if y1 == y2:
    fark = math.fabs(m1 - m2)
else:
    fark = m1 + m2

zaman = fark * 4  # dakika cinsinden zaman farkı

saat = zaman // 60
dk = zaman % 60

print("%d %s meridyeni ile %d %s meridyeni arasındaki zaman farkı %d saat %d dakikadır" % (m1, y1, m2, y2, saat, dk))

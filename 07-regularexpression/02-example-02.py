# Turgut Uyar'ın denge şiiri
import re

siir = """DENGE
(Tel cambazının tel üstündeki durumunu anlatır şiirdir)

Sizin alınız al, inandım. 
Morunuz mor, inandım. 
Tanrınız büyük, âmenna. 
Şiiriniz adamakıllı şiir, 
Dumanı da caba.
Ama sizin adınız ne
Benim dengemi bozmayınız.

Bütün ağaçlarla uyuşmuşum, 
Kalabalık ha olmuş, ha olmamış. 
Sokaklarda yitirmiş, cebimde bulmuşum. 
Ama sokaklar şöyleymiş, 
Ağaçlar böyleymiş, 
Ama sizin adınız ne
Benim dengemi bozmayınız.

Aşkım da değişebilir, gerçeklerim de. 
Pırılpırıl dalgalı bir denize karşı 
Yangelmişim dizboyu sulara, 
Hepinize iyi niyetle gülümsüyorum, 
Hiçbirinizle döğüşemem.
Siz ne derseniz deyiniz 
Benim bir gizli bildiğim var, 
Sizin alınız al inandım, 
Sizin morunuz mor inandım, 
Ben tam dünyaya göre, 
Ben tam kendime göre, 
Ama sizin adınız ne
Benim dengemi bozmayınız.

Turgut Uyar
(1927 - 1985)

Büyük Saat, S. 119
"""

for misra in siir.split("\n"):
    eslesme = re.search("(siz|ben|denge)", misra, re.IGNORECASE)
    if eslesme:
        print(misra.replace(eslesme.group(), "###"))

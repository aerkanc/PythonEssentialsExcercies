class dortgen():
    genislik = 1
    yukseklik = 1
    karakter = '#'

    def ciz(self):
        for i in range(0, self.yukseklik):
            # soldaki çizgi
            print(self.karakter, end='')
            # aradaki çizgiler
            if i == 0 or i == self.yukseklik - 1:
                k = self.karakter
            else:
                k = ' '

            for j in range(1, self.genislik):
                print(k, end='')
            # sağdaki çizgi
            print(self.karakter, end='')
            print("")


class kare(dortgen):
    def __setattr__(self, key, value):
        if key == 'genislik':
            self.yukseklik = value
        super().__setattr__(key, value)


d = dortgen()
d.genislik = 15
d.yukseklik = 10
d.ciz()

k = kare()
k.genislik = 10
k.ciz()

class insan():
    isim = "İsimsiz"
    boy = 170
    agirlik = 75
    yas = 30
    sac_rengi = "Kahverengi"

    def yuru(self):
        print("%s Yürüdü" % self.isim)


erkan = insan()
erkan.isim = "Erkan"
erkan.boy = 175
erkan.agirlik = 80
erkan.yas = 41
erkan.sac_rengi = 'Siyah'
erkan.yuru()

ali = insan()
ali.isim = "Ali"
ali.boy = 195
ali.agirlik = 85
ali.yas = 25
ali.yuru()

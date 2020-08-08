# 01-regulatexpression.py by A.Erkan ÇELİK
# Copyright 2020

import re

metin = "python'u çok iyi kullananlara pythonist denir"

if re.search("python", metin):
    print("metin python kelimesi içeriyor")
else:
    print("metin python kelimesi içermiyor")
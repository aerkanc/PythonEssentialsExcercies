d = {"bir": 1, "iki": 2, "üç": 3}
print(d)
# {"bir": 1, "iki": 2, "üç": 3}

d1 = dict(bir=1, iki=2, üç=3)
print(d1)
# {"bir": 1, "iki": 2, "üç": 3}

type(d1)
# <class 'dict'>

d2 = {'dört': 4, "beş": 5, "altı": 6}

d3 = dict(**d2, **d1)
print(d3)
# {'dört': 4, 'beş': 5, 'altı': 6, 'bir': 1, 'iki': 2, 'üç': 3}

print('dört' in d3)
# True

print('yedi' in d3)
# False

for k in d3:
    print(k)
# dört
# beş
# altı
# bir
# iki
# üç

for k, v in d3.items():
    print(k, v)
# dört 4
# beş 5
# altı 6
# bir 1
# iki 2
# üç 3

print(d3["üç"])
# 3

# print(d2["üç"])
# Traceback (most recent call last):
#   File "D:/Kullanici Dosyalari/Workspaces/Python/PythonEssentialsExcercies/09-cantainers/03-dictionaries.py", line 45, in <module>
#     print(d2["üç"])
# KeyError: 'üç'

print(d2.get("üç"))
# None

print(d1.get("üç"))
# 3

print(d2.get("üç", "Bulunamadı"))
# Bulunamadı


del d2['dört']
print(d2)
# {'beş': 5, 'altı': 6}

print(d2.pop("beş"))
# 5
print(d2)
# {'altı': 6}

d3['yedi'] = 7
print(d3)
# {'dört': 4, 'beş': 5, 'altı': 6, 'bir': 1, 'iki': 2, 'üç': 3, 'yedi': 7}

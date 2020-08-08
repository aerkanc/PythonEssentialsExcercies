# project euler soru 4
# A palindromic sayi reads the same both ways. The largest palindrome made from the product of two 2-digit sayis is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit sayis.

def palindromic_mi(n):
    strn = str(n)
    return strn == strn[::-1]


en_buyuk_palindrome = 0
sayi = 0
for f in range(99, 999):
    for n in range(99, 999):
        sayi = n * f
        if palindromic_mi(sayi) and en_buyuk_palindrome < sayi:
            largestPalindrome = sayi
print(en_buyuk_palindrome)

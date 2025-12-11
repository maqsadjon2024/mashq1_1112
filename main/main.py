#1
kvadratlar = {x**2 for x in range(1, 21)}
print(kvadratlar)

#2
words = ["Salom", "Dunyo", "KITOB", "Python"]
kichik = {w.lower() for w in words}
print(kichik)

#3
yigindi10 = {x for x in range(1, 101) if sum(int(d) for d in str(x)) == 10}
print(yigindi10)

#4
matn = "Assalomu alaykum, Python dunyosi!"
unlilar = {harf for harf in matn.lower() if harf in "aeiouöüoauiy"}
print(unlilar)

#5
sonlar = [-20, -5, 0, 5, 10, 13, 25, 40, -15]
natija = {x for x in sonlar if x > 0 and x % 5 == 0}
print(natija)

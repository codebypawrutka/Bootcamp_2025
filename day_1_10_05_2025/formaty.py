#W Pythonie masz kilka sposobów formatowania tekstu i liczb — używane przy tworzeniu czytelnych komunikatów, tabel, raportów, itp. Poniżej przedstawiam kompletne zestawienie wraz z przykładami.

# #✅ 1. Stare formatowanie % (styl C)
# python
# Kopiuj
# Edytuj
name = "Ala"
age = 10
print("Mam na imię %s i mam %d lat." % (name, age))
# Specyfikatory:
#
# %s – string
#
# %d – liczba całkowita
#
# %f – liczba zmiennoprzecinkowa
#
# %.2f – liczba zmiennoprzecinkowa z 2 miejscami po przecinku
#
# ✅ 2. str.format() (Python 2.6+ / 3.x)
# python
# Kopiuj
# Edytuj
name = "Ala"
age = 10
print("Mam na imię {} i mam {} lat.".format(name, age))
# Z opcjami:
#
# python
# Kopiuj
# Edytuj
pi = 3.14159
print("Pi = {:.2f}".format(pi))      # Pi = 3.14
print("{:>10}".format("Hello"))      # Hello wyrównane do prawej
print("{:<10}".format("Hello"))      # Hello wyrównane do lewej
print("{:^10}".format("Hello"))      # Hello wyśrodkowane

# Numerowane indeksy:
#
# python
# Kopiuj
# Edytuj
print("Imię: {0}, Wiek: {1}, Imię: {0}".format(name, age))
# ✅ 3. F-stringi (Python 3.6+) – najlepsze i najszybsze
# python
# Kopiuj
# Edytuj
name = "Ala"
age = 10
pi = 3.14159
print(f"Mam na imię {name} i mam {age} lat.")
print(f"Pi zaokrąglone: {pi:.2f}")
print(f"{'tekst':^10}")  # wyśrodkowany w polu 10 znaków
# ✅ 4. format() liczbowy – typy formatowania
# Typ	Znaczenie	Przykład
# d	liczba całkowita	f"{42:d}" → 42
# f	float z domyślną precyzją	f"{3.14159:f}" → 3.141590
# .2f	float z 2 miejscami	f"{3.14159:.2f}" → 3.14
# e	zapis wykładniczy	f"{1500:e}" → 1.500000e+03
# b	binarnie	f"{10:b}" → 1010
# o	ósemkowo	f"{10:o}" → 12
# x	szesnastkowo (małe litery)	f"{255:x}" → ff
# X	szesnastkowo (duże litery)	f"{255:X}" → FF
# %	procent	f"{0.25:%}" → 25.000000%
#
# ✅ 5. Zera, odstępy, wyrównanie, znaki
# python
# Kopiuj
# Edytuj
num = 42
print(f"{num:05}")     # 00042 (wypełnienie zerami)
print(f"{num:<5}")     # '42   ' (lewo)
print(f"{num:>5}")     # '   42' (prawo)
print(f"{num:^5}")     # ' 42  ' (środek)
print(f"{-42:+d}")     # -42
print(f"{42:+d}")      # +42
# ✅ 6. Przykład praktyczny – tabela
# python
# Kopiuj
# Edytuj
for i in range(1, 6):
    print(f"{i:^3} | {i**2:^5} | {i**3:^5}")
# Kopiuj
# Edytuj
#  1  |  1   |  1
#  2  |  4   |  8
#  3  |  9   | 27
#  4  | 16   | 64
#  5  | 25   |125
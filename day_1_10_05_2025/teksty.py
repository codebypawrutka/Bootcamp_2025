tekst = "Witaj Świecie"

print(tekst)
print(type(tekst))
# Witaj Świecie
# <class 'str'>

# pula tekstów - teksty są niemutowalne
tekst.upper()
""" Return a copy of the string converted to uppercase. """
print(tekst)  # Witaj Świecie
print(tekst.upper())  # WITAJ ŚWIECIE
print(tekst)  # Witaj Świecie
tekst_upper = tekst.upper()
print(tekst_upper)  # WITAJ ŚWIECIE

# lower()
print(tekst.lower())  # witaj świecie

name = "Radek"
#       01234 - indeksowanie od zera

print(name[0])  # R
print(name[1])  # a
print(name[2])  # d
print(name[3])  # e
print(name[4])  # k
# print(name[5])  # IndexError: string index out of range
print(len(name))  # len() - długość tekstu, 5

# slicowanie - fragment tekstu
print(name[2:4])  # de, tylko indeksy 2, 3, z prawej strony otwarty (niewłącznie)
print(name[:4])  # Rade 0,1,2,3 indeksy
print(name[:])  # Radek

str1 = "HELLO WORLD"
# teksty są niemutowalne
# str1[0:5] = "HOLAA" # TypeError: 'str' object does not support item assignment
print(str1)  # HELLO WORLD

my_str = "  Hello Everyone  "
print(my_str)  # "  Hello Everyone  "
print(my_str.strip())  # "Hello Everyone" - strip() - usunięcie białych znaków, wiodących, końcowych spacji
print(my_str.rstrip())  # "  Hello Everyone" - usunięcie po prawej stronie
print(my_str.lstrip())  # "Hello Everyone  " - usnięcie po lewej strone

my_str2 = "***Hello****World***"
print(my_str2.strip("*"))  # Hello****World
print(my_str2.rstrip("*"))  # ***Hello****World
print(my_str2.lstrip("*"))  # Hello****World***
print(my_str)  # "  Hello Everyone  "
print(my_str2)  # "***Hello****World***"

print(tekst)
# Witaj Świecie
# 0123456789012

print(tekst.removeprefix("Witaj"))  # " Świecie" Funkcja tekst.removeprefix() w języku Python służy do usuwania określonego prefiksu (początkowego fragmentu) ze stringa, jeśli taki występuje.
tekst = "autobus"
nowy = tekst.removeprefix("auto")
print(nowy)  # wynik: "bus"


print(tekst.removesuffix("Świecie"))  # Witaj  Funkcja tekst.removesuffix() w Pythonie służy do usuwania określonego sufiksu (końcówki) ze stringa, jeśli taka końcówka występuje.

plik = "raport.txt"
nazwa = plik.removesuffix(".txt")
print(nazwa)  # wynik: "raport"




print(tekst.count("i"))  # występuje 3 razy
print(tekst.count("i", 0, 4))  # 1 wystepuje 1 raz
print(tekst.count("j", 0, 4))  # wystepuje 0 razy bo indeksy 0123
print(tekst.index("j"))  # 4
    

print(my_str2)  # ***Hello****World***
# zamiana tekstu
print(my_str2.replace("He", 'Ho'))  # ***Hollo****World*** Funkcja replace() w Pythonie służy do zamiany fragmentów tekstu (ciągów znaków) w stringach.

print(my_str)  # "  Hello Everyone  "
print(my_str.replace(" ", ""))  # HelloEveryone
print(my_str.center(40))  # wycentrowanie tekstu podczas wypisywania
# "             Hello Everyone             "

print("Mój ulubiony serial \"Alternatywy 4\"")  # Mój ulubiony serial "Alternatywy 4"
print('Mój ulubiony serial "Alternatywy 4"')  # Mój ulubiony serial "Alternatywy 4"
# \ - w stringach znak ucieczki oznacza nie interpretuj kolejnego znaku tylko po prostu wyświetl

imie = "Radek"
# f-string - sformatowany tekst
formatted_text = f"Mam na imię {imie} i lubię Pythona."
print(formatted_text)  # Mam na imię Radek i lubię Pythona.

formatted_text_2 = f"\tMam na imię {imie}\n i lubię Pythona.\b"
print(formatted_text_2)
# " 	Mam na imię Radek
#  i lubię Pythona"
# \n - Nowa linia
# \t - Tabulacja pozioma
# \b - Powrót kursora (usuwa poprzedni znak)

# starszy sposób wstrzykiwania zmiennej do tekstu
starszy = "Witaj %s!"  # w miejsce %s podstawi wartość zmiennej str
print(starszy % name)  # Witaj Radek!
# %s - łańcuch znaków (string)
# %d - liczba całkowita (integer)
# %i - liczba całkowita (integer)

print("Witaj {}!".format(imie))  # Witaj Radek!

print("Witaj", name)  # Witaj Radek

print("""Tekst
    wielolinijkowy""")
# "Tekst
#     wielolinijkowy"
# WYSWIG

"""Komentarz
 wielolinijkowy"""
# Process finished with exit code 0

# kodowanie znaków
encoded_s = tekst.encode("utf-8")
print(encoded_s)  # b'Witaj \xc5\x9awiecie'
print(type(encoded_s))  # <class 'bytes'>, typ bajtowy
# b - typ bajtowy
# \xc5\x9a - kod szesnatkowy znaku Ś, \xc5 -> 197
print(encoded_s.decode('utf-8'))  # Witaj Świecie

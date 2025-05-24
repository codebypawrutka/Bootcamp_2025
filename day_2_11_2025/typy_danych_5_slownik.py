# W Pythonie słownik (dict) to kolekcja par klucz–wartość. Jest to jedna z najważniejszych struktur danych w języku Python — bardzo szybka i elastyczna.
#
# 🧠 Czym jest słownik (dict)?
# Klucze muszą być unikalne i niezmienne (np. liczby, stringi, tuple).
#
# Wartości mogą być dowolne (inne słowniki, listy, liczby, itd.).
#
# Możesz szybko odczytać wartość na podstawie klucza.
#
# ✅ Tworzenie słownika

osoba = {
    "imie": "Ala",
    "wiek": 10,
    "miasto": "Kraków"
}
# 🔍 Dostęp do wartości

print(osoba["imie"])     # Ala
#✔️ Bezpieczny dostęp (bez błędu przy braku klucza):


print(osoba.get("kraj", "brak danych"))  # brak danych
#🛠️ Dodawanie i modyfikowanie

osoba["kraj"] = "Polska"           # dodanie nowej pary
osoba["wiek"] = 11                 # modyfikacja istniejącej

#❌ Usuwanie elementów

del osoba["miasto"]                # usuwa klucz
osoba.pop("wiek")                  # usuwa i zwraca wartość
osoba.clear()                      # czyści cały słownik

#🔁 Iterowanie po słowniku

for klucz in osoba:
    print(klucz, osoba[klucz])
#Lub:


for klucz, wartosc in osoba.items():
    print(f"{klucz} => {wartosc}")
# 📚 Metody słowników – najważniejsze
# Metoda	Działanie
# dict.get(klucz)	Zwraca wartość lub None (lub domyślną)
# dict.keys()	Zwraca wszystkie klucze
# dict.values()	Zwraca wszystkie wartości
# dict.items()	Zwraca listę (klucz, wartość)
# dict.update(inny_dict)	Aktualizuje słownik
# dict.pop(klucz)	Usuwa i zwraca wartość
# dict.clear()	Usuwa wszystko
# klucz in dict	Sprawdza czy klucz istnieje
#
# 🧪 Przykłady zaawansowane
# Zagnieżdżone słowniki:

uczen = {
    "imie": "Ola",
    "oceny": {"matematyka": 5, "polski": 4}
}
print(uczen["oceny"]["matematyka"])  # 5

#Liczenie wystąpień:

tekst = "ala ma kota"
wystapienia = {}
for znak in tekst:
    wystapienia[znak] = wystapienia.get(znak, 0) + 1
print(wystapienia)

#🔁 1. Konwersja listy par (tupli) do słownika

pary = [("a", 1), ("b", 2), ("c", 3)]
slownik = dict(pary)
print(slownik)  # {'a': 1, 'b': 2, 'c': 3}

#📋 2. Słownik z listami jako wartościami

uczniowie = {
    "Ala": [5, 4, 3],
    "Bartek": [3, 3, 4],
    "Celina": [5, 5, 5]
}
print(uczniowie["Ala"])        # [5, 4, 3]
print(sum(uczniowie["Celina"]))  # suma ocen: 15
#📊 3. Sortowanie słownika

#Po kluczach:

d = {"b": 2, "a": 5, "c": 1}
for k in sorted(d):
    print(k, d[k])

#Po wartościach:

for k, v in sorted(d.items(), key=lambda x: x[1]):
    print(k, v)
#📈 4. Licznik wystąpień znaków / słów

tekst = "ala ma kota ala lubi kota"
licznik = {}

for slowo in tekst.split():
    licznik[slowo] = licznik.get(slowo, 0) + 1

print(licznik)  # {'ala': 2, 'ma': 1, 'kota': 2, 'lubi': 1}

#🧊 5. Słownik z domyślną wartością (defaultdict)
#Jeśli chcesz automatycznie tworzyć listy lub liczniki:


from collections import defaultdict

slownik = defaultdict(list)
slownik["a"].append(1)
slownik["a"].append(2)
print(slownik)  # {'a': [1, 2]}
#📑 6. Zamiana kluczy z wartościami

oryginal = {"a": 1, "b": 2, "c": 3}
odwrocony = {v: k for k, v in oryginal.items()}
print(odwrocony)  # {1: 'a', 2: 'b', 3: 'c'}

#----------------------------------------------------------------------
my_dict5 = {"Name": "Radek","ID":12345, "DDB": 1991, 'Address': "Warsaw"}
print(my_dict5) #{'Name': 'Radek', 'ID': 12345, 'DDB': 1991, 'Address': 'Warsaw'}
print(my_dict5['DDB']) #1991
print(my_dict5.get('DDB')) # 1991

# nadpisanie wartości dla klucza
my_dict5['DDB'] = '1980'
print(my_dict5) #{'Name': 'Radek', 'ID': 12345, 'DDB': '1980', 'Address': 'Warsaw'}
print(type(my_dict5['DDB']))  # <class 'str'>

my_dict5['Address'] = "Warsaw Centrum"
print(my_dict5) # {'Name': 'Radek', 'ID': 12345, 'DDB': '1980', 'Address': 'Warsaw Centrum'}

dict1 = {"DDB": 1995}
print(dict1) # {'DDB': 1995}
print(type(dict1)) # <class 'dict'>

#update słownik innym słownikiem
my_dict5.update(dict1)
print(my_dict5)
#{'Name': 'Radek', 'ID': 12345, 'DDB': 1995, 'Address': 'Warsaw Centrum'}

dict2 = {'cpi': 3.41} # float, liczby
print(dict2) #{'cpi': 3.41}

# update słownika
# jesli klucz w docelowym słowniku nieistnieje zostanie dodany
# docelowy słownik my_dict5

my_dict5.update(dict2)
print(my_dict5)
#{'Name': 'Radek', 'ID': 12345, 'DDB': 1995, 'Address': 'Warsaw Centrum', 'cpi': 3.41}

# usuniecie elementu ze słownika
print(my_dict5.pop("cpi")) # {'Name': 'Radek', 'ID': 12345, 'DDB': 1995, 'Address': 'Warsaw Centrum', 'cpi': 3.41}   3.41

#usunięcie ostatniego elementu ze słownika
print(my_dict5.popitem())
print(my_dict5) #('Address', 'Warsaw Centrum')
#{'Name': 'Radek', 'ID': 12345, 'DDB': 1995}

#usunięcie po kluczu
del my_dict5['ID']
print(my_dict5)

#usunięcie wszystkich elementów ze słownika

my_dict5.clear()
print(my_dict5)

# usunięcie z pamięci
del my_dict5
# my_dict5 nie istnieje - został usunięty z pamięci

# zamiana klucza w słowniku



# kopiowanie słownika
my_dict5 = {'Name': 'Radek', 'ID': 12345, 'DDB': 1995, 'Address': 'Warsaw Centrum', 'cpi': 3.41}
#kopia referencji
my_dict5_copy_ref = my_dict5
print(id(my_dict5_copy_ref))
print(id(my_dict5))

# kopia elementów słownka do drugiego słownika
my_dict5_copy = my_dict5.copy()
my_dict5


# napisac program który bedzie dzialal jak słownik  angielsko - polski
# wyświetla dostępne słowa
# pobiera słowo od użytkownika
# wyświetla tłumaczenie
# input() - pobiera dane od użytkownika

#odp = input("Podaj imię")
#print(odp)



slownik = {
    "book": "książka",
    "pencil": "ołówek",
    "house": "dom",
    "red": "czerwony"
}
wyraz = input("Podaj  słowo do tłumaczenia: ").lower()
print("Po angielsku:", slownik.get(wyraz, "Brak tłumaczenia"))

ang_pol = {'name': 'imie', "cat": "kot", 'water': "woda"}
print('---------Słownik pol-----------')
print("Mamy takie slowko w slowniku", ang_pol.keys())
odp = input("Podaj słowko do przetłumaczenia")

print(f"{odp.strip().casefold()} to: {ang_pol[odp.strip().casefold())}")
print(f"{odp.strip().casefold()} to: {ang_pol[odp.strip().casefold(), "NIe ma w słowniku")}")

 a= input("Podaj liczbe")
 print(a)
 a = float(input"Podaj liczbe")








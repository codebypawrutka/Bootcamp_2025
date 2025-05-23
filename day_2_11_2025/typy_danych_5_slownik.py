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
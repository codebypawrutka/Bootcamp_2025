# instrukcje warunkowe
# instrukcja sterowania przepływem programu
# if - sterowana warunkiem
#if warunek:
# komenda(blok) wykonywany gdy warunek spełniony

#odp = False
#print(bool(odp))

#if odp:
#    print("Brawo")

#print("Dalsza część programu")

# odp = "Radek"
# if odp:
#     print("ok")
#
# odp ="Tomek"
# if odp == "Radek":
#     print("Radek")
# else: # w przeciwnym przypadku
#     print("Inny pacjent") # Inny pacjent
#
# podatek = 0.9
# zarobki = int(input("Podaj dochód"))
# po pierwszym spełnionym warunku wychodzi z drzewka
# kolejność warunków ma znaczenie
# if zarobki < 10000:
#     podatek = 0.0
# elif zarobki < 100000:
#     podatek = 0.4
#     if zarobki < 1999:
#         podatek = 0
#
# elif zarobki < 30_000:
#     podatek = 0.2
# else:
#     podatek = 0.9
#
# print(f"Płacisz {zarobki * podatek} podatek")


suma_zam = 250
if suma_zam > 150:
    rabacik = 25
else:
    rabacik = 0

print(f"Rabat wynosi {rabacik}")
rabat = 25 if suma_zam > 150 else 0
print(f"Rabat wynosi {rabat}")




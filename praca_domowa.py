print("PROGRAM DO OBSLUGI LADOWARKI PACZEK")
import random
print()
ilosc_elementow = int(input("Ile chcesz wyslac elementow? "))
ilosc_wyslanyc_kg = 0
numer_aktalnej_paczki = 1
ilosc_kg_w_paczke = 0
najwiecej_pustych_kg= 0
numer_paczki_max_puste_kg = 1
summa_pustych_kg = 0
print()
for i in range(ilosc_elementow):
    waga_kg = random.randint(1, 10)
    ilosc_wyslanyc_kg += waga_kg
    print(f"Element{i + 1}: {waga_kg} ma kg")
    if ilosc_kg_w_paczke + waga_kg > 20:
            puste_kg_tej_paczki = 20 - ilosc_kg_w_paczke
            print(f"Paczka {numer_aktalnej_paczki} zapelniona: {ilosc_kg_w_paczke} kg, pozostaly puste kg : {puste_kg_tej_paczki} ")
            summa_pustych_kg += puste_kg_tej_paczki
            if puste_kg_tej_paczki > najwiecej_pustych_kg :
                najwiecej_pustych_kg = puste_kg_tej_paczki
                numer_paczki_max_puste_kg = numer_aktalnej_paczki
                numer_aktalnej_paczki += 1
            ilosc_kg_w_paczke = waga_kg
    else :
        ilosc_kg_w_paczke += waga_kg


puste_kg_ostatniej_paczki = 20 - ilosc_kg_w_paczke
summa_pustych_kg += puste_kg_ostatniej_paczki
print (f"Paczka {numer_aktalnej_paczki} zapelniona: {ilosc_kg_w_paczke} kg, pozostaly puste kg: {puste_kg_ostatniej_paczki} ")
if puste_kg_ostatniej_paczki> najwiecej_pustych_kg :
    najwiecej_pustych_kg = puste_kg_ostatniej_paczki
    numer_paczki_max_puste_kg = numer_aktalnej_paczki

print()
print (f"Wyslano : {numer_aktalnej_paczki} paczek")
print (f"Wyslano elementow: {ilosc_elementow} z  { ilosc_wyslanyc_kg} kg")
print(f"Najwiecej pustych kg  ma paczka {numer_paczki_max_puste_kg} : {najwiecej_pustych_kg} kg")
print(f"Suma pustych kilogramów: {summa_pustych_kg} kg")


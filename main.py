import random
import matplotlib.pyplot as plt
import numpy as np


# Parametry problemu plecakowego
pojemnosc_plecaka = 50
wagi = [10, 20, 30, 15, 5]  # Wagi przedmiotów
wartosci = [40, 50, 60, 30, 10]  # Wartości przedmiotów
ilosc_przedmiotow = len(wagi)

# Parametry algorytmu genetycznego
liczba_generacji = 100
liczba_osobnikow = 50
szansa_mutacji = 0.1

def stworz_osobnika():
    return [random.randint(0, 1) for _ in range(ilosc_przedmiotow)] #zwraca 1 jesli osobnik wystąpi w plecaku, 0 jeśli nie wystąpi.
# przykladowy output: 10110

def oblicz_wartosc(osobnik):
    return sum(wartosci[i] for i in range(ilosc_przedmiotow) if osobnik[i] == 1) #liczymy sume tablicy "wartosci", uzywaj
#ąc elementów które odpowiadają 1 w stworzonym wcześniej osobniku
#przykladowy output: 40+0+60+30+0 = 130.

def oblicz_wage(osobnik):
    return sum(wagi[i] for i in range(ilosc_przedmiotow) if osobnik[i] == 1) #liczymy sume wag

def selekcja(populacja):
    populacja.sort(key=lambda x: oblicz_wartosc(x), reverse=True) #bierzemy populacje osobników,
    #dla każdego obliczamy wartość, sortujemy malejąco
    return populacja[:int(0.5 * len(populacja))] #ZAUWAŻ DWUKROPEK- zwracamy pierwszą połowę populacji.

def krzyzowanie(rodzice):
    punkt_przeciecia = random.randint(1, ilosc_przedmiotow - 1)
    dziecko1 = rodzice[0][:punkt_przeciecia] + rodzice[1][punkt_przeciecia:]#sklejany jest osobnik dziecięcy- z dwóch
    #chromosomów rodziców, np: czesc matki: 101  czesc ojca:00 -> powstaje dziecko -> 10100
    dziecko2 = rodzice[1][:punkt_przeciecia] + rodzice[0][punkt_przeciecia:]
    return dziecko1, dziecko2

def mutacja(osobnik):
    indeks_mutacji = random.randint(0, ilosc_przedmiotow - 1)
    osobnik[indeks_mutacji] = 1 - osobnik[indeks_mutacji]
    return osobnik # ta metoda losowo decyduje czy pojedynczy fragment chromosomu danego osobnika zostanie zamieniony.
    #na przyład zmieniamy 2 element chromosomu w osobniku a więc przed mutacją osobnik= 11001, po mutacji: 11101.

# Algorytm genetyczny
populacja = [stworz_osobnika() for _ in range(liczba_osobnikow)] #tworzymy populacje osobników. w tym przypadku 50.

for generacja in range(liczba_generacji):
    populacja = selekcja(populacja) #populacja to zbiór 50 osobników, generacja to zbiór populacji.

    nowa_populacja = []
    while len(nowa_populacja) < liczba_osobnikow:
        rodzice = random.sample(populacja, 2)
        dziecko1, dziecko2 = krzyzowanie(rodzice)

        if random.random() < szansa_mutacji:
            dziecko1 = mutacja(dziecko1)
        if random.random() < szansa_mutacji:
            dziecko2 = mutacja(dziecko2)

        nowa_populacja.append(dziecko1)
        nowa_populacja.append(dziecko2)

    populacja = nowa_populacja
    #print(tab_wartośći)

najlepszy_osobnik = max(populacja, key=lambda x: oblicz_wartosc(x))
najlepsza_wartosc = oblicz_wartosc(najlepszy_osobnik)
najlepsza_waga = oblicz_wage(najlepszy_osobnik)

print("Najlepsza wartość:", najlepsza_wartosc)
print("Najlepsza waga:", najlepsza_waga)
print("Najlepszy osobnik:", najlepszy_osobnik)

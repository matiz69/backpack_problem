import random

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
    return [random.randint(0, 1) for _ in range(ilosc_przedmiotow)]

def oblicz_wartosc(osobnik):
    return sum(wartosci[i] for i in range(ilosc_przedmiotow) if osobnik[i] == 1)

def oblicz_wage(osobnik):
    return sum(wagi[i] for i in range(ilosc_przedmiotow) if osobnik[i] == 1)

def selekcja(populacja):
    populacja.sort(key=lambda x: oblicz_wartosc(x), reverse=True)
    return populacja[:int(0.5 * len(populacja))]

def krzyzowanie(rodzice):
    punkt_przeciecia = random.randint(1, ilosc_przedmiotow - 1)
    dziecko1 = rodzice[0][:punkt_przeciecia] + rodzice[1][punkt_przeciecia:]
    dziecko2 = rodzice[1][:punkt_przeciecia] + rodzice[0][punkt_przeciecia:]
    return dziecko1, dziecko2

def mutacja(osobnik):
    indeks_mutacji = random.randint(0, ilosc_przedmiotow - 1)
    osobnik[indeks_mutacji] = 1 - osobnik[indeks_mutacji]
    return osobnik

# Algorytm genetyczny
populacja = [stworz_osobnika() for _ in range(liczba_osobnikow)]

for generacja in range(liczba_generacji):
    populacja = selekcja(populacja)

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

najlepszy_osobnik = max(populacja, key=lambda x: oblicz_wartosc(x))
najlepsza_wartosc = oblicz_wartosc(najlepszy_osobnik)
najlepsza_waga = oblicz_wage(najlepszy_osobnik)

print("Najlepsza wartość:", najlepsza_wartosc)
print("Najlepsza waga:", najlepsza_waga)
print("Najlepszy osobnik:", najlepszy_osobnik)

# import numpy as np
import cupy as cp
#import sympy as sp
from statistics import mean
import string
import random


# ------- Zad 1 ----------------------------------------------------
# input in Celsius
def convert_temp(x):
    if isinstance(x, (int, float)): #sprwdza czy x jest int lub float lub nie
        f = 1.8 * x + 32 #zamiana z C na F
        print(f"Temperatura {x} deg C to {f} F")
    else:        
        print("Błąd: podana wartość nie jest liczbą")
#sprawdzenie
convert_temp(0)
convert_temp(25)


# ------- Zad 2 ----------------------------------------------------
def usun_duplikaty(sekwencja):
    unikalne = sorted(set(sekwencja))
    for liczba in unikalne:
        ile = sekwencja.count(liczba)
        print(f"{liczba} występuje {ile} razy")
#sprawdzenie
usun_duplikaty([1, 2, 3, 2, 4, 1, 5])


# ------- Zad 3 ----------------------------------------------------
znajdz_pierwszy = lambda sekwencja, pierwszy: print("Are they equal?: ", sekwencja[0] == pierwszy)
#sprawdzenie
znajdz_pierwszy([2,1], 1) 


# ------- Zad 4 ----------------------------------------------------
def isPrime(liczba):
    if liczba < 2:
        return False
    elif liczba == 2:
        return True
    else:
        for n in range(2, liczba):
            if liczba % n == 0:
                return False
    return True

def liczby_pierwsze(x):
    for i in range (1, x + 1):
        if isPrime(i):
            print(i)

#sprawdzenie
liczby_pierwsze(20)


# ------- Zad 5 ----------------------------------------------------
def statystyki(lista_liczb):
    min_ = min(lista_liczb)
    max_ = max(lista_liczb)
    suma_ = sum(lista_liczb)
    srednia_ = suma_ / len(lista_liczb)
    liczba_ = len(lista_liczb)
    
    return {
        "min": min_,
        "max": max_,
        "suma": suma_,
        "srednia": srednia_,
        "liczba": liczba_
    }
#sprawdzenie
print(statystyki([2, 4, 6, 7, 10]))  


# ------- Zad 6 ----------------------------------------------------
lista = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7,8, 9]
lista_pierwsze =                [x for x in lista if isPrime(x)]
lista_kwadraty =                [x**2 for x in lista]
lista_kwadraty_dodatnich =      [x**2 for x in lista_kwadraty if x > 0]
lista_powyzej_sredniej =        [x for x in lista if x > mean(lista)]

#sprawdzenie
print("Lista liczb pierwszych:", lista_pierwsze)
print("Lista kwadratów:", lista_kwadraty)   
print("Lista kwadratów dodatnich:", lista_kwadraty_dodatnich)
print("Lista liczb powyżej średniej:", lista_powyzej_sredniej)


# ------- Zad 7 ----------------------------------------------------

def analizuj_tekst(tekst):
    tekst = tekst.lower()

    for znak in string.punctuation:
        tekst = tekst.replace(znak, '')
        
    slowa = tekst.split()
    
    wystapienia = {}
    for slowo in slowa:
        if slowo in wystapienia:
            wystapienia[slowo] += 1
        else:
            wystapienia[slowo] = 1
            
    return wystapienia

#sprawdzenie
testowy_tekst = "Python jest prosty, Python jest czytelny."
print(analizuj_tekst(testowy_tekst))


# ------- Zad 8 ----------------------------------------------------

tablica = np.random.randint(0, 101, size=20)

print("1. Oryginalna tablica:")
print(tablica)

x_min = tablica.min()
x_max = tablica.max()
print("\n2. Wartość minimalna:", x_min)
print("   Wartość maksymalna:", x_max)

srednia = tablica.mean()
odchylenie = tablica.std()
print(f"\n3. Średnia: {srednia:.2f}")
print(f"   Odchylenie standardowe: {odchylenie:.2f}")

wieksze_od_sredniej = tablica[tablica > srednia]
print("\n4. Elementy większe od średniej:")
print(wieksze_od_sredniej)

posortowana = np.sort(tablica)
print("\n5. Posortowana tablica:")
print(posortowana)

tablica_znormalizowana = (tablica - x_min) / (x_max - x_min)
print("\n6. Tablica znormalizowana (zaokrąglona do 2 miejsc po przecinku):")
print(np.round(tablica_znormalizowana, 2))


# ------- Zad 9 ----------------------------------------------------


# ------- Zad 10 ---------------------------------------------------


# ------- Zad 11 ---------------------------------------------------
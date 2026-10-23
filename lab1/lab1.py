import numpy as np
#import cupy as np
import sympy as sp
from statistics import mean
import string
import random
import re


# ======= Zad 1 ======================================
# input in Celsius
def convert_temp(x):
    if isinstance(x, (int, float)): #sprwdza czy x jest int lub float lub nie
        f = 1.8 * x + 32 #zamiana z C na F
        print(f"Temperatura {x} deg C to {f} F")
    else:
        print("Błąd: podana wartość nie jest liczbą")
# ------- sprawdzenie ----------
convert_temp(0)
convert_temp(25)


# ======= Zad 2 ======================================
def usun_duplikaty(sekwencja):
    unikalne = sorted(set(sekwencja))
    for liczba in unikalne:
        ile = sekwencja.count(liczba)
        print(f"{liczba} występuje {ile} razy")
# ------- sprawdzenie ----------
usun_duplikaty([1, 2, 3, 2, 4, 1, 5])


# ======= Zad 3 ======================================
znajdz_pierwszy = lambda sekwencja, pierwszy: print("Are they equal?: ", sekwencja[0] == pierwszy)
# ------- sprawdzenie ----------
znajdz_pierwszy([2,1], 1)


# ======= Zad 4 ======================================
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

# ------- sprawdzenie ----------
liczby_pierwsze(20)


# ======= Zad 5 ======================================
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
# ------- sprawdzenie ----------
print(statystyki([2, 4, 6, 7, 10]))


# ======= Zad 6 ======================================
lista = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7,8, 9]
lista_pierwsze =                [x for x in lista if isPrime(x)]
lista_kwadraty =                [x**2 for x in lista]
lista_kwadraty_dodatnich =      [x**2 for x in lista_kwadraty if x > 0]
lista_powyzej_sredniej =        [x for x in lista if x > mean(lista)]

#druga opcja z chata
lista = np.arange(-10, 10)
lista_pierwsze =                [x for x in lista if sp.isprime(x)]
lista_kwadraty =                lista ** 2
lista_kwadraty_dodatnich =      lista[lista > 0] ** 2
lista_powyzej_sredniej =        lista[lista > lista.mean()]


# ------- sprawdzenie ----------
print("Lista liczb pierwszych:", lista_pierwsze)
print("Lista kwadratów:", lista_kwadraty)
print("Lista kwadratów dodatnich:", lista_kwadraty_dodatnich)
print("Lista liczb powyżej średniej:", lista_powyzej_sredniej)


# ======= Zad 7 ======================================
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

# ------- sprawdzenie ----------
testowy_tekst = "Python jest prosty, Python jest czytelny."
print(analizuj_tekst(testowy_tekst))


# ======= Zad 8 ======================================
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
print()
print()
print()

# ======= Zad 9 ======================================
def losowa_macierz(rows, cols, max_val):
    matrix = []
    for i in range(rows):
        row = np.random.randint(0, max_val + 1, size=cols)
        matrix.append(row)
    print(matrix)
    print(np.array(matrix))
    return np.array(matrix)

# druga opcja - z chata
def losowa_macierz2(rows, cols, max_val):
    matrix = np.random.randint(0, max_val + 1, size=(rows, cols))
    print(matrix)
    return matrix

# ------- sprawdzenie ----------
A = losowa_macierz(3, 4, 10)
B = losowa_macierz(4, 2, 6)
print("macierz A:\n", A)
print("macierz B:\n", B)

print("Rozmiary macierzy A, m x n:\n", np.shape(A))
print("Rozmiary macierzy B, m x n:\n", np.shape(B))
print("Wymnożona macierz:", np.matmul(A, B), "\n Rozmiar wymnożonej macierzy, m x n:", np.shape(np.matmul(A, B)))
print("transponowana macierz A':\n", np.transpose(A))

A_sum = []
for i in range(np.shape(A)[0]):
    suma_wiersza = 0
    for j in range(np.shape(A)[1]):
        suma_wiersza += A[i][j]
    A_sum.append(suma_wiersza)
print("Wektor sum wierszy macierzy A:\n", A_sum)

# druga opcja - z chata
A_sum = np.sum(A, axis=1)
print("Wektor sum wierszy macierzy A wersja 2:\n", A_sum)

A_mean = np.mean(A, axis=0)
print("Wektor srednich kolumn macierzy A:\n", A_mean)


# ======= Zad 10 =====================================
class Calculator:
    def __init__(self, x=0, y=0):
       self.x = x
       self.y = y

    def set(self, x, y):
        self.x = x
        self.y = y
    def get(self):
        return [self.x, self.y]

    def add(self):
        return self.x + self.y
    def multiply(self):
        return self.x*self.y
    def divide(self):
        if self.y != 0:
            return self.x / self.y
        else:
            print("Błąd! dzielenie przez zero.")
            return None

# ------- sprawdzenie ----------
liczbunie = Calculator()
print("Wartosc x = ", liczbunie.x, "Wartość y = ", liczbunie.y)
podzielenie = liczbunie.divide()

liczbunie.set(2, 10)
print("Nowe wartości: ", liczbunie.get())
print("suma = ", liczbunie.add())
print("mnozenie = ", liczbunie.multiply())
print("dzielenie = ", liczbunie.divide())


# ======= Zad 11 =====================================
class Morse_translator:
    def __init__(self, sequence = ''):
        self.sequence = sequence
        self.MORSE_CODE_DICT = { 'a':'.-', 'b':'-...',
                            'c':'-.-.', 'd':'-..', 'e':'.',
                            'f':'..-.', 'g':'--.', 'h':'....',
                            'i':'..', 'j':'.---', 'k':'-.-',
                            'l':'.-..', 'm':'--', 'n':'-.',
                            'o':'---', 'p':'.--.', 'q':'--.-',
                            'r':'.-.', 's':'...', 't':'-',
                            'u':'..-', 'v':'...-', 'w':'.--',
                            'x':'-..-', 'y':'-.--', 'z':'--..',
                            '1':'.----', '2':'..---', '3':'...--',
                            '4':'....-', '5':'.....', '6':'-....',
                            '7':'--...', '8':'---..', '9':'----.',
                            '0':'-----', ', ':'--..--', '.':'.-.-.-',
                            '?':'..--..', '/':'-..-.', '-':'-....-',
                            '(':'-.--.', ')':'-.--.-'}
    def __str__(self):
        return self.sequence

    def set(self, sequence):
        self.sequence = sequence
    def get(self):
        return self.sequence

    def only_small_letters(self):
        self.sequence = re.sub(r'\d+', '', self.sequence)
        self.sequence = self.sequence.lower()

    def translate(self):
        self.only_small_letters()
        cipher = ''
        for letter in self.sequence:
            if letter != ' ':
                cipher += self.MORSE_CODE_DICT[letter] + ' '
            else:
                cipher += ' '
        print(cipher)
        return cipher

# ------- sprawdzenie ----------
zdanie = Morse_translator('SkibiDIDI 123hihI fajnie69 tLumaczy6767 na morsa')
print("\n\nTo jest zdane zdanie:\n", zdanie, "\n")

zdanie.translate()

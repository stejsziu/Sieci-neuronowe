import numpy as np
import sys
import matplotlib.pyplot as plt

'''
structure = [
    {f'type': 'input', 'units': 1},
{'type': 'dense', 'units': 8, 'activation_function': 'tanh'},
{'type': 'dense', 'units': 2, 'activation_function': 'linear'}
]

def create_network(structure):
    network = [structure[0].copy()]
    network[0]['output'] = None

    for i in range(1, len(structure)):
        layer = {
            'type': structure[i]['type'], # pomijana bo jeden typ warstw
            'units': structure[i]['units'], # pomijana bo pozniej wyznaczone wagi
            'weights': np.random.randn(structure[i]['units'], structure[i-1['units']]),
            'activation_function': structure[i]['activation_function'],
            'activation_potential': None,
            'output': None,
            'delta': None
        }
    return network

structure = [
{'type': 'input', 'units': 1},
{'type': 'dense', 'units': 8,'activation_function': 'tanh'},
{'type': 'dense', 'units': 8,'activation_function': 'relu'},
{'type': 'dense', 'units': 1,'activation_function': 'linear'}
]
network = create_network ( structure )
'''

# ======================== ZAD 1 ========================
class Activation_fcn:
    def __init__(self):
        self.functions = {
            'linear': self.linear,
            'sigmoid': self.logistic,
            'logistic': self.logistic,
            'tanh': self.tanh,
            'relu': self.relu
        }

    def output(self, layer, name, derivative=False):
        if name in self.functions:
            return self.functions[name](layer['activation_potential'], layer['output'], derivative)
        else:
            sys.exit(f"Error: Activation function '{name}' not found.")

    # Identity (Tożsamościowa / Liniowa)
    def linear(self, activation_potential, output, derivative=False):
        if not derivative:
            return activation_potential
        else:
            return np.ones_like(activation_potential)

    # Logistic (Sigmoid / Logistyczna)
    def logistic(self, activation_potential, output, derivative=False):
        if not derivative:
            return 1.0 / (1.0 + np.exp(-activation_potential))
        else:
            s = 1.0 / (1.0 + np.exp(-activation_potential))
            return s * (1.0 - s)

    # Hyperbolic tangent (Tangens hiperboliczny)
    def tanh(self, activation_potential, output, derivative=False):
        if not derivative:
            return np.tanh(activation_potential)
        else:
            t = np.tanh(activation_potential)
            return 1.0 - np.square(t)

    # ReLU (Rectified Linear Unit)
    def relu(self, activation_potential, output, derivative=False):
        if not derivative:
            return np.maximum(0, activation_potential)
        else:
            return np.where(activation_potential > 0, 1.0, 0.0)

# --- sprawdzenie ---

afcn = Activation_fcn()
# Przykładowa warstwa z wyznaczonym potencjałem aktywacji
layer = {
    'activation_potential': np.array([-2.0, 0.0, 1.5, 3.0]),
    'output': None
}
for name in ['linear', 'logistic', 'tanh', 'relu']:
    out = afcn.output(layer, name, derivative=False)
    print(f"Funkcja {name:8s} -> wyjście: {out}")


# ======================== ZAD 2 ========================
'''
class Neural_network(object):
    def __init__(self, structure=None, init_weight='rand'):
        self.af = Activation_fcn() # Zakładamy, że klasa z Zadania 1 została wczytana wcześniej
        if structure:
            # UWAGA: Zmieniono przekazywany parametr z uciętego na sztywno 'rand'
            # na wartość parametru init_weight, aby sieć mogła tworzyć się z odpowiednimi wagami
            self.create_network(structure, init_weight)

    def create_network(self, structure, init_weight='rand'):
        # Kopiujemy pierwszą warstwę i zapewniamy jej pole output
        self.nnetwork = [structure[0].copy()]
        self.nnetwork[0]['output'] = None

        for i in range(1, len(structure)):
            # Określenie wymiarów macierzy wag
            rows = structure[i]['units']
            cols = structure[i-1]['units']

            # Nowa funkcjonalność: wybór metody inicjalizacji wag
            if init_weight == 'zero':
                weights = np.zeros((rows, cols))
            elif init_weight == 'one':
                weights = np.ones((rows, cols))
            elif init_weight == 'rand':
                weights = np.random.randn(rows, cols)
            else:
                raise ValueError("Nieznana metoda inicjalizacji. Wybierz: 'zero', 'one', 'rand'.")

            # Tworzenie nowej warstwy w słowniku
            new_layer = {
                'weights': weights,
                'activation_function': structure[i]['activation_function'],
                'activation_potential': None,
                'delta': None,
                'output': None
            }
            self.nnetwork.append(new_layer)

        return self.nnetwork

# --- sprawdzenie ---
# Przykładowa struktura z instrukcji
structure = [
    {'type': 'input', 'units': 1},
    {'type': 'dense', 'units': 8, 'activation_function': 'tanh'},
    {'type': 'dense', 'units': 8, 'activation_function': 'tanh'},
    {'type': 'dense', 'units': 1, 'activation_function': 'linear'}
]

# Sprawdzenie inicjalizacji typu 'zero'
model_zero = Neural_network(structure, init_weight='zero')
print("Wagi pierwszej warstwy ukrytej (zero):\n", model_zero.nnetwork[1]['weights'])

# Sprawdzenie inicjalizacji typu 'one'
model_one = Neural_network(structure, init_weight='one')
print("\nWagi ostatniej warstwy (one):\n", model_one.nnetwork[3]['weights'])
'''

# ======================== ZAD 3 ========================
class Neural_network(object):
    def __init__(self, structure=None, init_weight='rand'):
        self.af = Activation_fcn()  # Obiekt zawierający funkcje aktywacji z Zadania 1
        if structure:
            self.create_network(structure, init_weight)

    def create_network(self, structure, init_weight='rand'):
        self.nnetwork = [structure[0].copy()]
        self.nnetwork[0]['output'] = None

        for i in range(1, len(structure)):
            rows = structure[i]['units']
            cols = structure[i-1]['units']

            if init_weight == 'zero':
                weights = np.zeros((rows, cols))
            elif init_weight == 'one':
                weights = np.ones((rows, cols))
            elif init_weight == 'rand':
                weights = np.random.randn(rows, cols)
            else:
                raise ValueError("Nieznana metoda inicjalizacji.")

            new_layer = {
                'weights': weights,
                'activation_function': structure[i]['activation_function'],
                'activation_potential': None,
                'delta': None,
                'output': None
            }
            self.nnetwork.append(new_layer)

        return self.nnetwork
    # nowe funkcje z zad 3
    # Forward propagate input to a network output
    def forward_propagate(self, nnetwork, inputs):
        # Pobieramy próbkę początkową jako początkowy sygnał "wejściowy"
        inp = np.array(inputs, copy=True)

        # Zapiszmy sygnał wejściowy w zerowej warstwie dla spójności
        nnetwork[0]['output'] = inp

        for i in range(1, len(nnetwork)):
            layer = nnetwork[i]

            # 1. Wyznaczenie potencjału aktywacji: V = W * X
            # (mnożenie macierzy wag przez sygnał wejściowy / wyjście z poprzedniej warstwy)
            layer['activation_potential'] = np.matmul(layer['weights'], inp)

            # 2. Wyznaczenie wyjścia: Y = f(V)
            # Korzystamy z metody output z klasy Activation_fcn
            layer['output'] = self.af.output(layer, layer['activation_function'], derivative=False)

            # 3. Wyjście obecnej warstwy staje się wejściem do warstwy następnej
            inp = layer['output']

        # Zwracamy wynik z ostatniej warstwy (spłaszczony do wektora 1D)
        return inp.flatten()

    def predict(self, nnetwork, inputs):
        out = []
        # Dla każdej próbki z danych wejściowych wykonujemy propagację w przód
        for input_sample in inputs:
            # Używamy zaimplementowanej wyżej metody
            prediction = self.forward_propagate(nnetwork, input_sample)
            out.append(prediction)

        return out
# --- sprawdzenie ---


# ======================== ZAD 4 ========================
import numpy as np

# Utworzenie instancji klasy sieci (zależnie od implementacji w Zad. 2)
# Używamy domyślnego obiektu, struktura będzie nadpisywana w create_network
model = Neural_network()

print("=== PRZYPADEK 1: Inicjalizacja 'zero', funkcja 'linear' ===")
structure1 = [
    {'type': 'input', 'units': 1},
    {'type': 'dense', 'units': 2, 'activation_function': 'linear'},
    {'type': 'dense', 'units': 1, 'activation_function': 'linear'}
]
# Tworzenie sieci z wagami zerowymi
network1 = model.create_network(structure1, "zero")
n = 1
X1 = np.linspace(-5, 5, n).reshape(-1, 1)
# Predykcja
predicted1 = model.predict(network1, X1)
print("Wejście X:", X1.flatten())
print("Wyjście (predicted):", predicted1, "\n")


print("=== PRZYPADEK 2: Inicjalizacja 'one', funkcja 'tanh' ===")
structure2 = [
    {'type': 'input', 'units': 1},
    {'type': 'dense', 'units': 2, 'activation_function': 'tanh'},
    {'type': 'dense', 'units': 2, 'activation_function': 'tanh'},
    {'type': 'dense', 'units': 1, 'activation_function': 'tanh'}
]
# Tworzenie sieci z wagami o wartości 1
network2 = model.create_network(structure2, "one")
n = 1
X2 = np.linspace(-5, 5, n).reshape(-1, 1)
# Predykcja
predicted2 = model.predict(network2, X2)
print("Wejście X:", X2.flatten())
print("Wyjście (predicted):", predicted2, "\n")


print("=== PRZYPADEK 3: Inicjalizacja 'rand', funkcja 'relu' ===")
structure3 = [
    {'type': 'input', 'units': 1},
    {'type': 'dense', 'units': 4, 'activation_function': 'relu'},  # Zmieniono 'ReLu' na 'relu' by pasowało do słownika z Zad. 1
    {'type': 'dense', 'units': 4, 'activation_function': 'relu'},
    {'type': 'dense', 'units': 1, 'activation_function': 'relu'}
]
# Tworzenie sieci z wagami losowymi
network3 = model.create_network(structure3, "rand")
n = 1
X3 = np.linspace(-5, 5, n).reshape(-1, 1)
# Predykcja
predicted3 = model.predict(network3, X3)
print("Wejście X:", X3.flatten())
print("Wyjście (predicted):", predicted3, "\n")

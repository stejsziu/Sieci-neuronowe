import numpy as np
#import sys
import matplotlib.pyplot as plt


# ======================== ZAD 1 ========================
def dane_wejsciowe(inputs, weights):
    layer = {
        'activation_potential': np.array([np.matmul(weights, inputs)]),
        'output': None
    }
    print(layer)
    return layer

# ******** sprawdzenie *********
np.random.seed(42)
input_size = 10
inputs = [np.random.randn() for i in range(input_size)]
weights = [np.random.randn() for i in range(input_size)]

layer = dane_wejsciowe(inputs, weights)
print("Struktura słownika:", layer)
print("Kształt 'activation_potential':", layer['activation_potential'].shape)
print("\n")

# ======================== ZAD 2 ========================
# ------- LINEAR ----------
def linear(activation_potential, output, derivative = False):
    if not derivative:
        return activation_potential
    else:
        return np.ones_like(activation_potential)

# ------- SIGMOID ----------
def sigmoid(activation_potential, output, derivative = False):
    s =  1. / ( 1. + np.exp(-activation_potential) )
    if not derivative:
        return s
    else:
        return s * (1 - s)

# ------- TANH ----------
def tanh(activation_potential, output, derivative = False):
    s = (np.exp(activation_potential) - np.exp(-activation_potential)) / (np.exp(activation_potential) + np.exp(-activation_potential))
    if not derivative:
        return s
    else:
        return 1 - np.square(s)

# ------- ReLU ----------
def ReLU(activation_potential, output, derivative = False):
    if not derivative:
        return np.maximum(0, activation_potential)
    else:
        return np.where(activation_potential > 0, 1., 0.)

# --- sprawdzenie ---
funkcje = [('linear', linear), ('sigmoid', sigmoid), ('tanh', tanh), ('ReLU', ReLU)]
for nazwa, fcn in funkcje:
    layer = dane_wejsciowe(inputs, weights)

    # Forward pass (obliczenie wyjścia)
    layer['output'] = fcn(layer['activation_potential'], None, derivative=False)
    # Backward pass (obliczenie pochodnej)
    check_derivative = fcn(layer['activation_potential'], layer['output'], derivative=True)

    print(f"=== FUNKCJA: {nazwa} ===")
    print("Potencjał:    ", layer['activation_potential'])
    print("Wyjście:      ", layer['output'])
    print("Pochodna:     ", check_derivative)
    print("-" * 40)


# ======================== ZAD 3 ========================
def plot_activation(activation_fcn, layer, title="Funkcja Aktywacji", derivative=False):
    # Obliczenie wyjścia/pochodnej dla zadanej funkcji
    potencjał = layer['activation_potential']
    wynik = activation_fcn(potencjał, layer['output'], derivative=derivative)

    # Rysowanie wykresu
    plt.figure(figsize=(7, 4))
    plt.plot(potencjał, wynik, label=title, color='green', linewidth=2)
    plt.axhline(0, color='black', linestyle='--', linewidth=0.8) # oś X
    plt.axvline(0, color='black', linestyle='--', linewidth=0.8) # oś Y
    plt.title(title)
    plt.xlabel("Potencjał aktywacji (v)")
    plt.ylabel("Wyjście y / pochodna y'")
    plt.grid(True)
    plt.legend()
    plt.show()

# --- sprawdzenie ---
layer = {
    'activation_potential': np.arange(-4., 4., 0.1),
    'output': None
}
#plot_activation(linear, layer, title="Liniowa")
#plot_activation(sigmoid, layer, title="Sigmoid")
#plot_activation(tanh, layer, title="Tanh")
#plot_activation(ReLU, layer, title="ReLU")


# ======================== ZAD 4 ========================
import sys
import numpy as np

class Activation_fcn:
    def __init__(self):
        self.functions = { # spis funkcji
            'linear': self.linear,
            'sigmoid': self.logistic,
            'logistic': self.logistic,
            'tanh': self.tanh,
            'relu': self.relu
        }

    def output(self, layer, name, derivative=False): # wywołanie po nazwie
        if name in self.functions:
            return self.functions[name](layer['activation_potential'], layer['output'], derivative)
        else:
            sys.exit(f"Error: Activation function '{name}' not found.")

    # Identity
    def linear(self, activation_potential, output, derivative=False):
        if not derivative:
            return activation_potential
        else:
            return np.ones_like(activation_potential)

    # Logistic (sigmoid)
    def logistic(self, activation_potential, output, derivative=False):
        s = 1.0 / (1.0 + np.exp(-activation_potential))
        if not derivative:
            return s
        else:
            return s * (1.0 - s)

    # Hyperbolic tangent
    def tanh(self, activation_potential, output, derivative=False):
        t = np.tanh(activation_potential)
        if not derivative:
            return t
        else:
            return 1.0 - np.square(t)

    # ReLU
    def relu(self, activation_potential, output, derivative=False):
        if not derivative:
            return np.maximum(0, activation_potential)
        else:
            return np.where(activation_potential > 0, 1.0, 0.0)

# --- sprawdzenie ---
afcn = Activation_fcn()
nazwy_funkcji = ['linear', 'sigmoid', 'tanh', 'relu']

for name in nazwy_funkcji:
    layer['output'] = afcn.output(layer, name, derivative=False) # forward pass
    pochodna = afcn.output(layer, name, derivative=True) # backward pass

    print(f"=== FUNKCJA: {name} ===")
    print("Potencjał: ", layer['activation_potential'])
    print("Wyjście:   ", layer['output'])
    print("Pochodna:  ", pochodna)
    print("-" * 40)


# ======================== ZAD 5 ========================
class Loss_fcn:
    def __init__(self):
        self.functions = { # spis funkcji
            'mse': self.mse,
            'binary_cross_entropy': self.binary_cross_entropy
        }

    def output(self, name, expected, outputs, derivative=False): # wywołanie po nazwie
        if name in self.functions:
            return self.functions[name](expected, outputs, derivative)
        else:
            sys.exit(f"Error: Loss function '{name}' not found.")

    # Mean Square Error loss function
    def mse(self, expected, outputs, derivative=False):
        expected = np.array(expected)
        outputs = np.array(outputs)

        if not derivative:
            # l_sq = 0.5 * (expected - outputs)^2
            return 0.5 * np.power(expected - outputs, 2)
        else:
            # dl_sq / d_output = -(expected - outputs) = outputs - expected
            return -(expected - outputs)

    # Cross-entropy loss function
    def binary_cross_entropy(self, expected, outputs, derivative=False):
        expected = np.array(expected)
        outputs = np.array(outputs)

        # Zabezpieczenie przed log(0) oraz dzieleniem przez zero (np. clip do [1e-7, 1 - 1e-7])
        eps = 1e-7
        outputs = np.clip(outputs, eps, 1.0 - eps)

        if not derivative:
            # l_BCE = - [ t * ln(y) + (1 - t) * ln(1 - y) ]
            return -(expected * np.log(outputs) + (1.0 - expected) * np.log(1.0 - outputs))
        else:
            # dl_BCE / d_output = - (expected / outputs) + (1 - expected) / (1 - outputs)
            return -(expected / outputs) + ((1.0 - expected) / (1.0 - outputs))

# --- sprawdzenie ---
loss = Loss_fcn()

# Przykładowe dane testowe (dla 3 próbek):
# expected (t) - prawdziwe etykiety / wartości oczekiwane
# outputs (y)  - predykcje zwrócone przez model
expected = np.array([1.0, 0.0, 1.0])
outputs  = np.array([0.8, 0.2, 0.3])

print("Wartości oczekiwane (expected):", expected)
print("Wartości modelu (outputs):      ", outputs)
print("=" * 55)

# --- MSE
mse_val = loss.output('mse', expected, outputs, derivative=False)
mse_der = loss.output('mse', expected, outputs, derivative=True)

print("=== BŁĄD ŚREDNIOKWADRATOWY (MSE) ===")
print("Wartość straty (Loss):   ", mse_val)
print("Pochodna (Derivative):   ", mse_der)
print("-" * 55)

# --- BINARY CROSS-ENTROPY
bce_val = loss.output('binary_cross_entropy', expected, outputs, derivative=False)
bce_der = loss.output('binary_cross_entropy', expected, outputs, derivative=True)

print("=== BINARNA ENTROPIA KRZYŻOWA (BCE) ===")
print("Wartość straty (Loss):   ", bce_val)
print("Pochodna (Derivative):   ", bce_der)
print("=" * 55)


# ======================== ZAD 6 ========================
def plot_loss_function(loss_obj, loss_name, expected_val, outputs_range, title="Przebieg funkcji straty"):
    """
    Rysuje wykres wartości funkcji straty oraz jej pochodnej w zależności od różnicy (wyjście - oczekiwana).

    Parameters:
    - loss_obj: instancja klasy Loss_fcn
    - loss_name: nazwa funkcji straty ('mse' lub 'binary_cross_entropy')
    - expected_val: zadana wartość oczekiwana (t)
    - outputs_range: tablica NumPy zawierająca zakreślane wartości wyjściowe modelu (y)
    """
    # 1. Obliczenie różnicy (błędu): e = y - t (lub t - y)
    difference = outputs_range - expected_val

    # 2. Obliczenie wartości funkcji straty oraz jej pochodnej
    loss_values = [loss_obj.output(loss_name, expected_val, y, derivative=False) for y in outputs_range]
    derivatives  = [loss_obj.output(loss_name, expected_val, y, derivative=True) for y in outputs_range]

    # Rysowanie wykresu
    plt.figure(figsize=(8, 5))
    plt.plot(difference, loss_values, label=f'Strata (Loss) - {loss_name}', color='red', linewidth=2)
    plt.plot(difference, derivatives, label=f'Pochodna (Derivative)', color='blue', linestyle='--', linewidth=1.5)

    plt.axhline(0, color='black', linestyle=':', linewidth=0.8)
    plt.axvline(0, color='black', linestyle=':', linewidth=0.8)

    plt.title(f"{title} (dla wartości oczekiwanej t = {expected_val})")
    plt.xlabel("Różnica pomiędzy wartością zadaną i wyznaczoną (y - t)")
    plt.ylabel("Wartość funkcji straty / pochodnej")
    plt.grid(True)
    plt.legend()
    plt.show()

# --- sprawdzenie ---
loss = Loss_fcn()

# --- MSE
# Dla MSE wartość oczekiwana może wynosić np. 0, a wyjścia z modelu zmieniają się od -3 do 3
outputs_mse = np.linspace(-3.0, 3.0, 300)
plot_loss_function(
    loss_obj=loss,
    loss_name='mse',
    expected_val=0.0,
    outputs_range=outputs_mse,
    title="Wizualizacja błędu MSE"
)

# --- BCE
# Dla BCE zakładamy t = 1.0 (etykieta pozytywna), a wyjście modelu y leży w (0, 1)
outputs_bce = np.linspace(0.001, 0.999, 300)
plot_loss_function(
    loss_obj=loss,
    loss_name='binary_cross_entropy',
    expected_val=1.0,
    outputs_range=outputs_bce,
    title="Wizualizacja błędu Binary Cross-Entropy"
)

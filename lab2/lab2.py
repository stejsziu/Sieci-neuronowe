import numpy as np
import sys
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


'''
# ======================== ZAD 3 ========================
def plotPotentialActivation(activtion_potential, output, derivative = False):
    layer = {
        'ativation_potential': activation_potential,
        'output': None}
    linear(layer)
    return 0
    plt.figue
    plt.plot(layer['activation_potential'], linear(layer['activation_potential'], derivative = False))
    plt.show()


# ======================== ZAD 4 ========================
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

    # Identity
    def linear(self, activation_potential, output, derivative = False):
        pass # TODO

    # Logistic (sigmoid)
    def logistic(self, activation_potential, output, derivative = False):
        pass # TODO

    # Hyperbolic tangent
    def tanh(self, activation_potential, output, derivative = False):
        pass # TODO

    # ReLU
    def relu(self, activation_potential, output, derivative = False):
        pass # TODO

# po uzupelnieniu
afcn = Activation_fcn()
afcn.output(layer, 'linear')


# ======================== ZAD 5 ========================
def mse(self, np.expcted, output, derivative=False):
    if not derivative:
        return 0.5 * np.power(np.expected - outputs, 2)
    else:
        return -(np.expected - outputs)

class Loss_fcn:
    def __init__(self):
        self.funtions = {
            'mse': self.mse,
            'binary_cross_entropy': self.binary_cross_entropy
        }

    # Loss/error value calculated for all input data samples
    def output(self, name, np.expected, outputs, derivative)
        if name in self.functions:
            return self.functions[name](np.expected, outputs, derivative)
        else:
            sys.exit(f"Error: Loss function '{name}' not found.")

    # Mean Square Error Loss funciton
    def mse(self, name, np.expected, outputs, derivtive):
        #if name in self.functions:
        #    return self.functions[name](np.expected, outputs, derivative):
        #else:
        #   sys.exit(f"Error: Loss function '{name}' not found.")

    # Cross-entropy loss funciton
    def binary_cross_entropy(self, name, np.expected, outputs, derivtive):


# ======================== ZAD 6 ========================
'''

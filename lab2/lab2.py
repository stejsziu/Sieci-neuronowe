import numpy as np
import sys
import matplotlib.pyplot as plt


# ======================== ZAD 1 ========================
np.random.seed(42)
input_size = 10

inputs = [np.random.randn() for i in range(input_size)]
weight = [np.random.randn() for i in range(input_size)]

layer = {
    'activation_potential': np.matmul(weights, inputs),
    'output': None
}

print(layer)


# ======================== ZAD 2 ========================
# ---- LINEAR ----
def linear_log(activation_potential, output, derivative = False):
    if not derivative:
        return activation_potential
    else:
        return np.ones_like(activation_potential)

activation_potential = layer['activation_potential']
layer['output'] = linear_log(activation_potential, 0)
linear_log(layer)

# ---- SIGMOID ----
def sigmoid_log(activation_potential, output, derivative = False):
    if not derivative:
        return 1 / (1 + exp(-activation_potential) )
    else:
        return (1 - exp(-activation_potential)) / (1 + exp(-activation_potential))**2

activation_potential = layer['activation_potential']
layer['output'] = sigmoid_log(activation_potential, 0)
sigmoid_log(layer)

# ---- TANH ----
def tanh_log(activation_potential, output, derivative = False):
    if not derivative:
        return (exp(activation_potential) - exp(activation_potential)) / (exp(activation_potential)- exp(activation_potential))
    else:
        return 1 - ( (exp(activation_potential) - exp(activation_potential)) / (exp(activation_potential)- exp(activation_potential)) )**2

activation_potential = layer['activation_potential']
layer['output'] = tanh_log(activation_potential, 0)
tanh_log(layer)

# ---- ReLU ----
#ReLU
def ReLU(activation_potential, output, derivative = False):
    if not derivative:
        return max(0, activation_potential)
    else:
        if activation_potential > 0: return 1;
        else: return 0;

activation_potential = layer['activation_potential']
layer['output'] = ReLU_log(activation_potential, 0)
ReLU(layer)


# ======================== ZAD 3 ========================
def plotPotentialActivation(activtion_potential, output, derivative = False):
    layer = {
        'ativation_potential': activation_potential,
        'output': None}
    linear_log(layer)
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
def mse(self, expcted, output, derivative=False):
    if not derivative:
        return 0.5 * np.power(expected - outputs, 2)
    else:
        return -(expected - outputs)

class Loss_fcn:
    def __init__(self):
        self.funtions = {
            'mse': self.mse,
            'binary_cross_entropy': self.binary_cross_entropy
        }

    # Loss/error value calculated for all input data samples
    def output(self, name, expected, outputs, derivative)
        if name in self.functions:
            return self.functions[name](expected, outputs, derivative)
        else:
            sys.exit(f"Error: Loss function '{name}' not found.")

    # Mean Square Error Loss funciton
    def mse(self, name, expected, outputs, derivtive):
        #if name in self.functions:
        #    return self.functions[name](expected, outputs, derivative):
        #else:
        #   sys.exit(f"Error: Loss function '{name}' not found.")

    # Cross-entropy loss funciton
    def binary_cross_entropy(self, name, expected, outputs, derivtive):


# ======================== ZAD 6 ========================


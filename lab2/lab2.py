#import cupy as np
import numpy as np
import sys

# ------- Zad 1 ----------------------------------------------------
np.random.seed (42)
input_size = 10 # lub inna zadana liczba
inputs = [np.random.randn() for i in range (input_size)]
weights = [np.random.randn() for i in range (input_size)]

def v(input, weight, shift, input_size):
    for i in range (0, input_size):
        effective_input += weight * input
    effective_input += shift
    return effective_input    

layer = {
    'activation_potential': np.matmul(weights, inputs),
    'output': None
}
print (layer)


# ------- Zad 2 ----------------------------------------------------
# ------- linear --------- funkcja tożsamości
def linear(activation_potential, output, derivative=False):
    if not derivative:
        return activation_potential
    else :
        return np.ones_like(activation_potential)

activation_potential = layer['activation_potential']

layer['output'] = linear(activation_potential, 0)
print(layer)

# ------- sigmoid -------- funkcja logistyczna
def sigmoid(activation_potential, output, derivative=False):
    if not derivative:
        return 1 / (1 + exp(-activation_potential))
    else :
        return activation_potential / (1 + exp(-activation_potential))

activation_potential = layer['activation_potential']

layer['output'] = linear(activation_potential, 0)
print(layer)
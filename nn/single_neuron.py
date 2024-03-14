import numpy as np
import sys

def single_neuron(inputs:list, weights:list, bias=float)->float:
    output = np.dot(inputs,weights)+bias
    return output

if __name__ == "__main__":
    inputs_raw = sys.argv[1].split()
    
    inputs = list(map(lambda x:float(x), inputs_raw))
    weights_raw = sys.argv[2].split()
    weights = list(map(lambda x:float(x), weights_raw))
    bias = float(sys.argv[3])
    print("inputs: ", inputs)
    print("weights: ", weights)
    print("bias: ", bias)
    print("output: ", single_neuron(inputs,weights,bias)) 
import numpy as np
from scipy.integrate import odeint
from random import random

rho = 28.0
sigma = 10.0
beta = 8.0 / 3.0

def f(state, t):
    x, y, z = state  # Unpack the state vector
    return sigma * (y - x), x * (rho - z) - y, x * y - beta * z  # Derivatives

def export_states():
    state0 = [1.0*random()*2-1, 1.0*random()*2-1, 1.0*random()*2-1]
    t = np.arange(0.0, 1000.0, 0.01)

    states = odeint(f, state0, t)
    return states
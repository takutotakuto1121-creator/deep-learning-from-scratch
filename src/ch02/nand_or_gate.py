import numpy as np

def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return (0)
    else:
        return (1)

def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.4
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return (0)
    else:
        return (1)

def nand_gate():
    print("= nand_gate =")
    print(f"0, 0 -> {NAND(0, 0)}")
    print(f"0, 1 -> {NAND(0, 1)}")
    print(f"1, 0 -> {NAND(1, 0)}")
    print(f"1, 1 -> {NAND(1, 1)}")
    print()

def or_gate():
    print("= or_gate =")
    print(f"0, 0 -> {OR(0, 0)}")
    print(f"0, 1 -> {OR(0, 1)}")
    print(f"1, 0 -> {OR(1, 0)}")
    print(f"1, 1 -> {OR(1, 1)}")
    print()

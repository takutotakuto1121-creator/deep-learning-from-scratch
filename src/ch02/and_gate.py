import numpy as np

def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return (0)
    else:
        return (1)

def and_gate():
    print("= and_gate.py =")
    print(f"0, 0 -> {AND(0, 0)}")
    print(f"0, 1 -> {AND(0, 1)}")
    print(f"1, 0 -> {AND(1, 0)}")
    print(f"1, 1 -> {AND(1, 1)}")
    print()

if __name__ == "__main__":
    and_gate()
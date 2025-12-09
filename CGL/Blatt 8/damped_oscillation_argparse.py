import numpy as np
import matplotlib.pyplot as plt
import argparse

# Funktion zur Berechnung der gedämpften harmonischen Schwingung
def damped_oscillation(t, A, gamma, omega):
    """
    Berechnet die Auslenkung einer gedämpften harmonischen Schwingung zur Zeit t.
    
    x(t) = A * e^(-gamma * t) * cos(omega * t)
    """
    return A * np.exp(-gamma * t) * np.cos(omega * t)

def main():
    parser = argparse.ArgumentParser(description="Gedämpfte harmonische Schwingung")
    
    parser.add_argument(
        "-A", "--amplitude", type=float,
        default=1.0,
        help="Anfangsamplitude A (Standard: 1.0)")

    parser.add_argument(
        "-gamma", "--damping", type=float,
        default=0.2,
        help="Dämpfungskonstante gamma (Standard: 0.2)")
    
    parser.add_argument(
        "-omega", "--frequency", type=float,
        default=2 * np.pi,
        help="Kreisfrequenz omega (Standard: 2 pi)")

    args = parser.parse_args()

    t = np.linspace(0, 10, 500)
    x = damped_oscillation(t, args.amplitude, args.damping, args.frequency)

    plt.figure(figsize=(8,4))
    plt.plot(t, x, label="x(t)")
    plt.title("Gedämpfte harmonische Schwingung")
    plt.xlabel("Zeit t [s]")
    plt.ylabel("Auslenkung x(t)")
    plt.legend()
    plt.savefig("damped_oscillator.pdf")
    plt.show()
if __name__ == "__main__":
    main()
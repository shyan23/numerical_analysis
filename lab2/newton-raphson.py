import math
import matplotlib.pyplot as plt
import sympy as sp
import numpy as np


g = 9.81
c = 15
t_val = 10  
y_target = 36


m = sp.Symbol('m')

def f(m_val):
    return (g*m_val/c)*(1 - math.exp(-(c/m_val)*t_val)) - y_target

def f_symbolic():
    return (g*m/c)*(1 - sp.exp(-(c/m)*t_val)) - y_target

def derivative(m_val):
    f_sym = f_symbolic()
    f_prime_sym = sp.diff(f_sym, m)
    derivative_val = f_prime_sym.subs(m, m_val)
    return float(derivative_val)

def newton_raphson(m0, es=0.001):
    errors = []
    ea = 4 # 4% percent shurute
    iteration = 1

    print("{:<5}{:<15}{:<20}{:<20}{:<10}".format("Iter", "m", "f(m)", "f'(m)", "ea (%)"))
    print("-" * 70)

    m_current = m0

    while ea > es:
        f_val = f(m_current)
        derivative_val = derivative(m_current)
        if(derivative_val ==0): return "problem has"

        # Newton-Raphson formula
        m_new = m_current - f_val / derivative_val


        if iteration > 1:
            ea = abs((m_new - m_current) / m_new) * 100
        else:
            ea = float("inf")

        errors.append(ea if ea != float("inf") else 1000)

        # Print current iteration
        ea_str = "-" if ea == float("inf") else f"{ea:.6f}"
        print("{:<5}{:<15.10f}{:<20.10f}{:<20.10f}{:<10}".format(
            iteration, m_current, f_val, derivative_val, ea_str
        ))

        m_current = m_new
        iteration += 1

    print(f"\nConverged after {iteration-1} iterations")


    filtered_errors = [ea for ea in errors if ea != 1000]

    if filtered_errors:  
        plt.figure(figsize=(10, 6))
        plt.plot(range(2, len(filtered_errors) + 2),
                filtered_errors, marker='o', linewidth=2, markersize=8, color="tab:blue")

        plt.xlabel("Iteration")
        plt.ylabel("Approx. Relative Error (%)")
        plt.title("Newton-Raphson Method Convergence")
        plt.grid(True, alpha=0.3)

        # Linear scale with better Y-limits and spacing
        ymin = 0  # Start from 0 for cleaner look
        ymax = max(filtered_errors) * 1.1  # Add 10% padding
        plt.ylim(ymin, ymax)

        plt.ticklabel_format(style='plain', axis='y')
        

        for i, (x, y) in enumerate(zip(range(2, len(filtered_errors) + 2), filtered_errors)):
            plt.annotate(f'{y:.6f}%', 
                        xy=(x, y), 
                        xytext=(0, 10),  # 10 points above the point
                        textcoords='offset points',
                        ha='center', 
                        fontsize=9,
                        bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.8))


        plt.xlim(1.5, len(filtered_errors) + 2.5)
        
        plt.xticks(range(2, len(filtered_errors) + 2))

        plt.tight_layout()
        plt.savefig("newton_raphson.png", dpi=600, bbox_inches='tight')
        plt.show()
        plt.close()


    return m_current


if __name__ == "__main__":
    root = newton_raphson(40, es=0.001)
    print(f"\nFinal root: m = {root:.10f} kg")
    print(f"f(m) at root: {f(root):.10e}")

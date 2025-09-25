import math
import matplotlib.pyplot as plt

g = 9.81
c = 15
t = 10
y_target = 36

def f(m):
    return (g*m/c)*(1 - math.exp(-(c/m)*t)) - y_target

def secant(xl, xu, es=0.001):  
    errors = []
    ea = float("inf")
    iteration = 1

    print("{:<5}{:<15}{:<15}{:<20}{:<10}".format("Iter", "m_prev", "m_curr", "f(m_curr)", "ea (%)"))
    print("-" * 70)

    ans = xu

    while ea > es:
        f_val = f(xu)
        f_val_bef = f(xl)
        diff_posn = xu - xl
        diff_func_val = f_val - f_val_bef
        right_side = diff_posn / diff_func_val
        right_side = f_val * right_side
        ans_new = xu - right_side  

        if iteration > 1:
            ea = abs((ans_new - ans) / ans_new) * 100
        else:
            ea = float("inf")

        
        if ea != float("inf"):
            errors.append(ea)

        
        ea_str = "-" if ea == float("inf") else f"{ea:.6f}"

        print("{:<5}{:<15.10f}{:<15.10f}{:<20.10f}{:<10}".format(
            iteration, xl, xu, f_val, ea_str
        ))

        xl, xu = xu, ans_new
        ans = ans_new
        iteration += 1

    print(f"\nConverged after {iteration-1} iterations")
    print(f"Root = {ans:.10f}, f(root) = {f(xu):.6e}")

    

    if errors:  
        iterations = range(2, len(errors) + 2)  
        plt.figure(figsize=(10, 6))
        plt.plot(iterations, errors, marker='o', linewidth=2, markersize=8, color='tab:red')
        plt.xlabel("Iteration")
        plt.ylabel("Approximate Relative Error (%)")
        plt.title("Secant Method Convergence")
        plt.grid(True, alpha=0.3)
        
        
        ymin = 0  
        ymax = max(errors) * 1.1  
        plt.ylim(ymin, ymax)
        
        
        plt.ticklabel_format(style='plain', axis='y')
        
        
        plt.xticks(list(iterations))
        
        
        plt.xlim(1.5, max(iterations) + 0.5)
        
        
        for i, (x, y) in enumerate(zip(iterations, errors)):
            plt.annotate(f'{y:.6f}%', 
                        xy=(x, y), 
                        xytext=(0, 10),  
                        textcoords='offset points',
                        ha='center', 
                        fontsize=9,
                        bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.8))
        
        plt.tight_layout()
        plt.savefig("secant.png", dpi=300, bbox_inches='tight')
        plt.show()
        plt.close()

    return xu


if __name__ == "__main__":
    root = secant(30, 40, es=0.001)
    print(f"\nFinal root: m = {root:.10f} kg")

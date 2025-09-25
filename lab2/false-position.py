import math
import matplotlib.pyplot as plt

g = 9.81
c = 15
t = 10
y_target = 36

# Function
def function(m):
    return (g*m/c)*(1 - math.exp(-(c/m)*t)) - y_target

def false_position(xl, xu, es=0.001, max_iter=100):
    if function(xl)*function(xu) > 0:
        raise ValueError("Hobe na")

    errors = []
    xr_old = xl
    print(f"{'Iter':<5}{'xl':<15}{'xu':<15}{'xr':<15}{'f(xr)':<20}{'ea (%)':<10}")
    for i in range(1, max_iter+1):
        xr = (xl*function(xu) - xu*function(xl)) / (function(xu) - function(xl))

        ea = abs((xr - xr_old)/xr)*100 if i > 1 else None # first er error baad disi
        if ea is not None:
            errors.append(ea)

        print(f"{i:<5}{xl:<15.10f}{xu:<15.10f}{xr:<15.10f}{function(xr):<20.10f}{ea if ea else '-':<10}")

        if function(xl)*function(xr) < 0:
            xu = xr
        else:
            xl = xr

        if ea is not None and ea < es: # breaking condtion
            break
        xr_old = xr

    if errors:  
        iterations = range(2, len(errors) + 2)
        plt.figure(figsize=(10, 6))
        plt.plot(iterations, errors, marker='o', linewidth=2, markersize=8, color='tab:green')
        plt.xlabel("Iteration")
        plt.ylabel("Approx. Relative Error (%)")
        plt.title("False Position Method Convergence")
        plt.grid(True, alpha=0.3)

        # Better Y-axis limits with padding
        ymin = min(errors) * 0.8
        ymax = max(errors) * 1.2
        plt.ylim(ymin, ymax)
        
        # Let matplotlib handle Y-ticks for better spacing
        plt.ticklabel_format(style='plain', axis='y')
        
        # Ensure integer ticks on x-axis
        plt.xticks(list(iterations))
        
        # Set appropriate x-axis limits
        plt.xlim(1.5, max(iterations) + 0.5)
        
        # Add value labels on points with better positioning
        for i, (x, y) in enumerate(zip(iterations, errors)):
            plt.annotate(f'{y:.6f}%', 
                        xy=(x, y), 
                        xytext=(0, 10),  # 10 points above the point
                        textcoords='offset points',
                        ha='center', 
                        fontsize=9,
                        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.9))

        plt.tight_layout()
        plt.savefig("false_position.png", dpi=300, bbox_inches='tight')
        plt.show()
        plt.close()
    return xr_old

if __name__ == "__main__":
    root = false_position(40, 80)
    print(f"\nFinal root: m = {root:.10f} kg")

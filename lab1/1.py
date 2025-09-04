from helper import bisection_with_log, display_table, plot_error

def polynomial_function(x: float) -> float:
    """
    Polynomial function:
    f(x) = 225 + 82x − 90x^2 + 44x^3 − 8x^4 + 0.7x^5
    """
    return 225.0 + 82.0 * x - 90.0 * x**2 + 44.0 * x**3 - 8.0 * x**4 + 0.7 * x**5

def solve_problem1():

    lower_bound, upper_bound = -1.2, -1.0

    # Run bisection method
    iterations = bisection_with_log(
        func=polynomial_function,
        lower=lower_bound,
        upper=upper_bound,
        tol_pct=0.05,   # stopping criterion in %
        max_iterations=100
    )

    # Display iteration table
    display_table(iterations, "Problem 1: Polynomial Root")

    # Plot approximate relative error
    plot_error(iterations, "Problem 1: Polynomial Root", "p1_approximate_error_plot.png")

# Execute directly
if __name__ == "__main__":
    solve_problem1()

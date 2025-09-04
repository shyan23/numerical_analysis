from helper import bisection_with_log, display_table, plot_error


FLOW_RATE = 20.0
GRAVITY = 9.81

def channel_width(depth: float) -> float:
    """Top width of the channel as a function of depth."""
    return 3.0 + depth

def channel_area(depth: float) -> float:
    """Cross-sectional area of the channel as a function of depth."""
    return 3.0 * depth + 0.5 * depth**2

def critical_depth_eq(depth: float) -> float:
    """Equation whose root gives the critical depth of flow."""
    return 1.0 - (FLOW_RATE**2) / (GRAVITY * (channel_area(depth)**3) * channel_width(depth))

def solve_problem2():
    """Solve for the critical depth using the bisection method."""
    lower_bound, upper_bound = 0.5, 2.5

    
    iterations = bisection_with_log(
        func=critical_depth_eq,
        lower=lower_bound,
        upper=upper_bound,
        tol_pct=1.0,# 1%    
        max_iterations=10
    )

    
    display_table(iterations, "Problem 2: Critical Depth")

    
    plot_error(iterations, "Problem 2: Critical Depth", "p2_approximate_error_plot.png")


if __name__ == "__main__":
    solve_problem2()

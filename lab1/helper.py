from typing import Callable, List, Optional
import matplotlib.pyplot as plt

def bisection_with_log(
    func: Callable[[float], float],
    lower: float,
    upper: float,
    tol_pct: float,
    max_iterations: int,
    true_val: Optional[float] = None
) -> List[dict]:
    
    a, b = lower, upper
    fa, fb = func(a), func(b)
    if fa * fb > 0:
        raise ValueError("Invalid interval: function values must have opposite signs.")

    log = []
    prev_mid = None

    for k in range(1, max_iterations + 1):
        mid = (a + b) / 2.0
        f_mid = func(mid)

        # Approximate relative error
        if prev_mid is None:
            approx_err = None
        else:
            approx_err = abs((mid - prev_mid) / mid) * 100 if mid != 0 else abs(mid - prev_mid) * 100

        # True error (if known)
        if true_val is not None:
            #true_err = abs((true_val - mid) / true_val) * 100 if true_val != 0 else abs(true_val - mid) * 100
            abs_err = abs(true_val - mid)
        else:
            true_err, abs_err = None, None

        log.append({
            "iter": k,
            "xl": a,
            "xu": b,
            "xr": mid,
            "f_xr": f_mid,
            "approx_rel_err": approx_err,
            "abs_err": abs_err
        })

        # Stop
        if approx_err is not None and approx_err < tol_pct:
            break

        # Update bounds
        if fa * f_mid < 0:
            b, fb = mid, f_mid
        else:
            a, fa = mid, f_mid

        prev_mid = mid

    return log


def  display_table(rows: List[dict], title: str) -> None:
    """Prints iteration results in a formatted table."""
    print(f"\n{title}")
    headers = ["iter", "xl", "xu", "xr", "f(xr)", "Approx Rel Error %", "Abs Error"]
    print("{:>4s} {:>14s} {:>14s} {:>14s} {:>14s} {:>24s} {:>18s}".format(*headers))

    for row in rows:
        def fmt(val): return f"{val:.10f}" if val is not None else "".ljust(10)
        print("{:4d} {:>14s} {:>14s} {:>14s} {:>14s} {:>24s} {:>18s}".format(
            row["iter"],
            fmt(row["xl"]),
            fmt(row["xu"]),
            fmt(row["xr"]),
            fmt(row["f_xr"]),
            fmt(row["approx_rel_err"]),
            fmt(row["abs_err"])
        ))


def plot_error(rows: List[dict], title: str, filename: str) -> None:
    """Plots the approximate relative error against iterations."""
    rel_errs = [r["approx_rel_err"] for r in rows if r["approx_rel_err"] is not None]
    iterations = list(range(1, len(rel_errs) + 1))

    plt.figure()
    plt.plot(iterations, rel_errs, marker="o")
    plt.xlabel("Iteration")
    plt.ylabel("Approximate Relative Error (%)")
    plt.title(title)
    plt.grid(True, linestyle=":")
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

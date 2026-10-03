"""Statistical Process Control (SPC) calculations for the Quality Inspection Management System."""
import statistics


def control_limits(samples):
    """Individuals control chart: mean and 3-sigma upper/lower control limits."""
    mean = statistics.mean(samples)
    sigma = statistics.stdev(samples)
    return {"mean": mean, "sigma": sigma, "ucl": mean + 3 * sigma, "lcl": mean - 3 * sigma}


def out_of_control(samples):
    """Return (position, value) for each measurement outside the 3-sigma limits."""
    limits = control_limits(samples)
    return [(i, x) for i, x in enumerate(samples) if x > limits["ucl"] or x < limits["lcl"]]


def process_capability(samples, lsl, usl):
    """Cp and Cpk: how well the process fits the spec limits (LSL/USL)."""
    mean = statistics.mean(samples)
    sigma = statistics.stdev(samples)
    cp = (usl - lsl) / (6 * sigma)
    cpk = min(usl - mean, mean - lsl) / (3 * sigma)
    return {"Cp": round(cp, 2), "Cpk": round(cpk, 2)}
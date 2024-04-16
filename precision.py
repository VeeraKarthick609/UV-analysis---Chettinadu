import numpy as np

def calculate_precision(amount_present):
    """
    Calculate precision.

    Parameters:
        amount_present (list): List of measured values.

    Returns:
        tuple: Tuple containing standard deviation and relative standard deviation.
    """
    standard_deviation = np.std(amount_present)
    mean_absorbance = np.mean(amount_present)
    relative_standard_deviation = (standard_deviation / mean_absorbance) * 100
    return standard_deviation, relative_standard_deviation

import numpy as np

def find_H_point(wavelengths, concentrations, absorbance1, absorbance2):
    """
    Find the H point concentration and absorbance.

    Parameters:
        wavelengths (list): List of wavelengths.
        concentrations (list): List of concentrations.
        absorbance1 (list): Absorbance values at wavelength 1.
        absorbance2 (list): Absorbance values at wavelength 2.

    Returns:
        tuple: Tuple containing H point concentration and H point absorbance.
    """
    regression1 = np.polyfit(concentrations, absorbance1, 1)
    regression2 = np.polyfit(concentrations, absorbance2, 1)
    H_concentration = (regression2[1] - regression1[1]) / (regression1[0] - regression2[0])
    H_absorbance = regression1[0] * H_concentration + regression1[1]
    return H_concentration, H_absorbance

def calculate_recovery(absorbance_measured, absorbance_expected):
    """
    Calculate recovery percentages for each measurement and average recovery percentage.

    Parameters:
        absorbance_measured (list): List of measured absorbance values.
        absorbance_expected (list): List of expected absorbance values.

    Returns:
        tuple: Tuple containing a list of recovery percentages for each measurement and the average recovery percentage.
    """
    recovery_percentages = [(measured / expected) * 100 for measured, expected in zip(absorbance_measured, absorbance_expected)]
    average_recovery_percentage = sum(recovery_percentages) / len(recovery_percentages)
    return recovery_percentages, average_recovery_percentage

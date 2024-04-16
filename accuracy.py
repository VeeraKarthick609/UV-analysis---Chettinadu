def calculate_accuracy(absorbance, dilution_factor, avg_tablet_weight, expected_concentration):
    """
    Calculate the accuracy given absorbance, dilution factor, average tablet weight, and expected concentration.
    
    Arguments:
    absorbance: The absorbance measured in the experiment.
    dilution_factor: The dilution factor used in the experiment.
    avg_tablet_weight: The average weight of the tablet used in the experiment.
    expected_concentration: The expected concentration of the substance.
    
    Returns:
    accuracy_percentage: The accuracy percentage calculated based on the given data.
    """
    try:
        # Calculate concentration from absorbance and dilution factor
        concentration = absorbance * dilution_factor
        
        # Calculate mass of substance from concentration and tablet weight
        mass_substance = concentration * avg_tablet_weight
        
        # Calculate accuracy percentage
        accuracy_percentage = (mass_substance / expected_concentration) * 100
        
        return accuracy_percentage
    except ZeroDivisionError:
        print("Error: Division by zero. Please provide a non-zero expected concentration.")

def calculate_purity(amount_found, label_claim):
    """
    Calculate the percentage purity.

    Parameters:
        amount_found (float): The amount found.
        label_claim (float): The label claim.

    Returns:
        float: The percentage purity.
    """
    return (amount_found / label_claim) * 100

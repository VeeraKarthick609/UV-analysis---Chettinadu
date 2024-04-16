import streamlit as st
import pandas as pd

from accuracy import calculate_accuracy
from purity import calculate_purity
from precision import calculate_precision
from recovery import calculate_recovery
from h_point import find_H_point
from linear_equation import calculate_x
from contour_plot import plot_contour, plot_interaction_contour

def main():
    st.title("Chemistry Analysis App")

    # Sidebar
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ("Accuracy", "Purity", "Precision", "Recovery", "H-Point", "Linear Equation", "Contour Plot", "Interaction Contour"))

    if page == "Accuracy":
        st.header("Accuracy Calculation")
        absorbance = st.number_input("Absorbance", value=0.0)
        dilution_factor = st.number_input("Dilution Factor", value=0.0)
        avg_tablet_weight = st.number_input("Average Tablet Weight (grams)", value=0.0)
        expected_concentration = st.number_input("Expected Concentration (mg/L)", value=0.0)

        if st.button("Calculate Accuracy"):
            accuracy = calculate_accuracy(absorbance, dilution_factor, avg_tablet_weight, expected_concentration)
            st.success(f"The accuracy is {accuracy:.2f}%.")

    elif page == "Purity":
        st.header("Percentage Purity Calculation")
        amount_found = st.number_input("Amount Found", value=0.0)
        label_claim = st.number_input("Label Claim", value=0.0)

        if st.button("Calculate Percentage Purity"):
            percentage_purity = calculate_purity(amount_found, label_claim)
            st.success(f"Percentage Purity: {percentage_purity:.2f}%")

    elif page == "Precision":
        st.header("Precision Calculation")
        amount_present = st.text_input("Enter comma-separated measured values:")
        if st.button("Calculate Precision"):
            amount_present_list = [float(x.strip()) for x in amount_present.split(",")]
            standard_deviation, relative_standard_deviation = calculate_precision(amount_present_list)
            st.success(f"Standard Deviation: {standard_deviation:.2f}")
            st.success(f"Relative Standard Deviation (RSD): {relative_standard_deviation:.2f}%")

    elif page == "Recovery":
        st.header("Recovery Study")
        absorbance_measured = st.text_input("Enter comma-separated measured absorbance values:")
        absorbance_expected = st.text_input("Enter comma-separated expected absorbance values:")
        if st.button("Calculate Recovery"):
            absorbance_measured_list = [float(x.strip()) for x in absorbance_measured.split(",")]
            absorbance_expected_list = [float(x.strip()) for x in absorbance_expected.split(",")]
            recovery_percentages, average_recovery_percentage = calculate_recovery(absorbance_measured_list, absorbance_expected_list)
            st.success(f"Recovery Percentages: {recovery_percentages}")
            st.success(f"Average Recovery Percentage: {average_recovery_percentage:.2f}%")

    elif page == "H-Point":
        st.header("H-Point Determination")
        # Input fields for wavelengths, concentrations, absorbance1, absorbance2
        wavelengths = st.text_input("Enter comma-separated wavelengths:")
        concentrations = st.text_input("Enter comma-separated concentrations:")
        absorbance1 = st.text_input("Enter comma-separated absorbance values at wavelength 1:")
        absorbance2 = st.text_input("Enter comma-separated absorbance values at wavelength 2:")
    
        if st.button("Find H-Point"):
            # Convert input strings to lists of floats
            wavelengths_list = [float(x.strip()) for x in wavelengths.split(",")]
            concentrations_list = [float(x.strip()) for x in concentrations.split(",")]
            absorbance1_list = [float(x.strip()) for x in absorbance1.split(",")]
            absorbance2_list = [float(x.strip()) for x in absorbance2.split(",")]
        
            # Call the function to find H-Point
            H_concentration, H_absorbance = find_H_point(wavelengths_list, concentrations_list, absorbance1_list, absorbance2_list)
        
            # Display the result
            st.success(f"The H-point concentration is: {H_concentration:.2f}")
            st.success(f"The H-point absorbance is: {H_absorbance:.2f}")


    elif page == "Linear Equation":
        st.header("Linear Equation Calculation")
        y = st.number_input("Enter the y-coordinate:", value=0.0)
        m = st.number_input("Enter the slope (m):", value=0.0)
        c = st.number_input("Enter the y-intercept (c):", value=0.0)
        if st.button("Calculate x"):
            x = calculate_x(y, m, c)
            st.success(f"The value of x is: {x:.2f}")


    elif page == "Contour Plot":
        st.header("Contour Plot")

        # File uploader for factor values
        st.subheader("Upload a CSV file containing factor values:")
        factor_file = st.file_uploader("Factor CSV file", type=["csv"])

        if st.button("Plot Contour") and factor_file:
            # Read CSV file and extract factor values
            factor_data = pd.read_csv(factor_file)
            factor1_values_list = factor_data['Factor 1'].tolist()
            factor2_values_list = factor_data['Factor 2'].tolist()
            factor3_values_list = factor_data['Factor 3'].tolist()
        
            # Call the function to plot contour
            plot_contour(factor1_values_list, factor2_values_list, factor3_values_list)

    elif page == "Interaction Contour":
        st.header("Interaction Contour Plot")
        # Add input fields or file uploader for CSV file containing factor values
        factor_file = st.file_uploader("Factor CSV file", type=["csv"])

        if st.button("Interaction Contour") and factor_file:
            # Read CSV file and extract factor values
            factor_data = pd.read_csv(factor_file)
            factor1_values_list = factor_data['Factor 1'].tolist()
            factor2_values_list = factor_data['Factor 2'].tolist()
            factor3_values_list = factor_data['Factor 3'].tolist()
        
            # Call the function to plot contour
            plot_interaction_contour(factor1_values_list, factor2_values_list, factor3_values_list)



if __name__ == "__main__":
    st.set_option('deprecation.showPyplotGlobalUse', False)

    main()

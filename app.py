import streamlit as st
import pandas as pd

# Assuming the custom modules are correctly placed in the same directory
from accuracy import calculate_accuracy
from purity import calculate_purity
from precision import calculate_precision
from recovery import calculate_recovery
from h_point import find_H_point
from linear_equation import calculate_x
from contour_plot import plot_contour, plot_interaction_contour

def main():
    st.title("Chemistry Analysis App")

    # Sidebar navigation
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
            st.success(f"The accuracy is {accuracy:.5f}%.")

    elif page == "Purity":
        st.header("Percentage Purity Calculation")
        amount_found = st.number_input("Amount Found", value=0.0)
        label_claim = st.number_input("Label Claim", value=0.0)

        if st.button("Calculate Percentage Purity"):
            percentage_purity = calculate_purity(amount_found, label_claim)
            st.success(f"Percentage Purity: {percentage_purity:.5f}%")

    elif page == "Precision":
        st.header("Precision Calculation")
        amount_present_file = st.file_uploader("Upload CSV file with measured values", type=["csv"])
        if amount_present_file:
            df = pd.read_csv(amount_present_file)
            st.write(df)  # Display the uploaded data frame
            if "Measured Values" in df.columns:
                amount_present_list = df["Measured Values"].tolist()
                if st.button("Calculate Precision"):
                    standard_deviation, relative_standard_deviation = calculate_precision(amount_present_list)
                    st.success(f"Standard Deviation: {standard_deviation:.5f}")
                    st.success(f"Relative Standard Deviation (RSD): {relative_standard_deviation:.5f}%")
            else:
                st.error("CSV must contain a 'Measured Values' column")

    elif page == "Recovery":
        st.header("Recovery Study")
        absorbance_measured_file = st.file_uploader("Upload CSV file with measured absorbance values", type=["csv"])
        absorbance_expected_file = st.file_uploader("Upload CSV file with expected absorbance values", type=["csv"])
        if absorbance_measured_file and absorbance_expected_file:
            df_measured = pd.read_csv(absorbance_measured_file)
            df_expected = pd.read_csv(absorbance_expected_file)
            st.write(df_measured)
            st.write(df_expected)
            if "Measured Absorbance" in df_measured.columns and "Expected Absorbance" in df_expected.columns:
                absorbance_measured_list = df_measured["Measured Absorbance"].tolist()
                absorbance_expected_list = df_expected["Expected Absorbance"].tolist()
                if st.button("Calculate Recovery"):
                    recovery_percentages, average_recovery_percentage = calculate_recovery(absorbance_measured_list, absorbance_expected_list)
                    st.success(f"Recovery Percentages: {recovery_percentages}")
                    st.success(f"Average Recovery Percentage: {average_recovery_percentage:.5f}%")
            else:
                st.error("CSV must contain 'Measured Absorbance' and 'Expected Absorbance' columns")

    elif page == "H-Point":
        st.header("H-Point Determination")
        data_file = st.file_uploader("Upload CSV file with data", type=["csv"])
        if data_file:
            df = pd.read_csv(data_file)
            st.write(df)
            required_columns = {"Wavelengths", "Concentrations", "Absorbance1", "Absorbance2"}
            if required_columns.issubset(df.columns):
                wavelengths_list = df["Wavelengths"].tolist()
                concentrations_list = df["Concentrations"].tolist()
                absorbance1_list = df["Absorbance1"].tolist()
                absorbance2_list = df["Absorbance2"].tolist()
                if st.button("Find H-Point"):
                    H_concentration, H_absorbance = find_H_point(wavelengths_list, concentrations_list, absorbance1_list, absorbance2_list)
                    st.success(f"The H-point concentration is: {H_concentration:.5f}")
                    st.success(f"The H-point absorbance is: {H_absorbance:.5f}")
            else:
                st.error("CSV must contain 'Wavelengths', 'Concentrations', 'Absorbance1', and 'Absorbance2' columns")

    elif page == "Linear Equation":
        st.header("Linear Equation Calculation")
        y = st.number_input("Enter the y-coordinate:", value=0.0)
        m = st.number_input("Enter the slope (m):", value=0.0)
        c = st.number_input("Enter the y-intercept (c):", value=0.0)
        if st.button("Calculate x"):
            x = calculate_x(y, m, c)
            st.success(f"The value of x is: {x:.5f}")

    elif page == "Contour Plot":
        st.header("Contour Plot")
        st.subheader("Upload a CSV file containing factor values:")
        factor_file = st.file_uploader("Factor CSV file", type=["csv"])

        if factor_file:
            factor_data = pd.read_csv(factor_file)
            if all(col in factor_data.columns for col in ["Factor 1", "Factor 2", "Factor 3"]):
                factor1_values_list = factor_data['Factor 1'].tolist()
                factor2_values_list = factor_data['Factor 2'].tolist()
                factor3_values_list = factor_data['Factor 3'].tolist()
                if st.button("Plot Contour"):
                    plot_contour(factor1_values_list, factor2_values_list, factor3_values_list)
            else:
                st.error("CSV must contain 'Factor 1', 'Factor 2', and 'Factor 3' columns")

    elif page == "Interaction Contour":
        st.header("Interaction Contour Plot")
        factor_file = st.file_uploader("Factor CSV file", type=["csv"])

        if factor_file:
            factor_data = pd.read_csv(factor_file)
            if all(col in factor_data.columns for col in ["Factor 1", "Factor 2", "Factor 3"]):
                factor1_values_list = factor_data['Factor 1'].tolist()
                factor2_values_list = factor_data['Factor 2'].tolist()
                factor3_values_list = factor_data['Factor 3'].tolist()
                if st.button("Interaction Contour"):
                    plot_interaction_contour(factor1_values_list, factor2_values_list, factor3_values_list)
            else:
                st.error("CSV must contain 'Factor 1', 'Factor 2', and 'Factor 3' columns")

if __name__ == "__main__":
    st.set_option('deprecation.showPyplotGlobalUse', False)
    main()

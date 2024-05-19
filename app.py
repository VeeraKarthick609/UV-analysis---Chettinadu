import streamlit as st
import pandas as pd

from accuracy import calculate_accuracy
from purity import calculate_purity
from precision import calculate_precision
from recovery import calculate_recovery
from h_point import find_H_point
from linear_equation import calculate_x
from contour_plot import plot_contour, plot_interaction_contour

def create_table_input(columns, example_data):
    """Create a table input widget with given columns and example data."""
    st.write(f"Enter data in the table below (columns: {', '.join(columns)}):")
    example_df = pd.DataFrame(example_data, columns=columns)
    df = st.data_editor(example_df, num_rows="dynamic")
    return df

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
        df = create_table_input(columns=["Measured Values"], example_data=[[10.0], [15.5], [20.0]])

        if st.button("Calculate Precision"):
            if "Measured Values" in df.columns:
                amount_present_list = df["Measured Values"].tolist()
                standard_deviation, relative_standard_deviation = calculate_precision(amount_present_list)
                st.success(f"Standard Deviation: {standard_deviation:.5f}")
                st.success(f"Relative Standard Deviation (RSD): {relative_standard_deviation:.5f}%")
            else:
                st.error("Input must contain a 'Measured Values' column")

    elif page == "Recovery":
        st.header("Recovery Study")
        df_measured = create_table_input(columns=["Measured Absorbance"], example_data=[[0.1], [0.2], [0.3]])
        df_expected = create_table_input(columns=["Expected Absorbance"], example_data=[[0.1], [0.2], [0.3]])

        if st.button("Calculate Recovery"):
            if "Measured Absorbance" in df_measured.columns and "Expected Absorbance" in df_expected.columns:
                absorbance_measured_list = df_measured["Measured Absorbance"].tolist()
                absorbance_expected_list = df_expected["Expected Absorbance"].tolist()
                recovery_percentages, average_recovery_percentage = calculate_recovery(absorbance_measured_list, absorbance_expected_list)
                st.success(f"Recovery Percentages: {recovery_percentages}")
                st.success(f"Average Recovery Percentage: {average_recovery_percentage:.5f}%")
            else:
                st.error("Input must contain 'Measured Absorbance' and 'Expected Absorbance' columns")

    elif page == "H-Point":
        st.header("H-Point Determination")
        df = create_table_input(columns=["Wavelengths", "Concentrations", "Absorbance1", "Absorbance2"],
                                example_data=[[400, 0.5, 0.2, 0.3], [450, 0.6, 0.25, 0.35]])

        if st.button("Find H-Point"):
            if all(col in df.columns for col in ["Wavelengths", "Concentrations", "Absorbance1", "Absorbance2"]):
                wavelengths_list = df["Wavelengths"].tolist()
                concentrations_list = df["Concentrations"].tolist()
                absorbance1_list = df["Absorbance1"].tolist()
                absorbance2_list = df["Absorbance2"].tolist()
                H_concentration, H_absorbance = find_H_point(wavelengths_list, concentrations_list, absorbance1_list, absorbance2_list)
                st.success(f"The H-point concentration is: {H_concentration:.5f}")
                st.success(f"The H-point absorbance is: {H_absorbance:.5f}")
            else:
                st.error("Input must contain 'Wavelengths', 'Concentrations', 'Absorbance1', and 'Absorbance2' columns")

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
        df = create_table_input(columns=["Factor 1", "Factor 2", "Factor 3"], example_data=[[1, 2, 3], [4, 5, 6]])

        if st.button("Plot Contour"):
            if all(col in df.columns for col in ["Factor 1", "Factor 2", "Factor 3"]):
                factor1_values_list = df['Factor 1'].tolist()
                factor2_values_list = df['Factor 2'].tolist()
                factor3_values_list = df['Factor 3'].tolist()
                plot_contour(factor1_values_list, factor2_values_list, factor3_values_list)
            else:
                st.error("Input must contain 'Factor 1', 'Factor 2', and 'Factor 3' columns")

    elif page == "Interaction Contour":
        st.header("Interaction Contour Plot")
        df = create_table_input(columns=["Factor 1", "Factor 2", "Factor 3"], example_data=[[1, 2, 3], [4, 5, 6]])

        if st.button("Interaction Contour"):
            if all(col in df.columns for col in ["Factor 1", "Factor 2", "Factor 3"]):
                factor1_values_list = df['Factor 1'].tolist()
                factor2_values_list = df['Factor 2'].tolist()
                factor3_values_list = df['Factor 3'].tolist()
                plot_interaction_contour(factor1_values_list, factor2_values_list, factor3_values_list)
            else:
                st.error("Input must contain 'Factor 1', 'Factor 2', and 'Factor 3' columns")

if __name__ == "__main__":
    st.set_option('deprecation.showPyplotGlobalUse', False)
    main()

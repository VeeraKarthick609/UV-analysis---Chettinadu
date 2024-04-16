import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def plot_contour(factor1_values, factor2_values, factor3_values):
    # Create a meshgrid for the three factors
    factor1_grid, factor2_grid, factor3_grid = np.meshgrid(factor1_values, factor2_values, factor3_values)

    # Define the response function (replace this with your actual response function)
    response = factor1_grid ** 2 + factor2_grid ** 2 - factor3_grid ** 2

    # Plot contour plot
    plt.figure(figsize=(10, 10))
    contour = plt.contourf(factor1_grid[:,:,0], factor2_grid[:,:,0], response[:,:,0], cmap='viridis')  # Adjusted index to 0
    plt.colorbar(contour, label='Response')
    plt.xlabel('Factor 1')
    plt.ylabel('Factor 2')
    plt.title('Contour Plot of Response with Factor 1, Factor 2, Factor 3')
    plt.grid(True)

    # Display plot in Streamlit app
    st.pyplot()

def plot_interaction_contour(factor1_values, factor2_values, factor3_values):
    """
    Plot an interaction contour plot.

    Parameters:
        factor1_values (ndarray): Values of factor 1.
        factor2_values (ndarray): Values of factor 2.
        factor3_values (ndarray): Values of factor 3.
    """
    # Generate a meshgrid from the factor values
    factor1_grid, factor2_grid, factor3_grid = np.meshgrid(factor1_values, factor2_values, factor3_values)

    # Define the response function (replace this with your actual response function)
    response = factor1_grid ** 2 + factor2_grid ** 2 - factor3_grid ** 2

    # Get the size of the third axis
    size_axis_2 = response.shape[2]

    # Choose the index within the bounds of the third axis
    index = min(size_axis_2 - 1, 25)

    # Plot interaction contour plot
    fig, ax = plt.subplots(figsize=(10, 7))
    contour = ax.contourf(factor1_grid[:,:,0], factor2_grid[:,:,0], response[:,:,index], cmap='viridis')
    plt.colorbar(contour, ax=ax, label='Response')
    plt.xlabel('Factor 1')
    plt.ylabel('Factor 2')
    plt.title('Contour Plot of Response with Factor 1, Factor 2, Factor 3')
    plt.grid(True)

    # Display plot in Streamlit app
    st.pyplot()
    
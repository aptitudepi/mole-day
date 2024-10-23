#!/usr/bin/env python3
# Devkumar Banerjee

import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu

periodic_table_df = pd.read_csv("periodic_table.csv")

def home_page():
    st.title("🧪 Welcome to the Mole Calculator")
    st.write("Explore the world of chemistry with our comprehensive mole calculator!")
    
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Mole_day.svg/1200px-Mole_day.svg.png", width=400)
    
    st.markdown("""
    ### What is a mole?
    A mole is a unit of measurement used in chemistry to express amounts of a chemical substance. 
    One mole is defined as the amount of substance containing exactly 6.02214076 × 10²³ elementary entities.
    
    ### Why is it important?
    The mole concept allows chemists to:
    - Perform stoichiometric calculations
    - Relate microscopic properties to macroscopic observations
    - Standardize chemical measurements
    
    Explore our calculators to learn more about moles and their applications in chemistry!
    """)

def mole_calculators():
    st.title("🧮 Mole Calculators")
    
    calculator = st.selectbox("Choose a calculator:", 
                              ["Moles to Mass", "Mass to Moles", "Moles to Particles", "Particles to Moles"])
    if calculator == "Moles to Mass":
        st.subheader("Moles to Mass Calculator")
        moles = st.number_input("Enter number of moles:", min_value=0.0, format="%.4f")
        element = st.selectbox("Select an element:", periodic_table_df["Element"])
        molar_mass = periodic_table_df.loc[periodic_table_df["Element"] == element, "AtomicMass"].values[0]
        st.write(f"Molar Mass: {molar_mass} g/mol")
        if st.button("Calculate Mass"):
            mass = moles * molar_mass
            st.success(f"Mass: {mass:.4f} g")

    elif calculator == "Mass to Moles":
        st.subheader("Mass to Moles Calculator")
        mass = st.number_input("Enter mass (g):", min_value=0.0, format="%.4f")
        element = st.selectbox("Select an element:", periodic_table_df["Element"])
        molar_mass = periodic_table_df.loc[periodic_table_df["Element"] == element, "AtomicMass"].values[0]
        st.write(f"Molar Mass: {molar_mass} g/mol")
        if st.button("Calculate Moles"):
            moles = mass / molar_mass
            st.success(f"Moles: {moles:.4f} mol")    
    elif calculator == "Moles to Particles":
        st.subheader("Moles to Particles Calculator")
        moles = st.number_input("Enter number of moles:", min_value=0.0, format="%.4f")
        if st.button("Calculate Particles"):
            particles = moles * 6.02214076e23
            st.success(f"Particles: {particles:.4e}")
    elif calculator == "Particles to Moles":
        st.subheader("Particles to Moles Calculator")
        particles = st.number_input("Enter number of particles:", min_value=0.0, format="%.4e")
        if st.button("Calculate Moles"):
            moles = particles / 6.02214076e23
            st.success(f"Moles: {moles:.4f} mol")

def mole_conversions():
    st.title("↔️ Mole Conversions")
    
    st.write("Explore the relationship between moles and other units.")
    
    conversion_data = {
        "From": ["Moles", "Grams", "Liters (at STP)", "Particles"],
        "To": ["Grams", "Moles", "Moles", "Moles"],
        "Conversion Factor": ["× Molar Mass", "÷ Molar Mass", "÷ 22.4", "÷ 6.02214076 × 10²³"]
    }
    
    df = pd.DataFrame(conversion_data)
    st.table(df)
    
    st.subheader("Interactive Conversion Calculator")
    from_unit = st.selectbox("Convert from:", ["Moles", "Grams", "Liters (at STP)", "Particles"])
    to_unit = st.selectbox("Convert to:", ["Moles", "Grams", "Liters (at STP)", "Particles"])
    value = st.number_input("Enter value:", format="%.6f")
    molar_mass = st.number_input("Enter molar mass (g/mol) if applicable:", min_value=0.0, format="%.4f")
    
    if st.button("Convert"):
        if from_unit == "Moles" and to_unit == "Grams":
            result = value * molar_mass
            st.success(f"{value} moles = {result:.4f} grams")
        elif from_unit == "Grams" and to_unit == "Moles":
            result = value / molar_mass
            st.success(f"{value} grams = {result:.4f} moles")
        elif from_unit == "Moles" and to_unit == "Liters (at STP)":
            result = value * 22.4
            st.success(f"{value} moles = {result:.4f} liters at STP")
        elif from_unit == "Liters (at STP)" and to_unit == "Moles":
            result = value / 22.4
            st.success(f"{value} liters at STP = {result:.4f} moles")
        elif from_unit == "Moles" and to_unit == "Particles":
            result = value * 6.02214076e23
            st.success(f"{value} moles = {result:.4e} particles")
        elif from_unit == "Particles" and to_unit == "Moles":
            result = value / 6.02214076e23
            st.success(f"{value} particles = {result:.4f} moles")
        else:
            st.warning("Direct conversion not available. Please use moles as an intermediate step.")

def about_page():
    st.title("ℹ️ About This App")
    
    st.write("""
    This Mole Calculator app was created to help chemistry students and enthusiasts understand and work with the concept of moles.
    
    ### Features:
    - Various mole-related calculators
    - Conversion tools
    - Educational information about moles
    
    ### How to use:
    1. Navigate through the sidebar menu
    2. Choose the calculator or conversion tool you need
    3. Input the required values
    4. Get instant results!
    
    ### Feedback:
    We're constantly working to improve this app. If you have any suggestions or find any issues, please let us know!
    
    Happy calculating! 🧪🔬
    """)

    st.info("Did you know? If you had a mole of standard sized marbles, they would cover the entire Earth to a depth of 50 miles!")

    st.subheader("Quick Mole Quiz")
    quiz_question = st.radio(
        "What is the approximate number of particles in one mole?",
        ("6 × 10²²", "6 × 10²³", "6 × 10²⁴", "6 × 10²⁵")
    )
    if quiz_question == "6 × 10²³":
        st.success("Correct! One mole contains approximately 6.02214076 × 10²³ particles.")
    else:
        st.error("Not quite. The correct answer is 6 × 10²³ (more precisely, 6.02214076 × 10²³).")

def main():
    # Set page configuration
    st.set_page_config(page_title="Mole Calculator", page_icon="🧪", layout="centered")

    # Custom CSS for styling
    # Sidebar navigation
    with st.sidebar:
        selected = option_menu(
            menu_title="Navigation",
            options=["Home", "Mole Calculators", "Mole Conversions", "About"],
            icons=["house", "calculator", "arrow-left-right", "info-circle"],
            menu_icon="flask",
            default_index=0,
        )

    # Page routing
    if selected == "Home":
        home_page()
    elif selected == "Mole Calculators":
        mole_calculators()
    elif selected == "Mole Conversions":
        mole_conversions()
    elif selected == "About":
        about_page()

    # Add a footer

if __name__ == "__main__":
    main()

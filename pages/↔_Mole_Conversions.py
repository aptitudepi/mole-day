import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

def mole_conversions():
    st.title("↔️ Mole Conversions")
    st.write("Explore the relationship between moles and other units.")
    # Define static conversion data outside the function
    conversion_data = {
        "From": ["Moles", "Grams", "Liters (at STP)", "Particles"],
        "To": ["Grams", "Moles", "Moles", "Moles"],
        "Conversion Factor": ["× Molar Mass", "÷ Molar Mass", "÷ 22.4", "÷ 6.02214076 × 10²³"]
    }
    df = pd.DataFrame(conversion_data)
    # Display static conversion table
    st.table(df)
    st.subheader("Interactive Conversion Calculator")
    from_unit = st.selectbox("Convert from:", df["From"])
    to_unit = st.selectbox("Convert to:", ["Moles", "Grams", "Liters (at STP)", "Particles"])
    value = st.number_input(f"Enter initial number of {from_unit}:", format="%.6f")
    # Only show molar mass input when necessary
    molar_mass = 0.0
    if from_unit in ["Moles", "Grams"] or to_unit in ["Moles", "Grams"]:
        molar_mass = st.number_input("Enter molar mass (g/mol) if applicable:", min_value=0.0, format="%.4f")
    if st.button("Convert"):
        result = None
        if from_unit == "Moles":
            if to_unit == "Grams":
                result = value * molar_mass
            elif to_unit == "Liters (at STP)":
                result = value * 22.4
            elif to_unit == "Particles":
                result = value * 6.02214076e23
        elif from_unit == "Grams" and to_unit == "Moles":
            result = value / molar_mass
        elif from_unit == "Liters (at STP)" and to_unit == "Moles":
            result = value / 22.4
        elif from_unit == "Particles" and to_unit == "Moles":
            result = value / 6.02214076e23
        if result is not None:
            st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
        else:
            st.warning("Direct conversion not available. Please use moles as an intermediate step.")

def main():
    mole_conversions()

if __name__ == "__main__":
    main()

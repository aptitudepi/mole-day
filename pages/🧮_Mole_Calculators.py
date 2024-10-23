import streamlit as st
import pandas as pd
from molmass import Formula


st.set_page_config(layout="wide")

# Cache the loading of periodic table data
@st.cache_data
def load_periodic_table():
    return pd.read_csv("data/periodic_table.csv")


def mole_calculators():
    # Load data at startup
    periodic_table_df = load_periodic_table()

    st.title("🧮 Mole Calculators")
    calculator = st.selectbox("Choose a calculator:",["Moles to Mass", "Mass to Moles", "Moles to Particles", "Particles to Moles"])
    if calculator in ["Moles to Mass", "Mass to Moles"]:
        st.subheader(f"{calculator} Calculator")
        # Add option for chemical compounds
        input_type = st.radio("Input type:", ["Element", "Compound"])
        if input_type == "Element":
            # Handle element selection
            elements = ["Custom"] + list(periodic_table_df["Element"])
            element = st.selectbox("Select an element or choose 'Custom':", elements)
            if element == "Custom":
                molar_mass = st.number_input("Enter custom molar mass (g/mol):", min_value=0.0, format="%.4f")
            else:
                molar_mass = periodic_table_df.loc[periodic_table_df["Element"] == element, "AtomicMass"].values[0]
                st.write(f"Molar Mass: {molar_mass} g/mol")
        else:
            # Handle compound input
            compound_formula = st.text_input("Enter compound formula:")
            if compound_formula:
                try:
                    formula = Formula(compound_formula)
                    molar_mass = formula.mass
                    st.write(f"Molecular Weight: {molar_mass:.4f} g/mol")
                except Exception as e:
                    st.error(f"Invalid formula: {e}")
        if calculator == "Moles to Mass":
            moles = st.number_input("Enter number of moles:", min_value=0.0, format="%.4f")
            if st.button("Calculate Mass"):
                mass = moles * molar_mass
                st.success(f"Mass: {mass:.4f} g")
        elif calculator == "Mass to Moles":
            mass = st.number_input("Enter mass (g):", min_value=0.0, format="%.4f")
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

def main():
    mole_calculators()

if __name__ == "__main__":
    main()

import streamlit as st

st.set_page_config(layout="wide")

def about_page():
    st.title("🧪 Discover the Mole Calculator")
    st.write("Dive into the fascinating world of chemistry with our versatile mole calculator!")
    st.markdown("""
    ### Understanding the Mole
    In chemistry, a *mole* is a fundamental unit used to quantify the amount of a substance. It is defined by Avogadro's number, which is approximately 6.02214076 × 10²³ particles.

    ### Significance of the Mole Concept
    The concept of the mole is crucial for chemists as it enables them to:
    - Conduct stoichiometric calculations with precision
    - Connect microscopic properties with macroscopic phenomena
    - Ensure consistency in chemical measurements

    Use our calculators to deepen your understanding of moles and their vital role in chemical analysis!
    """)

def main():
    about_page()

if __name__ == "__main__":
    main()

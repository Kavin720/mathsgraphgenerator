import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x = sp.symbols('x')

st.title("📈 Function Graph Plotter")

st.write("Enter function (use ** for power, * for multiplication, / for division, + for addition and - for subraction)")

user_input = st.text_input("Function")
choice = st.selectbox("Range", ["Small", "Medium", "Large", "Custom"])


# -------------------------
# RANGE SELECTION
# -------------------------
if choice == "Small":
    xmin, xmax = -10, 10

elif choice == "Medium":
    xmin, xmax = -50, 50

elif choice == "Large":
    xmin, xmax = -500, 500

else:
    xmin = st.number_input("Lower bound", value=-10, step=1)
    xmax = st.number_input("Upper bound", value=10, step=1)


# -------------------------
# VALIDATION FIRST
# -------------------------
if xmin >= xmax:
    st.error("Invalid range: lower bound must be less than upper bound")

elif user_input == "":
    st.warning("Enter a function first")

else:
    try:
        # convert function
        expr = sp.sympify(user_input)

        f = sp.lambdify(x, expr, "numpy")

        x_vals = np.linspace(xmin, xmax, 400)
        y_vals = f(x_vals)

        # plot
        fig, ax = plt.subplots()
        ax.plot(x_vals, y_vals)
        ax.axhline(0, color="black")
        ax.axvline(0, color="black")
        ax.set_title(f"Graph of {user_input}")

        st.pyplot(fig)

    except:
        st.error("❌ Invalid function. Use ** for power, * for multiplication, / for division, + for addition and - for subraction ")

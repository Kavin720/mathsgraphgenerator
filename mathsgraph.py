import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x = sp.symbols('x')

st.title("📈 Function Graph Plotter")

st.write("Enter a function of x (example: x**2 + 3*x)")

user_input = st.text_input("Function")

if user_input:

    try:
        # convert to sympy expression
        expr = sp.sympify(user_input)

        # convert sympy → numpy function
        f = sp.lambdify(x, expr, "numpy")

        # generate x values
        x_vals = np.linspace(-10, 10, 400)

        # compute y values
        y_vals = f(x_vals)

        # plot
        fig, ax = plt.subplots()
        ax.plot(x_vals, y_vals)
        ax.axhline(0, color="black")
        ax.axvline(0, color="black")
        ax.set_title(f"Graph of {user_input}")

        st.pyplot(fig)

    except:
        st.error("❌ Invalid function. Use ** to represent power, * to represent multiplication, + to represent addition and - to represent subraction")

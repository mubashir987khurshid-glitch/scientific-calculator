import streamlit as st
import math

st.set_page_config(page_title="Scientific Calculator", page_icon="🧮")
st.title("🧮 Scientific Calculator")

# Operation selection first
operation = st.selectbox(
    "Select operation",
    [
        "Addition", "Subtraction", "Multiplication", "Division",
        "Square", "Square Root", "Power", "Logarithm (base e)", "Logarithm (base 10)",
        "Sine", "Cosine", "Tangent", "Factorial"
    ]
)

# Input fields
if operation == "Factorial":
    num = st.number_input("Enter a number", min_value=0, step=1, format="%d")
else:
    num = st.number_input("Enter first number", value=0.0, format="%.6f")

num2 = None
if operation in ["Addition", "Subtraction", "Multiplication", "Division", "Power"]:
    num2 = st.number_input("Enter second number", value=0.0, format="%.6f")

# Degree/Radian choice for trig functions
angle_mode = None
if operation in ["Sine", "Cosine", "Tangent"]:
    angle_mode = st.radio("Angle mode", ["Degrees", "Radians"], horizontal=True)

# Perform calculation
result = None
try:
    if operation == "Addition":
        result = num + num2
    elif operation == "Subtraction":
        result = num - num2
    elif operation == "Multiplication":
        result = num * num2
    elif operation == "Division":
        if num2 != 0:
            result = num / num2
        else:
            st.error("Error: Cannot divide by zero!")
    elif operation == "Square":
        result = num ** 2
    elif operation == "Square Root":
        if num >= 0:
            result = math.sqrt(num)
        else:
            st.error("Error: Negative number cannot have a real square root!")
    elif operation == "Power":
        result = math.pow(num, num2)
    elif operation == "Logarithm (base e)":
        if num > 0:
            result = math.log(num)
        else:
            st.error("Error: Logarithm undefined for non-positive numbers!")
    elif operation == "Logarithm (base 10)":
        if num > 0:
            result = math.log10(num)
        else:
            st.error("Error: Logarithm undefined for non-positive numbers!")
    elif operation in ["Sine", "Cosine", "Tangent"]:
        value = num if angle_mode == "Radians" else math.radians(num)
        if operation == "Sine":
            result = math.sin(value)
        elif operation == "Cosine":
            result = math.cos(value)
        elif operation == "Tangent":
            if math.isclose(math.cos(value), 0, abs_tol=1e-9):
                st.error("Error: Tangent undefined at this angle!")
            else:
                result = math.tan(value)
    elif operation == "Factorial":
        result = math.factorial(int(num))
except Exception as e:
    st.error(f"An error occurred: {e}")

# Show result
if result is not None:
    st.success(f"Result: {result}")

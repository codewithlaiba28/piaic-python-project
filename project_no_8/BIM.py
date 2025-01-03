import streamlit as st
import pandas as pd

st.title("BMI calculator")
height = st.slider("Enter your height (in cm):",100 , 250 , 175 )
weight = st.slider("Enter your weight (in kg):",40, 200 , 70)

bmi = weight / ((height / 100 ) ** 2)
st.write(f"Your BMI is{bmi:.2f}")

st.write("### BMI Categories ###")
st.write("_ UnderWeight: BMI less than 18.5")
st.write("_ Normal Weight: BMI between 18.5 and 24.9")
st.write("_ OverWeight: BMI between 25 and 29.9")
st.write("_ Obesity: BMI between 30 and greater")
import streamlit as st
from PIL import Image

st.set_page_config(page_title="¡Hola neurona!", layout="centered")

img = Image.open("img/neurona.png")
st.image(img, width=800)

st.markdown("<h1 style='text-align: center;'>¡Hola neurona!</h1>", unsafe_allow_html=True)

tabs = st.tabs(["Una entrada", "Dos entradas", "Tres entradas y sesgo"])

with tabs[0]:
	w0 = st.slider("Peso w₀", min_value=0.0, max_value=5.0, value=0.0, step=0.01, key="w0_1")
	x0 = st.number_input("Entrada x₀", min_value=-100.0, max_value=100.0, value=0.0, step=0.01, key="x0_1")
	if st.button("Calcular la salida", key="btn1"):
		y = w0 * x0
		st.success(f"Salida: {y:.2f}")

with tabs[1]:
	col1, col2 = st.columns(2)
	with col1:
		w0 = st.slider("Peso w₀", min_value=0.0, max_value=5.0, value=0.0, step=0.01, key="w0_2")
		x0 = st.number_input("Entrada x₀", min_value=-100.0, max_value=100.0, value=0.0, step=0.01 , key="x0_2")
	with col2:
		w1 = st.slider("Peso w₁", min_value=0.0, max_value=5.0, value=0.0, step=0.01 , key="w1_2")
		x1 = st.number_input("Entrada x₁", min_value=-100.0, max_value=100.0, value=0.0, step=0.01 , key="x1_2")
	if st.button("Calcular la salida", key="btn2"):
		y = w0 * x0 + w1 * x1
		st.success(f"Salida: {y:.2f}")

with tabs[2]:
	col1, col2, col3 = st.columns(3)
	with col1:
		w0 = st.slider("Peso w₀", min_value=0.0, max_value=5.0, value=0.0, step=0.01 , key="w0_3")
		x0 = st.number_input("Entrada x₀", min_value=-100.0, max_value=100.0, value=0.0, step=0.01 , key="x0_3")
	with col2:
		w1 = st.slider("Peso w₁", min_value=0.0, max_value=5.0, value=0.0, step=0.01 , key="w1_3")
		x1 = st.number_input("Entrada x₁", min_value=-100.0, max_value=100.0, value=0.0, step=0.01 , key="x1_3")
	with col3:
		w2 = st.slider("Peso w₂", min_value=0.0, max_value=5.0, value=0.0, step=0.01 , key="w2_3")
		x2 = st.number_input("Entrada x₂", min_value=-100.0, max_value=100.0, value=0.0, step=0.01 , key="x2_3")
	sesgo = st.number_input("Introduzca el valor del sesgo", min_value=-100.0, max_value=100.0, value=0.0, step=0.01 , key="sesgo_3")
	if st.button("Calcular la salida", key="btn3"):
		y = w0 * x0 + w1 * x1 + w2 * x2 + sesgo
		st.success(f"Salida: {y:.2f}")
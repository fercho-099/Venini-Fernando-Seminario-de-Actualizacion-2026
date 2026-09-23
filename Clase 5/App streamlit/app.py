import streamlit as st

st.title("Mi primera app con Streamlit")
st.write("Hola desde una app mínima funcionando correctamente.")

name = st.text_input("Tu nombre", "mundo")
number = st.slider("Selecciona un número", 0, 100, 25)

st.success(f"¡Hola, {name}! Has elegido el valor {number}.")

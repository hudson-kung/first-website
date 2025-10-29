import streamlit as st
import pandas as pa
import numpy as np

running = True
if st.toggle("Hi"):
    st.write("on")
else:
    st.write("off")


number = st.slider("How Happy Are You?", 1, 5, 3)
# Initialization
if 'value' not in st.session_state:
    st.session_state['value'] = 0


emojis = ["💀", "😠", "😐", "🙂", "😄"]
st.write(emojis[number -1])
np.random.choice([True, False]),

title = st.text_input("Choose A Color", "Orange")
st.write(title)

if st.button("+1"):
    st.session_state.value += 1

if st.button("+10"):
    st.session_state.value += 10

if st.button("+100"):
    st.session_state.value += 100

if running:
    st.write(st.session_state.value)
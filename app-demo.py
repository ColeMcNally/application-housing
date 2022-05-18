import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'name':['John', 'Mary', 'Tom'],
    'gender':['male', 'female', 'male'],
    'age':[20, 22, 21],
})

st.write(df)
st.write(df.plot())
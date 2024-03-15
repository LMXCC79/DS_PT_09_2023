import seaborn as sns
import pandas as pd
import streamlit as st

df = sns.load_dataset('penguins')

st.title ('ejemplo del uso del st.write()')
st.write('Hola: sunglasses :heart:')
st.write(1+1)


a = 2**3
st.write(a*5)
st.write(df.head(5))
st.write('st.write("tex"), df')
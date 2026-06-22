import streamlit as st
import pandas as pd
import numpy as np

## title of the app

st.title("hello webapp")


st.write("simple hfhaudbciadbvba")


df = pd.read_csv('csvdata.csv')
df.head(10)
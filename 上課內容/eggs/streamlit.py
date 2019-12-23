import streamlit as st
import pandas as pd
st.title("歡迎光臨")
df = pd.DataFrame({
    "A":[12,13,45],"B":[15,87,53]
    })

st.write(df)

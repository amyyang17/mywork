import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
st.title("這是一張圖")
st.markdown(r"這是張$\dfrac{\sin(x)}{x}$")
x=np.linspace(-10,10,200)
y=np.sinc(x)
plt.plot(x,y)

st.pyplot()
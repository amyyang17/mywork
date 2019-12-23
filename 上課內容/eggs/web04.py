import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
city=st.selectbox("居住地",["台北","新北","高雄"])
st.write(f"你選擇了{city}")
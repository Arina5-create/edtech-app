import numpy as np
import plotly.graph_objects as go
import streamlit as st
st.title('калькулятор среднего балла')
text=st.text_input('оценки(через пробел):')

a =[int(x) for x in text.split()]
sr  = np.mean(a)
st.write(f'**средний балл:**{sr:.2f}')

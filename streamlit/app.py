import streamlit as st
import pandas as pd
import numpy as np

#title of the application
st.title("Hello Streamlit")

#display a simple text
st.write("This is a simple text")

#Create a simpel dataframe and work onto
df = pd.DataFrame({
    "first":[1, 2, 3, 4],
    "second":[10, 20, 30, 40]
})
st.write(df)

chart_data=pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(chart_data)
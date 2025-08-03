import streamlit as st
import pandas as pd


st.title("Welcome")

#text_input
name=st.text_input("Enter your name: ")

#slider
age=st.slider("Select your age: ", 0, 100,25)



#selectbox
options=["Python", "C++", "Java"]
choice = st.selectbox(f"Choose your CP Language: ", options) 

st.write(f"Hello {name}")
st.write(f"your age is {age}")
st.write(f"you selected {choice}  ")


#using pandas data
data={
    "name":["Jenil", "Mansi", "vikshita"],
    "age":[19, 21, 22],
    "city":["Kumbakonam", "Kumbakonam", "Kumbakonam"]
}

st.write("DATA of SIBLINGS: ")
df=pd.DataFrame(data)
df.to_csv("sample.csv")
st.write(df)

#File uploader
uploaded_file = st.file_uploader("Choose a csv file", type="csv")
if uploaded_file:
    df=pd.read_csv(uploaded_file)
    st.write(df)

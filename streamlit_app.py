import streamlit as st

st.title("CalcGPA")
st.header("Semester GPA Calculator for the BTech of IPU")

name = st.text_input('Full Name')
if(len(name) != 0):
    st.write("Hello! ", name)
    Semester = st.number_input('Semester', min_value = 0, max_value = 8, step = 1)

col1, col2 = st.columns(2);

with st.container:
    if(Semester == 1):
        st.write("Enter your Marks!")
        with col1:
            with st.expander("Theory Marks"):
                st.number_input("Programming in C/Applied Chemistry", min_value=0, max_value=100, step=1)


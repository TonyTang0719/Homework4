import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

st.title("W4_Wednesday")
st.markdown("JIACHEN TANG 83049912")

rng=np.random.default_rng(seed=20)
if "ans" not in st.session_state:
    st.session_state["ans"]= rng.integers(0,100,size=(2,5))

A=rng.integers(0,100,size=(2,5))
st.write(A)
c=A.max()
st.write(c)
choice=st.radio("Do you want to search the column?", options=["Rows","Columns"])

ans=st.number_input(label="Enter the row number",value=2)
translate={"Rows":"row", "Columns":"column"}
st.write(f"The user answered {ans}")
try:
    if choice=="Rows":
        v=A[ans]
    elif choice=="Columns":
        v=A[:,ans]
    if choice=="Rows":
        if (v==c).sum()>0:
            st.write("You are correct")
        else:
            st.write("Not correct")
    elif choice=="Columns":
        if (v==c).sum()>0:
            st.write("You are correct")
        else:
            st.write("Not correct")
except IndexError:
    st.write("Enter a valid input")



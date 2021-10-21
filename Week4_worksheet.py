# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from altair.vegalite.v4.schema.channels import Color
import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
#Step1
st.title("Week4 Worksheet")
#Step2
st.markdown('Jiachen Tang id83049912, Here (https://github.com/TonyTang0719) is the link to Github')
#Step3
uploaded_file = st.file_uploader("Upload a CSV file",type="csv")
#Step4
try:
    df = pd.read_csv(uploaded_file) 
    st.write(df)
except ValueError:
    st.write("error")
#Step5    
df1=df.applymap(lambda x:np.nan if x==" " else x)    
#Step6
def can_be_numeric(df_input, c):
    try:
        pd.to_numeric(df_input[c])
        return True
    except:
        return False
my_list = [c for c in df1.columns if can_be_numeric(df1, c)]
st.write(my_list)
#Step7
df1[my_list] = df1[my_list].apply(pd.to_numeric, axis = 0)
#Step8
Xcoordinate=st.selectbox(label = "Choose the x-axis", options = my_list)
Ycoordinate=st.selectbox(label = "Choose the y-axis", options = my_list)
#Step9
SelctRange=st.slider(label = "Choose the range for the plot", max_value = len(df1), value = 100)
#Step10
st.write(f"Aftering chooosing your X-axis {Xcoordinate} , your Y-axis {Ycoordinate} , and your range of the plot {SelctRange} , Let's make the plot right now ")
#Step11
charted = alt.Chart(df1[0:SelctRange]).mark_circle().encode(
        x = alt.X(Xcoordinate),
        y = alt.Y(Ycoordinate)
    ).properties(
        width = 800,
        height = 400
    )

st.altair_chart(charted, use_container_width=True)

#Step12
chart_data=pd.DataFrame(df1[my_list],columns=[Xcoordinate,Ycoordinate])
st.area_chart(chart_data)
    

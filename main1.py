import streamlit as t
from package1 import odometrt,main
t.sidebar.header("Hello!")
a=t.sidebar.selectbox("Select feacture you want",options=["BMI Calculator","Check Inventory","set background black","set background white"],
                     
                      )
if t.sidebar.button("background color"):
     t.markdown("""
                <style>
               .stApp{
               background-color:#0E1117;
            
               }    
               </style>

""",unsafe_allow_html=True)



t.header("Welcome to Single Plaitform ")
if a=="BMI Calculator":
    
    b=odometrt.odometer1()
if a=="Check Inventory":
    b=main.inventory()  

   

import streamlit as t
from package1 import odometrt,main
t.sidebar.header("Hello!")
a=t.sidebar.selectbox("Select feacture you want",options=["BMI Calculator","Check Inventory"],
                     
                      )
#initialisation of theme
if "theme" not in t.session_state:
    t.session_state.theme="light"
if t.sidebar.button("Dark mode"):
    t.session_state.theme="dark"
if t.sidebar.button("Light mode"):
    t.session_state.theme="white"
#apply
if t.session_state.theme=="dark":
    t.success("Dark mode on &#127769;")
    t.image("https://images.pexels.com/photos/399973/pexels-photo-399973.jpeg",width=20)
    t.markdown("""
               <style>
               .stApp{
               background-color:#0E1117;
               color:white;
               }
              
               
               </style>
          

               
               
               """,unsafe_allow_html=True)
else:
    t.success("Light mode on  &#9728;")
    t.markdown("""
    <style>
               .tApp{
               background-color:white;
               color:black;
               }
    </style>           

""",unsafe_allow_html=True)

t.header("Welcome to Single Plaitform ")
if a=="BMI Calculator":
    
    b=odometrt.odometer1()
if a=="Check Inventory":
    b=main.inventory()  

   

import streamlit as st1
import plotly.graph_objects as go


def odometer1():
    st1.markdown("""
        <style>
                 stApp{
                 background-color:
                 var(--background-color);
                 color:var(--text-color);
                 }
        st.Button>button{
                 background-color:
                 var(--primary-color);
                 color:var(--text-color);
                 }
                 </style>




     """,unsafe_allow_html=True)
    st1.title("input based odometer")
    weight=st1.number_input("enter your weight(kg) ",min_value=1.0,step=0.5)                    
    height=st1.number_input("enter your height(cm)",min_value=50.0,step=1.0) 
    bmi=0                                        
    if st1.button("calculate BMI"):
        height_M= height/100
        bmi=weight/(height_M**2)   
        st1.subheader(f"your BMI is:{bmi:.2f} ")    
    if bmi<18.5:
        st1.warning("Category: underweight")
    elif 18.5<=bmi<25:
        st1.success("Category:Normal Weight")
    else:
        st1.error("enter coorect credentils")
    st1.plotly_chart(odometer(bmi)) 
def  odometer(value):
    fig=go.Figure(go.Indicator( 
        mode="gauge+number",
        value=value,
        title={"text":"odometer"},
        gauge={ 
            "axis":{"range":[0,30]},
            "steps":[
                {"range":[0,10],"color":"lightgreen"  },
                {"range":[10,25],"color":"yellow"},
                {"range":[25,30],"color":"red"},
            
            ],
          
            }
        
    ))
    return fig

# def odometer1():
#     st1.title("input based odometer")
#     weight=st1.number_input("enter your weight(kg) ",min_value=1.0,step=0.5)                    
#     height=st1.number_input("enter your height(cm)",min_value=50.0,step=1.0) 
#     bmi=0                                        
#     if st1.button("calculate BMI"):
#         height_M= height/100
#         bmi=weight/(height_M**2)   
#         st1.subheader(f"your BMI is:{bmi:.2f} ")    
#     if bmi<18.5:
#         st1.warning("Category: underweight")
#     elif 18.5<=bmi<25:
#         st1.success("Category:Normal Weight")
#     else:
#         st1.error("enter coorect credentils")
#     st1.plotly_chart(odometer(bmi)) 
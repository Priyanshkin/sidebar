import pandas as pd
import streamlit as st
from datetime import datetime
import plotly.express as pl
def inventory():
    def deldata():
        return pd.DataFrame(columns=["product_id", 
                            "product_name",
                            "product_price",
                            "product_category",
                            "product_qnantity",
    ])
    delted_data=deldata()
    delted_data.to_csv("deleted.csv",index=False)
    delted_data["Deleteddate"]=datetime.now().date()
    delted_data=delted_data.drop("product_qnantity",axis=1)
    delted_data=delted_data.drop("qnantity",axis=1,inplace=True,errors="ignore")
    # delted_data["quantity"]=0
    # delted_data["product_quantity"]=0

    def load_data():
        return pd.read_csv("inventory.csv",)
    df=load_data()
    df["Dateadded"]=datetime.now().date() 
    # df=df.drop("product_qnantity",axis=1)    
    # df["product_quantity"]="500gm"
    # df["quantity"]="1peces"  
    # df=df.drop("qnantity",axis=1,inplace=True,errors='ignore')
    st.title("shop inventory management system")
    #add new product
    st.subheader("Add Product")
    with st.form("Add_form"):
        id=st.number_input("enter product id",step=1)
        name=st.text_input("product name")
        price=st.number_input("enter price of product",step=1)
        quantity=st.selectbox("enter product quantity",options=["1litre","1kg","500ml","250ml","100ml","250gm","100gm","other"])
        category=st.selectbox("select category",options=["Ayaurvedic","Puja product","other"])
        stock=st.number_input("select quantity",step=1)
        submit=st.form_submit_button("Add product")
        if submit:
            new_row={
                "product_id":id,
            "product_name":name,
            "product_price": price,
                "product_category":category,
                "product_quantity":quantity,
                "quantity":stock

            }
            df=pd.concat([df,pd.DataFrame([new_row])
                        ],ignore_index=True
                        )
            df.to_csv("inventory.csv",index=False)
            st.success("product added")
    if st.button("check inventory"):
        st.dataframe(df)
    st.subheader("Delete product")
    del_id=st.selectbox("enter a product_id",options=df["product_id"],
            # format_func=lambda x:f"{x}-{df[df['product_id']]['product_name'].values[0]}"              
                        
                        )
    if st.button("Deleted"):
        # if(df[df["product_id"]==del_id]):
        #   delted_data=df[df["product_id"]==del_id]
        #   delted_data.to_csv("deleted.csv",index=False)
            delted_data=df[df["product_id"]==del_id]  
            delted_data.to_csv("deleted.csv",index=False)
            st.warning("Deleted item Saved in recyicle bin")
            if not delted_data.empty:
                df=df[df["product_id"]!=del_id]  
                df.to_csv("inventory.csv",index=False)
                st.warning("item deleted")
                st.dataframe(df)
            else:
                st.warning("product id is not exist")
    if st.button("Check graph"):
        fig=pl.bar(
            df,
            x="product_name",
            y="quantity",
            color="product_name",
            text="product_name",

        )   
        st.plotly_chart(fig)






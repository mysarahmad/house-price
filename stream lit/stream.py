from os import name
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pickle
model=pickle.load(open('house.pkl','rb'))


st.write('''
# House price prediction of metropolian cities in india
 Check the house prices of yoyr favourite city.
         ''')
st.write('---')

st.sidebar.header('Specify Input Parameters')

def house_pred(seller_type,bedroom,layout_type,property_type,area,furnish_type,bathroom,city):
    prediction=model.predict([[seller_type,bedroom,layout_type,property_type,area,furnish_type,bathroom,city]])
    print(prediction)
    return prediction

def main():
    st.title("Type the Inputs")
    seller_type=st.text_input("seller_type")
    bedroom=st.text_input("bedroom")
    layout_type=st.text_input("layout_type")
    property_type=st.text_input("property_type")
    area=st.text_input("area")
    furnish_type=st.text_input("furnish_type")
    bathroom=st.text_input("bathroom")
    city=st.text_input("city")
    result=""
    if st.button("predict"):
        result = house_pred(seller_type,bedroom,layout_type,property_type,area,furnish_type,bathroom,city)
    st.success("the output is {}".format(result))


 

if __name__=='__main__':
    main()
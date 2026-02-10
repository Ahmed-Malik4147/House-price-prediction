import pickle
import streamlit as st
import pandas as pd

with open('Model.pkl','rb') as f:
    load_data = pickle.load(f)

area = st.slider('area',500,10000)
bedrooms = st.slider('bedrooms',1,6)
bathrooms = st.slider('bathroom',1,5)
stories = st.slider('stories',1,4)
parking= st.slider('parking',0,3)
mainroad= st.slider('mainroad',0,1)

if st.button('predication final score'):
    model = pd.DataFrame({
        'area':[area],
        'bedrooms':[bedrooms],
        'bathrooms':[bathrooms],
        'stories':[stories],
        'parking':[parking],
        'mainroad':[mainroad]
    })

    prediction = load_data.predict(model)
    st.success(f"Predicted Final: **{prediction[0]:.2f}**")
import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.header('Datos disponibles')
st.write(car_data)

options = st.multiselect('elige el dato a graficar', ['price', 'model_year','condition' ,'cylinders', 'fuel','odometer'])
hist_button = st.button('Construir histograma') # crear un botón
disper_button = st.button('Construye un grafico de dispersion') 


if hist_button: # al hacer clic en el botón
    st.write('Creación de un histograma para el conjunto de datos de precio de venta de coches')         
    fig = px.histogram(car_data, x=options)
    st.plotly_chart(fig, use_container_width=True)

if disper_button: # al hacer clic en el botón
    st.write('Creación de un grafico de dispersion para el consumo de gasolina')
            
    fig = px.scatter(car_data, x=options)
    st.plotly_chart(fig, use_container_width=True)


 


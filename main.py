import streamlit as st
from functions import *

st.title("Consulta de Clima :sun_small_cloud:")
st.write("Digite o nome da cidade para obter as informações do clima.")

city_name = st.text_input("Nome da cidade:")
if st.button(":mag_right: Consultar Clima"):
    if city_name:
        weather_data = get_weather(city_name)
        if weather_data["cod"] == 401:
            st.error(f"Problema durante requisição!\nMensagem: {weather_data['message']}")
        elif weather_data["cod"] != "404":
            description_weather = weather_data["weather"][0]["description"]
            temperature = weather_data["main"]["temp"]

            st.write(f"**Clima em {city_name}:** {description_weather.capitalize()}")
            st.write(f"**Temperatura:** {temperature:.2f}ºC")
        else:
            st.error("Cidade não encontrada!")
    else:
        st.warning("Por favor, insira o nome da cidade!")

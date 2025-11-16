import pandas as pd
import streamlit as st
from PIL import Image
import altair as alt

st.markdown(
    """
    <style>
        .css-18e3th9, .css-1d391kg, .stApp {
            background-color: #bfdbda;
        }
        .center-text {
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 class='center-text' style='color:#042927; font-weight:bold; font-style:italic;'>Análisis de datos de Sensores en Mi Ciudad</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='center-text'>Trabajo hecho por Dante Chona Cuervo</h3>", unsafe_allow_html=True)

image = Image.open('grafana2.jpg')
st.image(image)

uploaded_file = st.file_uploader('Choose a file')

if uploaded_file is not None:
    df1 = pd.read_csv(uploaded_file)

    st.markdown("<h3 class='center-text'>Perfil gráfico de la variable medida.</h3>", unsafe_allow_html=True)
    df1 = df1.set_index('Time')

    chart = (
        alt.Chart(df1.reset_index())
        .mark_line(color='#042927')
        .encode(
            x='Time:T',
            y=alt.Y(df1.columns[0], type='quantitative')
        )
    )

    st.altair_chart(chart, use_container_width=True)

    st.write(df1)

    st.markdown("<h3 class='center-text'>Estadísticos básicos de los sensores.</h3>", unsafe_allow_html=True)
    st.dataframe(df1["temperatura ESP32"].describe())

    min_temp = st.slider('Selecciona valor mínimo del filtro ', min_value=-10, max_value=45, value=23, key=1)
    filtrado_df_min = df1.query(f"`temperatura ESP32` > {min_temp}")
    st.markdown("<h3 class='center-text'>Temperaturas superiores al valor configurado.</h3>", unsafe_allow_html=True)
    st.write('Dataframe Filtrado')
    st.write(filtrado_df_min)

    max_temp = st.slider('Selecciona valor máximo del filtro ', min_value=-10, max_value=45, value=23, key=2)
    filtrado_df_max = df1.query(f"`temperatura ESP32` < {max_temp}")
    st.markdown("<h3 class='center-text'>Temperaturas Inferiores al valor configurado.</h3>", unsafe_allow_html=True)
    st.write('Dataframe Filtrado')
    st.write(filtrado_df_max)

else:
    st.warning('Necesitas cargar un archivo csv excel.')

import streamlit as st #Framework
import pandas as pd #Biblioteca para trabalhar o excel
import plotly.express as px #Biblioteca para ajudar com gráficos

def main():
    data = pd.read_excel('Base.xlsx', sheet_name='Base')
    título = 'dashboard - Projetos Vendas'
    st.set_page_config(page_title=título,layout="wide")
    st.title(título)

    anos = data['Ano'].unique()
    países = data['País'].unique()

    filtro_ano = st.sidebar.selectbox("Selecione o Ano:", options=['Todos'] + sorted(anos), index=0)
    filtro_País = st.sidebar.selectbox("Selecione o País:", options=['Todos'] + sorted(países), index=0)

    data_filtrada = data.copy()
    if filtro_ano != 'Todos':
        data_filtrada = data_filtrada[data_filtrada['Ano'] == filtro_ano]
    if filtro_País !='Todos':
        data_filtrada = data_filtrada[data_filtrada['País'] == filtro_País]
 
main()
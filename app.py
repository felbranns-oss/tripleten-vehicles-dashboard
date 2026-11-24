import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title='Análise Exploratória de Anúncios de Veículos (EUA)',
    page_icon='🚗',
    layout='wide',
)

st.header('Análise Exploratória de Anúncios de Veículos (EUA)')

st.write(
    'Este aplicativo permite explorar de forma interativa os anúncios de '
    'vendas de veículos nos Estados Unidos. Use os botões abaixo para gerar '
    'um histograma da quilometragem (odômetro) ou um gráfico de dispersão '
    'relacionando quilometragem e preço. Os valores ausentes nas colunas '
    'numéricas são ignorados automaticamente pelos gráficos.'
)

car_data = pd.read_csv('vehicles_us.csv')

st.caption(f'Conjunto de dados: {len(car_data):,} anúncios e {car_data.shape[1]} colunas.'.replace(',', '.'))

hist_button = st.button('Criar histograma')

if hist_button:
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de '
        'vendas de carros (distribuição da quilometragem / odômetro).'
    )
    fig = px.histogram(
        car_data,
        x='odometer',
        nbins=50,
        title='Distribuição da quilometragem (odômetro)',
        labels={'odometer': 'Odômetro (milhas)'},
    )
    fig.update_layout(yaxis_title='Número de anúncios')
    st.plotly_chart(fig, use_container_width=True)

disp_button = st.button('Criar gráfico de dispersão')

if disp_button:
    st.write(
        'Criando um gráfico de dispersão para o conjunto de dados de '
        'anúncios de vendas de carros (odômetro versus preço).'
    )
    fig = px.scatter(
        car_data,
        x='odometer',
        y='price',
        title='Relação entre quilometragem (odômetro) e preço',
        labels={'odometer': 'Odômetro (milhas)', 'price': 'Preço (USD)'},
        opacity=0.4,
    )
    st.plotly_chart(fig, use_container_width=True)

show_type = st.checkbox('Mostrar distribuição de preços por tipo de veículo')

if show_type:
    st.write(
        'Distribuição de preços por tipo de veículo. Anúncios sem tipo ou '
        'sem preço (caso existam) são excluídos antes da visualização.'
    )
    type_data = car_data.dropna(subset=['type', 'price'])
    fig = px.box(
        type_data,
        x='type',
        y='price',
        title='Distribuição de preços por tipo de veículo',
        labels={'type': 'Tipo de veículo', 'price': 'Preço (USD)'},
    )
    fig.update_layout(xaxis_tickangle=-30)
    st.plotly_chart(fig, use_container_width=True)

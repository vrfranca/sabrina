# Importa os pacotes necessários
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Importa as variáveis globais
from dados import _global_df

def app():
    # Adiciona o banner de imagem usando st.image
    st.image("Banner_steam.png", use_container_width=True)
    
    # Usa o estilo personalizado para criar a linha separadora
    st.markdown('<div class="custom-divider" ></div>', unsafe_allow_html=True)

    # Referenciando o arquivo styles.css do streamlit
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

    # Acessando os dados armazenados na variável global
    # Exclui do dataset as colunas desnecessárias para a analise de popularidade
    df = _global_df[['Ano', 'Media de Tempo de Jogo', 'Preco']]
    
    # Definir um plano de cores específico
    color_sequence = ['#F0F0F0', '#FFD700', '#009B3A', '#002776']

###########################################################################
#### PREPARANDO OS DADOS ####

    # Crio o data set com as colunas que vou usar
    df_agrupado = df.groupby('Ano')['Media de Tempo de Jogo'].mean().reset_index(name='Media de horas')

    fig = px.line(
        df_agrupado,
        x='Ano',
        y='Media de horas',
        title='Media de horas por Ano',
        labels={
            'Ano': 'Ano',
            'Media de horas': 'Media de horas'
        },
        markers=True,
        text='Media de horas',
        )
    
    # usado para indicar que são suas casas decimais
    fig.update_traces(texttemplate='%{text:.2f}', textposition='top center')

    st.plotly_chart(fig)

    st.markdown('''<p style="color: white;text-align: justify;">
                <strong>Linha ascendente:</strong> Indica que, ao longo dos anos, as pessoas passaram a jogar mais. <br> 
                <strong>Linha descendente:</strong> Sugere que o tempo de jogo médio diminuiu ao longo dos anos.  <br><br>
                Picos ou quedas inesperadas podem sugerir mudanças no comportamento dos jogadores em determinados anos, como influências externas (lançamento de novos jogos, eventos ou mudanças culturais).
                Portanto, esse gráfico é útil para analisar como o tempo médio de jogo evolui ao longo dos anos, permitindo identificar padrões, comportamentos e possíveis fatores que influenciam a média de horas jogadas em diferentes períodos.                                                                                    
                <br><br><br></p>''', unsafe_allow_html=True)
    
    ###########################################################################
#### PREPARANDO OS DADOS ####

    # Crio o data set com as colunas que vou usar
    df_agrupado = df.groupby('Ano')['Preco'].mean().reset_index(name='Media de preco')

    fig = px.line(
        df_agrupado,
        x='Ano',
        y='Media de preco',
        title='Media de preco por Ano',
        labels={
            'Ano': 'Ano',
            'Media de preco': 'Media de preco'
        },
        markers=True,
        text='Media de preco',
        )
    
    # usado para indicar que são suas casas decimais
    fig.update_traces(texttemplate='%{text:.2f}', textposition='top center')

    st.plotly_chart(fig)

    st.markdown('''<p style="color: white;text-align: justify;">
                O gráfico é valioso para identificar <strong>tendências de longo prazo</strong> e compreender 
                como os preços se ajustam ao longo dos anos. Pode ser útil para <strong>estratégias 
                de precificação, análise de competitividade no mercado</strong>, ou até mesmo para 
                avaliar o impacto de fatores externos sobre o comportamento dos preços.<br><br>
                Quando se está lidando com um mercado específico 
                como o de jogos, o gráfico é uma boa ferramenta para observar como os 
                preços dessa categoria se comportam ao longo do tempo,
                 além de ajudar a prever futuros movimentos no mercado.<br><br>
                Esse tipo de gráfico é especialmente útil para análises econômicas, 
                estudos de mercado e decisões estratégicas baseadas em tendências de preços.                                      
                <br><br><br></p>''', unsafe_allow_html=True)

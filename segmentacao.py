# Importa os pacotes necessários
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Importa as variáveis globais
from dados import _global_df

def app():
    # Adiciona o banner de imagem usando st.image
    st.image("Banner_steam.png", use_column_width=True)
    
    # Usa o estilo personalizado para criar a linha separadora
    st.markdown('<div class="custom-divider" ></div>', unsafe_allow_html=True)

    # Referenciando o arquivo styles.css do streamlit
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

    # Acessando os dados armazenados na variável global
    # Exclui do dataset as colunas desnecessárias para a analise de popularidade
    df = _global_df[['Jogo', 'Editora', 'Desenvolvedor', 'Plataforma']]
    
    # Definir um plano de cores específico
    color_sequence = ['#F0F0F0', '#FFD700', '#009B3A', '#002776']
    
    ### Exibição dos dados ###
########################################################
    df_agrupado = df.groupby('Editora')['Jogo'].nunique().reset_index(name='Total de Jogos')

    top20 = df_agrupado.sort_values(by='Total de Jogos', ascending = False)

    top20 = top20.head(20)

    fig = px.bar(
        top20,
        x='Editora',
        y='Total de Jogos',
        title='Jogos por Editora',
        labels={
            'Editora': 'Editora',
            'Total de Jogos': 'Total de Jogos'
        },
        orientation='v',
        text='Total de Jogos'
    )
    st.plotly_chart(fig)

    st.markdown('''<span style="color: white;">
            Este gráfico é útil para observar quais editoras têm o maior portfólio de jogos. Editoras com barras mais altas indicam que elas publicaram um número significativamente maior de jogos, 
                enquanto editoras com barras mais baixas podem ter um número menor de lançamentos.<br>
            Por exemplo, a editora "Big Fish Games" tem uma barra alta, isso indica que ela tem um grande número de jogos publicados, enquanto uma editora com uma barra mais baixa,
                 como uma empresa independente, pode ter um portfólio mais modesto.<br>
            Em resumo, o gráfico oferece uma visão clara da distribuição de jogos por editora, permitindo comparar facilmente o impacto e a produção de diferentes editoras no mercado de jogos.
            <br><br><br>''', unsafe_allow_html=True)
    
    ######################################################################

    df_plataforma = df[['Jogo', 'Plataforma']]

    # Separar as plataforma em listas de forma segura
    df_plataforma['Plataforma'] = df_plataforma['Plataforma'].str.split(';')

    # Explodir a coluna de gêneros, criando uma linha para cada plataforma
    df_plataforma = df_plataforma.explode('Plataforma', ignore_index=True)

    df_agrupado = df_plataforma.groupby('Plataforma')['Jogo'].nunique().reset_index(name='Total de Jogos')

    fig = px.bar(
        df_agrupado,
        x='Plataforma',
        y='Total de Jogos',
        title='Jogos por Plataforma',
        labels={
            'Plataforma': 'Plataforma',
            'Total de Jogos': 'Total de Jogos'
        },
        orientation='v',
        text='Total de Jogos'
    )
    
    st.plotly_chart(fig)

    st.markdown('''<span style="color: white;">
            Este gráfico permite visualizar rapidamente quais plataformas têm o maior número de jogos disponíveis. 
                Plataformas com barras mais altas indicam que possuem um portfólio maior de títulos, enquanto plataformas com barras mais baixas podem indicar uma quantidade menor de jogos.<br>
            Por exemplo, a plataforma "Windowns" tem uma barra mais alta, isso sugere que a plataforma tem um grande número de jogos disponíveis, 
                possivelmente devido à sua natureza aberta e à variedade de desenvolvedores. Já uma plataforma com uma barra mais baixa, como mac, mais recente ou menos popular, 
                pode ter um número menor de jogos lançados até o momento.<br>
            Em resumo, o gráfico oferece uma visão clara da distribuição de jogos por plataforma, 
                permitindo comparações diretas sobre quais plataformas dominam o mercado de jogos em termos de quantidade de títulos.
            <br><br><br>''', unsafe_allow_html=True)

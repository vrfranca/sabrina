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
    df = _global_df[['Media de Tempo de Jogo', 'Categorias', 'Generos']]
    
    # Definir um plano de cores específico
    color_sequence = ['#F0F0F0', '#FFD700', '#009B3A', '#002776']

##############################################

    ### Preparação dos dados ###

    # Crio o data set com as colunas que vou usar
    df_categoria = df[['Media de Tempo de Jogo', 'Categorias']]

    # Separo as Categorias em listas de forma segura
    df_categoria['Categorias'] = df_categoria['Categorias'].str.split(';')

    # Explodo a coluna de Categorias, criando uma linha para cada categoria
    df_categoria = df_categoria.explode('Categorias', ignore_index=True)

    # Agrupo as informações que preciso com base na media de jogo
    df_agrupado = df_categoria.groupby('Categorias')['Media de Tempo de Jogo'].mean().reset_index(name='Tempo por categoria')

    # Pego o top 10
    df_agrupado = df_agrupado.sort_values(by='Tempo por categoria', ascending = False)

    #top10 = top10.head(10)

    # Gero o grafico da MEDIA DE HORAS JOGADAS POR CATEGORIA
    fig = px.bar(
        df_agrupado,
        x='Categorias',
        y='Tempo por categoria',
        title='Horas de jogo por categoria',
        labels={
            'Categorias': 'Categorias',
            'Tempo por categoria': 'Tempo por categoria'
        },
        orientation='v',
        text='Tempo por categoria',
        text_auto='.2f'
        )

    # Exibo o grafico
    st.plotly_chart(fig)

    #### INFORMAÇÕES SOBRE O GRAFICO ####
    st.markdown('''<p style="color: white;text-align: justify;">
                Esse tipo de visualização nos permite entender quais categorias estão atraindo mais tempo de jogo, permitindo uma análise comparativa rápida entre elas.
                Por exemplo, uma categoria com uma barra mais alta indica que ela está dominando em termos de tempo jogado, enquanto categorias com barras mais baixas 
                sugerem menos engajamento ou popularidade entre os jogadores. <br>           
                Em resumo, o gráfico oferece uma visão clara e direta sobre as preferências dos jogadores em relação às categorias de jogos, ajudando a identificar tendências de comportamento.                                                                                  
                <br><br><br></p>''', unsafe_allow_html=True)

##############################################

### Preparação dos dados ###

    # Crio o data set com as colunas que vou usar
    df_genero = df[['Media de Tempo de Jogo', 'Generos']]

    # Separo as Categorias em listas de forma segura
    df_genero['Generos'] = df_genero['Generos'].str.split(';')

    # Explodo a coluna de Categorias, criando uma linha para cada categoria
    df_genero = df_genero.explode('Generos', ignore_index=True)

    # Agrupo as informações que preciso com base na media de jogo
    df_agrupado = df_genero.groupby('Generos')['Media de Tempo de Jogo'].mean().reset_index(name='Tempo por genero')

    # Pego o top 10
    df_agrupado = df_agrupado.sort_values(by='Tempo por genero', ascending = False)

    #top10 = top10.head(10)

    # Gero o grafico da MEDIA DE HORAS JOGADAS POR GENERO
    fig = px.bar(
        df_agrupado,
        x='Generos',
        y='Tempo por genero',
        title='Horas de jogo por genero',
        labels={
            'Generos': 'Generos',
            'Tempo por genero': 'Tempo por genero'
        },
        orientation='v',
        text='Tempo por genero',
        text_auto='.2f'
        )

    # Exibo o grafico
    st.plotly_chart(fig)

    st.markdown('''<p style="color: white;text-align: justify;">
                Esse gráfico é útil para observar quais gêneros de jogos estão consumindo mais tempo dos jogadores.<br>
                Por exemplo, o gênero "Massively Multiplayer" tem uma barra mais alta, isso indica que os jogadores tendem a passar mais tempo jogando jogos desse tipo, enquanto um gênero com uma barra mais baixa, como "Casual", sugere um engajamento médio mais modesto ou uma preferência por sessões de jogo mais curtas.<br>
                Em resumo, o gráfico oferece insights sobre o comportamento dos jogadores em relação aos diferentes gêneros de jogos, ajudando a identificar quais gêneros são mais atrativos em termos de tempo investido e proporcionando uma base para análises mais profundas sobre o perfil dos jogadores.<br>                                                                      
                <br><br><br></p>''', unsafe_allow_html=True)

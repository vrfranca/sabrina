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
    df = _global_df[['Plataforma', 'Preco', 'Editora']]
    
    # Definir um plano de cores específico
    color_sequence = ['#F0F0F0', '#FFD700', '#009B3A', '#002776']

    #################################
    ## Preparando os dados da tabela ##
    df_plataforma = df[['Preco', 'Plataforma']]

    # Separar as plataforma em listas de forma segura
    df_plataforma['Plataforma'] = df_plataforma['Plataforma'].str.split(';')

    # Explodir a coluna de gêneros, criando uma linha para cada plataforma
    df_plataforma = df_plataforma.explode('Plataforma', ignore_index=True)

    df_agrupado = df_plataforma.groupby('Plataforma')['Preco'].mean().reset_index(name='Media de preco')

    fig = px.bar(
        df_agrupado,
        x='Plataforma',
        y='Media de preco',
        title='Preco medio por plataforma',
        labels={
            'Plataforma': 'Plataforma',
            'Media de preco': 'Media de preco'
        },
        orientation='v',
        text='Media de preco',
        text_auto= '.2f'
    )

    st.plotly_chart(fig)

    st.markdown('''<p style="color: white;text-align: justify;">A visualização permite observar rapidamente a disparidade de preços médios entre as diferentes plataformas.
                Ela pode ajudar desenvolvedores e editores a entender como os preços dos jogos podem ser ajustados com base na plataforma e seu público-alvo.
                Para os consumidores, a análise oferece uma boa referência para decidir onde investir, dependendo do tipo de jogo e preço que buscam.                                                                                   
                <br><br><br></p>''', unsafe_allow_html=True)
    
    #################################
    ## Preparando os dados da tabela ##

    df_agrupado = df.groupby('Editora')['Preco'].mean().reset_index(name='Preco por Editora')

    top20 = df_agrupado.sort_values(by='Preco por Editora', ascending = False)

    top20 = top20.head(20)
    
    fig = px.bar(
        top20,
        x='Editora',
        y='Preco por Editora',
        title='Preco por Editora',
        labels={
            'Editora': 'Editora',
            'Preco por Editora': 'Preco por Editora'
        },
        orientation='v',
        text='Preco por Editora'
    )

    st.plotly_chart(fig)

    st.markdown('''<p style="color: white;  text-align: justify;">O gráfico de barras permite comparar os preços médios dos produtos entre diferentes editoras,
                 facilitando a identificação de quais têm preços mais altos ou mais baixos. 
                Ele também ajuda a detectar outliers, ou seja, editoras cujos preços se destacam de forma significativa das demais,
                 o que pode refletir estratégias de precificação diferenciadas ou características específicas de mercado. <br>
                Essa comparação direta é útil para consumidores que buscam produtos mais acessíveis ou mais caros, 
                além de fornecer insights sobre a posição de cada editora no mercado.
                Além disso, se os preços representarem valores agregados, como o preço médio de livros, 
                pode-se investigar os motivos por trás de preços mais altos, como maior prestígio,
                custo de produção elevado ou foco em nichos específicos. 
                Essa análise pode ser útil para editoras que desejam ajustar suas estratégias de preços, 
                assim como para consumidores que buscam entender as diferenças de preços entre editoras no mercado.                                                                
                <br><br><br></p>''', unsafe_allow_html=True)
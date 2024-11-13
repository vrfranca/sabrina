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
    df = _global_df[['ID Jogo', 'Jogo', 'Avaliacoes Positivas', 'Avaliacoes Negativas', 'Total Avaliacoes Jogo']]
    
    # Definir um plano de cores específico
    color_sequence = ['#F0F0F0', '#FFD700', '#009B3A', '#002776']
    
    ### Exibição dos dados ###
    
    # Ordenar o dataset de popularidade pelo maior núemro de avaliações
    df_ordenado = df.sort_values(by='Total Avaliacoes Jogo', ascending = False)
    
    # Exibir a tabela interativa
    st.markdown(''':blue[***Tabela com dados de origem***]''')
    
    # Exibe a tabela com os dados originais
    st.dataframe(df)
    
    # Grafico do TOP 20 Jogos com mais avaliações recebidas
    top10 = df_ordenado.head(20)
    top10 = top10[['Jogo', 'Total Avaliacoes Jogo']]
    fig = px.bar(
        top10,
        x='Total Avaliacoes Jogo',
        y='Jogo',
        title='TOP 20 - Jogos com mais avaliações',
        labels={
            'Jogo': 'Jogo',
            'Total Avaliacoes Jogo': 'Total de Avaliações'
        },
        orientation='h',
        text='Total Avaliacoes Jogo'
    )
    fig.update_traces(textposition='outside', texttemplate='%{text:.0f}')
    
    # Configurações para centralizar o título e adicionar uma borda
    fig.update_layout(
        title_x=0.5,  # Centraliza o título
        margin=dict(l=150, r=20, t=60, b=20),  # Ajusta as margens para deixar espaço
        height=600,  # Ajusta a altura da área do gráfico
    )
    # Exibe o gráfico no Streamlit
    st.plotly_chart(fig)

    # Analise do gráfico
    # Obs.: Para trocar de linha é necessário 02 espaços seguidos ao final da linha
    st.markdown('''<span style="color: white;">No gráfico acima estão indicados os 20 jogos com maior número de retornos, avaliaçôes feitas pelos usuários.  
                Este maior número de avaliações recebidas indica que os usuários destes jogos são mais engajados na comunidade.  
                Estes retornos podem ser bastante utéis aos desenvolvedores nos novos projetos.                                                                                    
                <br><br><br>''', unsafe_allow_html=True)

    # Gráfico de percentual de avaliações positivas comparado com as avaliações negativas
    #total_avaliacoes_geral = df_ordenado['Total Avaliacoes Jogo'].sum()
    total_avaliacoes = df_ordenado['Avaliacoes Positivas'] + df_ordenado['Avaliacoes Negativas']
    
    # Cria as colunas de percentuais
   # df_ordenado['Percentual Positivo Geral'] = (df_ordenado['Avaliacoes Positivas'] / total_avaliacoes_geral) * 100
    df_ordenado['Percentual Positivo'] = (df_ordenado['Avaliacoes Positivas'] / total_avaliacoes) * 100
   # df_ordenado['Percentual Negativo Geral'] = (df_ordenado['Avaliacoes Negativas'] / total_avaliacoes_geral) * 100
    df_ordenado['Percentual Negativo'] = (df_ordenado['Avaliacoes Negativas'] / total_avaliacoes) * 100
    
    # Ordenar
    top10 = df_ordenado.head(20)
    
    # Remover as colunas auxiliares desnecessárias
    top10 = top10.drop(columns=['ID Jogo', 'Avaliacoes Positivas', 'Avaliacoes Negativas', 'Total Avaliacoes Jogo'])
    
    # Criar o gráfico de barras empilhadas
    fig = px.bar(
        top10,
        x=['Percentual Positivo', 'Percentual Negativo'],
        y='Jogo', 
        title='TOP 20 - Avaliações Positivas x Negativas',
        labels={
            'Percentual Positivo': 'Percentual Positivo', 
            'Percentual Negativo': 'Percentual Negativo'
        },
        color_discrete_map={'Percentual Positivo': 'green', 'Percentual Negativo': 'red'},
        text_auto='.2f'  # Exibir valores nas barras com duas casas decimais
    )

    # Configurações do layout do gráfico
    fig.update_layout(
        title_x=0.5,  # Centraliza o título
        xaxis_title='',  # Remove o título do eixo X
        yaxis_title='Jogo',  # Título do eixo Y
        legend_title='',  # Título da legenda
        barmode='stack',  # Empilhar as barras
        height=600,  # Ajusta a altura da área do gráfico
        xaxis_tickangle=45,  # Rotaciona os rótulos do eixo X
        margin=dict(l=150, r=20, t=60, b=20),  # Ajuste das margens
        legend=dict(
            orientation="h",  # Coloca a legenda na horizontal
            y=-0.2,  # Posiciona a legenda abaixo do gráfico
            x=0.5,  # Centraliza a legenda horizontalmente
            xanchor='center',  # Centraliza o ponto de ancoragem da legenda
            yanchor='bottom'  # Ancorar a legenda na parte inferior
        )
    )

    # Alterar os itens da legenda
    fig.update_traces(
        name='% Positivo', selector=dict(name='Percentual Positivo'),
        texttemplate='%{x:.2f}%',  # Formatação de duas casas decimais com símbolo de %
    )
    fig.update_traces(
        name='% Negativo', selector=dict(name='Percentual Negativo'),
        texttemplate='%{x:.2f}%',  # Formatação de duas casas decimais com símbolo de %
    )

    # Exibir o gráfico no Streamlit
    st.plotly_chart(fig)
    
     # Analise do gráfico
    # Obs.: Para trocar de linha é necessário 02 espaços seguidos ao final da linha
    st.markdown('''<span style="color: white;">No gráfico acima estão indicados os percentuais de avaliação dos 20 jogos com maior número de retornos, avaliaçôes feitas pelos usuários.  
                Observa-se que o jogo PLAYERUNKNOWS BATTLEGROUNDS recebeu um elevado número de avaliações negativas (49,54%), indicando a necessidade de novo rumo no desenvolvimento do jogo.  
                Em contrapartida a jogos com altissimo número de avaliações positivas, como o THE WITCHER 3: WILD HUNT com 97,69% de avaliações positivas, indica que os desenvolvedores estão no caminho certo.
                ''', unsafe_allow_html=True)

# Importa os pacotes necessários
import streamlit as st
import datetime
import locale
from datetime import datetime

def app():
    
    # Adiciona o banner de imagem usando st.image
    st.image("Banner_steam.png", width=100, use_container_width=True)

    # Referenciando o arquivo styles.css bo streamlit
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

    st.caption(''':blue[Criado por Sabrina Costa França]''')

    # Usa o estilo personalizado para criar a linha separadora
    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

    st.markdown(''':red[**OBJETIVO:**]''')

    texto1 = '''<p style="color: white;text-align: justify;">Esta pesquisa traz uma análise do crescimento da demanda por jogos digitais,
        destacando a necessidade de desenvolver métodos mais eficazes para filtrar, processar e interpretar volume massivos 
        e grandes de dados. Esses dados derivam de várias fontes, como engajamento, padrões de compra e preferências de jogo, 
        com o objetivo de compreender as dinâmicas do mercado de jogos digitais.                                                                                    
        <br><br></p>'''
    st.markdown(texto1, unsafe_allow_html=True)

    # Usa o estilo personalizado para criar a linha separadora
    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

    st.markdown(''':red[**INTEGRANTES:**]''')
    
    texto2 = '''<p style="color: white;text-align: justify;">
        Brayan Luiz Sobral Santos<br>
        Talita de Jesus Santos<br>
        Thiago Alexandre de Almeida Andrade
        Sabrina Costa França<br>
        Saymon Santos Alves<br>                                                                             
        <br><br></p>'''
    st.markdown(texto2, unsafe_allow_html=True)
    
    # Usa o estilo personalizado para criar a linha separadora
    st.markdown('<div class="custom-divider" ></div>', unsafe_allow_html=True)

    st.markdown(''':red[**PROFESSOR RESPONSÁVEL:**]''')
    
    texto3 = '''<p style="color: white;text-align: justify;">
        Max Castor                                                                                    
        <br><br></p>'''
    st.markdown(texto3, unsafe_allow_html=True)
    
    # Define o locale para português (Brasil)
    # locale.setlocale(locale.LC_TIME, "pt_BR.utf8")  # Para sistemas Linux/Unix
    # locale.setlocale(locale.LC_TIME, "Portuguese_Brazil.1252")  # Para sistemas Windows

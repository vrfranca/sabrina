import streamlit as st

from streamlit_option_menu import option_menu
import os
from dotenv import load_dotenv
import Home, engajamento, popularidade, preco, segmentacao, temporal
from dados import _global_df  # Importando a variável global de outro módulo
#from funcoes import menu_lateral  # Importando a função menu_lateral

# Carrega o arquivo .env para obter as variáveis de ambiente, como a chave do Google Analytics (definida como analytics_tag).
load_dotenv()

# Define o título da página exibido no navegador.
st.set_page_config(
    page_title = "Analise de Dados com Python - Estácio SE", 
    page_icon = "Designer.png", 
    layout = "wide"
)

# Integra o Google Analytics ao aplicativo usando JavaScript. 
# Ele carrega dinamicamente o ID de rastreamento do Analytics através da variável de ambiente analytics_tag
st.markdown(
    """
        <!-- Global site tag (gtag.js) - Google Analytics -->
        <script async src=f"https://www.googletagmanager.com/gtag/js?id={os.getenv('analytics_tag')}"></script>
        <script>
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());
            gtag('config', os.getenv('analytics_tag'));
        </script>
    """, unsafe_allow_html = True)
print(os.getenv('analytics_tag'))

# Esta classe (class MultiApp) define uma estrutura para gerenciar várias páginas no aplicativo.
# __init__: Inicializa a lista de aplicativos.
# add_app: Método para adicionar uma página ao menu

class MultiApp:
    
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append(
            {
            "title": title,
            "function": func
            }
        )
       
# Este é o núcleo do aplicativo, responsável por exibir as páginas com base na seleção do usuário. 
# Cria um menu lateral usando o option_menu com diferentes opções: 'Home', 'Analise de Engajamento', 'Analise de Popularidade', 'Analise de Preço', 'Analise de Segmentação', 'Analise Temporal'.
# icons: Define ícones para cada página.
# styles: Personaliza o estilo do menu (cor de fundo, cor de ícones, etc.).
    def run(self):
        
        # Exibe o menu de navegação principal
        with st.sidebar:        
            app = option_menu(
                menu_title = 'Estudo Steam',
                options = ['Home', 'Analise de Engajamento', 'Analise de Popularidade', 'Analise de Preço', 'Analise de Segmentação', 'Analise Temporal'],
                # endereço onde por ver os icones disponiveis https://icons.getbootstrap.com/
                icons = ['house', 'chat-square-quote', 'people', 'coin', 'globe', 'grid', 'calendar4-week'],
                menu_icon = 'steam',
                default_index = 0,
                styles = {
                    "container": {"padding": "5!important", "background-color": 'white',}, 
                    "icon": {"color": "black", "font-size": "18px"}, 
                    "nav-link": {"color": "black", "font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#81D6EB"}, 
                    "nav-link-selected": {"color": "black", "background-color": "#E3D8D8"},
                    "menu-title": {"color": "black", "font-size": "20px"},
                    "menu-icon": {"color": "black", "font-size": "25px"},
                }
            )
        
        # Com base na opção selecionada pelo usuário, o código chama a função correspondente dos módulos:
        # 'Home', 'Analise de Engajamento', 'Analise de Popularidade', 'Analise de Preço', 'Analise de Segmentação' e 'Analise Temporal' para renderizar a página apropriada.
        if app == 'Home':
            Home.app()
        elif app == 'Analise de Engajamento':
            engajamento.app()
        elif app == 'Analise de Popularidade':
            popularidade.app()
        elif app == 'Analise de Preço':
            preco.app()
        elif app == 'Analise de Segmentação':
            segmentacao.app()
        elif app == 'Analise Temporal':
            temporal.app()
    
# A função run é chamada ao final para iniciar o aplicativo.            
app = MultiApp()
app.run()

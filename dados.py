# Importando as bibliotecas necessárias
import pandas as pd

### Carga e tratamento dos dados para uso nas analises - ETL ###

try:

    # Fazendo a leitura do arquivo CSV
    df = pd.read_csv("steam.csv", sep=",", encoding="utf-8", header=0)

    # Criando uma nova coluna para os totais de avaliações
    df['Total Avaliacoes Jogo'] = df['positive_ratings'] + df['negative_ratings']
    
    # Convertendo a coluna de datas para o tipo datetime
    df['release_date'] = pd.to_datetime(df['release_date'])
    
    # Criando uma coluna de Ano para analises temporais
    df['Ano'] = df['release_date'].dt.year


    df = df.drop(columns=['required_age'])

    # Renomeando colunas
    df = df.rename(columns={
        'appid': 'ID Jogo',
        'name': 'Jogo',
        'english': 'Em Inglês',
        'release_date': 'Data Lancamento',
        'developer': 'Desenvolvedor',
        'publisher': 'Editora',
        'platforms': 'Plataforma',
        'categories': 'Categorias',
        'genres': 'Generos',
        'steamspy_tags': 'Tags Steamspy',
        'achievements': 'Conquistas',
        'positive_ratings': 'Avaliacoes Positivas',
        'negative_ratings': 'Avaliacoes Negativas',
        'average_playtime': 'Media de Tempo de Jogo',
        'median_playtime': 'Mediana de Tempo de Jogo',
        'owners': 'Compradores',
        'price': 'Preco',
    })
    
    _global_df = df

except Exception as e:
    # Mensagem amigável para o usuário
    print("Ocorreu um erro inesperado durante a carga dos dados.\nContate o administrador do sistema.")
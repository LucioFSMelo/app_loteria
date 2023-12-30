import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from numpy import random
import math

#####################Lendo o dataset##########################################################################################
@st.cache_data
def geral_data():
  url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTGuaXTgVOy65DU9E_WBVqP-DGUQsf_ScQCGciWRvqNZn1oA8Eyla6-H5WNKz8U1g/pub?output=xlsx"
  dados = pd.read_excel(url)
  # Calculando a ocorrência de cada número
  numeros = pd.concat([dados['bola 1'], dados['bola 2'], dados['bola 3'], dados['bola 4'], 
                     dados['bola 5'], dados['bola 6']], ignore_index=True)
  # Calculando a ocorrência geral de cada número
  ocorrencias = numeros.value_counts().sort_index()
  # Criando um DataFrame com os números e suas ocorrências
  df_ocorrencias = pd.DataFrame({'Número': ocorrencias.index, 'Ocorrências': ocorrencias.values})
  df_ocorrencias = df_ocorrencias.reset_index(drop=True)
  return [dados, df_ocorrencias]


##################################Gerando as ocorrências dos dias 31/12#######################################################
def virada_data():
  #Fazendo a cópia do dataframe
  dados = geral_data()
  df = dados[0].copy()

  # Convertendo a coluna 'Data' para o tipo datetime
  df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y')

  # Filtrando os concursos com a data '31/12'
  df_selecionado = df.loc[df['Data'].dt.strftime('%d/%m') == '31/12']

  # Calculando a ocorrência de cada número
  numbers = pd.concat([df_selecionado['bola 1'], df_selecionado['bola 2'], df_selecionado['bola 3'], 
                      df_selecionado['bola 4'], df_selecionado['bola 5'], df_selecionado['bola 6']], ignore_index=True)

  # Calculando a ocorrência de cada número
  ocorrencias2 = numbers.value_counts().sort_values(ascending=False)
  df_ocorrencias2 = pd.DataFrame({'Número': ocorrencias2.index, 'Ocorrências': ocorrencias2.values})
  df_ocorrencias2 = df_ocorrencias2.reset_index(drop=True)
  return df_ocorrencias2.head(10)

#######################################Gerando o gráfico com o pltly-express#################################################
def grafico():
  ocorrencias2 = virada_data()
  # Criando um gráfico interativo com Plotly
  fig = px.bar(ocorrencias2.head(10), x='Número', y='Ocorrências', labels={'Ocorrências': 'Ocorrências'})
  fig.update_layout(
    {
        "paper_bgcolor": "rgba(0, 0, 0, 0)",
        "plot_bgcolor": "rgba(0, 0, 0, 0)",
    }
)
  return fig

#st.plotly_chart(fig)
############################################Seção 2##################################################################
################################ Função para sortear os números #####################################################
def sorteio_number(qt_num):
  lista_numbers = np.arange(1, 61)
  n = 0
  sorteados = []
  num_sorteado = 0
  while n < qt_num:
    number = random.choice(lista_numbers)
    if number not in sorteados:
      num_sorteado = number
      sorteados.append(num_sorteado)
    else:
      while number in sorteados:
        number = random.choice(lista_numbers)
      num_sorteado = number
      sorteados.append(num_sorteado)
    n +=1
  return sorteados

# Função para cria a quantidade de jogos
# Função para criar a quantidade de apostas
def cria_jogos(qt_jogos, numeros):
  apostas = []
  n = 0
  while n < qt_jogos:
    jogo = sorteio_number(numeros)
    apostas.append(jogo)
    n+=1
  return apostas

def jogo():
    st.title("Ocorrência dos números da Mega Sena")
    st.subheader("Clique no botão abaixo para exibir as ocorrências de todos os números da Mega sena")
    ocorrencia1 = geral_data()
    coluna1, coluna2 = st.columns(2)
    exibir = coluna1.button('Exibir os 20 ultimos jogos')
    exibir2 = coluna2.button('Ocorrência Geral dos números')
    if exibir:
        st.dataframe(ocorrencia1[0].head(20))
        st.markdown(':blue[Fonte: As Loterias - www.asloterias.com.br - Todos Resultados da Mega Sena]')

    if exibir2:
        st.dataframe(ocorrencia1[1])

    st.title("Top 10 Mega da Virada")
    col1, col2 = st.columns(2)

    with col1:
      st.write('## Os dez números mais sorteados')
      virada = virada_data()
      st.dataframe(virada)

    with col2:
      st.write('## Gráfico dos Top 10 - Mega Sena')
      virada2 = grafico()
      st.plotly_chart(virada2, clear_figure=True)

    st.title("Gerador de Números para Mega Sena")

    qt_numeros = st.number_input('Informe a quantidade de numeros a marcar no bilhete: ', format="%d", key='numeros')
    qt_jogos = st.number_input('Informe a quantidade de jogos a serem feitos: ', format="%d", key='jogos')
    gera = st.button("Gerar Números")
    if gera:
      aposta = cria_jogos(qt_jogos, qt_numeros)
      n = int(qt_numeros + 1)
      colunas = ["Coluna %d" % i for i in range(1, n)]
      df = pd.DataFrame(aposta, columns= colunas)
      st.table(df)


if __name__=='__main__':
    jogo()
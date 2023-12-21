import streamlit as st
import numpy as np
import math


#C = n!/(p!*(n-p)!)
# Probabilidade de acetar a mega sena jogando os seis números
def combinac_6():
    bolas = 60
    escolha = 6
    quanti_bolas = math.factorial(bolas)
    elementos_PP = math.factorial(escolha)
    param_Sena = math.factorial(bolas - escolha)
    combinacao_Sena = quanti_bolas // (elementos_PP * param_Sena)
    return combinacao_Sena

# Quantidade de combinações com mais de 6 números
def quant_combinc():
    fixo = 6
    escolha = st.number_input("Informe a quantidade de dezenas para calcular as combinações dos bolhetes: ")
    tamanho_escolha = math.factorial(escolha)
    elementos_PP_tec = math.factorial(fixo)
    param_Tec = math.factorial(escolha - fixo)
    combinacao_Tec = tamanho_escolha // (elementos_PP_tec * param_Tec)
    return [combinacao_Tec, escolha]

# Lembrar de colocar depois a definição de análise combinatória
def home():
    st.title("Um Pouco de Análise Combinatória")
    st.markdown("""Espaço para o conteúdo do site""")
    preco = st.number_input("Informe o preço da aposta simples: ")
    combinacao_sena = combinac_6()
    quantidade_comb = quant_combinc()
    print('*'*60)
    print('')
    print(f'A Probabilidade de acertar na Mega Sena é {combinacao_sena}')
    print('')
    print(f'O valor a pagar por um jogo de 6 dezenas é {preco}')
    print('')
    print(f'Quantidades de combinações em um bilhete de {quantidade_comb[1]} números é {qquantidade_comb[0]} combinações.')
    print('')
    print(f'O valor a pagar por um jogo de {quantidade_comb[1]} dezenas é {preco*quantidade_comb[0]}')
    print('')
    print(f'A Probabilidade de acertar na Mega Sena com um jogo de {quantidade_comb[1]} dezenas é {quantidade_comb[0]}')
    print('--*--'*12)
    print('*'*60)

if __name__=="__main__":
    home()

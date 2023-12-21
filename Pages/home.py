import streamlit as st
import numpy as np
import math


st.title("Um Pouco de Análise Combinatória")






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
    escolha = int(input("Informe a quantidade de bolas para calcular a quantidade de combinações: "))
    tamanho_escolha = math.factorial(escolha)
    elementos_PP_tec = math.factorial(fixo)
    param_Tec = math.factorial(escolha - fixo)
    combinacao_Tec = tamanho_escolha // (elementos_PP_tec * param_Tec)
    return combinacao_Tec

# Quantidades de combinações obtidas pela lista ordem, tomados 7 a 7. 11/12/2022
quant_numeros = tamanho_ordem
p_elementos = int(input('Quatidade de números para prencher no bilhete: '))
elementos = math.factorial(quant_numeros)
opcoes = math.factorial(p_elementos)
param = math.factorial(quant_numeros - p_elementos)
combinacao = elementos // (opcoes * param)

# Quantidade de combinações formadas em um bilhete com 7 números
numeros_bilhete = p_elementos
quant_numeros_bilhete = math.factorial(numeros_bilhete)
param_bilhete = math.factorial(numeros_bilhete - escolha)
combinacao_bilhete = quant_numeros_bilhete // (elementos_PP * param_bilhete)


print('*'*60)
print('')
print(f'A Probabilidade de acertar na Mega Sena é {combinacao_Sena}')
print('')
print(f'A Probabilidade reduzida de acertar na Mega Sena é {combinacao_Tec}')
print('--*--'*12)

print(f'A quantidade de combinções {p_elementos} a {p_elementos} da lista ordem é {combinacao} combinações.')
print('')
print(f'Quantidades de combinações em um bilhete de {p_elementos} números é {combinacao_bilhete} combinações.')
print('')
print('*'*60)

import streamlit as st
import numpy as np
import math


# Função para o conteúdo
def conteudo():
    st.title("Primeiro Concurso da Mega Sena")
    st.subheader("""O primeiro concurso da Mega-Sena teve seus números sorteados no dia **11 de março de 1996**, em Brasília.  \
                A Mega-Sena é uma loteria criada pela Caixa Econômica Federal para substituir uma antiga loteria, a Sena,  \
                com a expectativa de entregar *"prêmios gigantescos"*. Além dos prêmios, dentre as mudanças estavam o maior  \
                número de dezenas no volante e a maior dificuldade de acertar os números. **Ninguém acertou os seis números**  \
                sorteados no primeiro concurso, acumulando mais de **um milhão de reais** para o segundo, mas houve ganhadores  \
                de quina e quadra.""")
    st.markdown("Fonte: https://pt.wikipedia.org/wiki/Primeiro_concurso_da_Mega-Sena")

    st.title("Um Pouco de Análise Combinatória")
    st.subheader("""A Análise Combinatória é um ramo da matemática associado ao estudo das regras de contagem. Se você deseja  \
                 fazer análises de possibilidades (probabilidades) e análises de possíveis combinações entre um conjunto de  \
                 elementos, a análise combinatória vai lhe fornecer métodos e técnicas que lhe proporcionarão uma maior precisão  \
                 nos seus calculos matemáticos.""")
    
    st.title("Combinação Simples")
    st.subheader("""Usando a combinação simples, um dos métodos da análise combinatória para resolução de problemas, podemos  \
                 encontar a quantidade total de combinações da Mega Sena e saber quantas combinações podemos ter um um bilhete  \
                 de jogo seguido as regras da loteria, onde um jogo pode ter de 6 a 20 números em um único bilhete e com isso o  \
                 valor desse jogo dependerá da quantidade de combinações dos números marcados.""")
    

    st.markdown(":blue[**Veja nesse exemplo a quantidade de combinações e o valor a pagar em um jogo, de acordo com a quantidade de dezenas do bilhete.**]")
    st.markdown(":blue[**Use o controle deslizante para interagir com a página**]")
    numbers = st.slider('Informe a quantidade de dezenas', 6, 20)
    #C = n!/(p!*(n-p)!)
    bolas = 60
    fixo = 6
    preco = 5
    quanti_total_bolas = math.factorial(bolas)
    elementos_PP = math.factorial(fixo)
    param_total_Sena = math.factorial(bolas - fixo)
    combinacao_total_sena = quanti_total_bolas // (elementos_PP * param_total_Sena)

    quanti_bolas = math.factorial(numbers)
    param_Sena = math.factorial(numbers - fixo)
    combinacao_sena = quanti_bolas // (elementos_PP * param_Sena)
    preco_total = preco * combinacao_sena

    chances = combinacao_total_sena // combinacao_sena

    if numbers == 6:
        st.markdown(f':blue[**Um bilhete com {numbers} dezenas, tem uma única combinação e custa R$ 5,00.**]')
        st.markdown(f':blue[**A probabilidade de acertar na Mega Sena com {numbers} dezenas é de {combinacao_sena} chance em {combinacao_total_sena}**]')
    else:
        st.markdown(f':blue[**Um bilhete com {numbers} dezenas, tem {combinacao_sena} combinações e custa R$ {preco_total},00.**]')
        st.markdown(f':blue[**A probabilidade de acertar na Mega Sena com {numbers} dezenas é de 1 chance em {chances}**]')


    

if __name__ == "__main__":
    conteudo()
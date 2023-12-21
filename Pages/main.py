import streamlit as st
from home import home


st.title("Mega Sena - Loteria")
st.markdown("""Este aplicativo não é uma garantia de que você ganhará no jogo.  
            Com este aviso eu me insento de qualquer eventual perda sua física ou financeira.  
            Este aplicativo é uma forma divertida e simplificada para os amantes de jogos,  
            se você não sabe quais dezenas jogar, este gerador de dezenas é uma boa escolha.  
            """)

pg_home = st.sidebar.button("Home")
if pg_home:
    home()
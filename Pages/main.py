import streamlit as st
from conteudo import conteudo
from mega_sena import jogo

# Configuração do layout
st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Adiciona um estilo personalizado usando CSS embutido
st.markdown(
    """
    <style>
        body {
            background-color: #87CEEB; /* Azul céu */

            <footer style="text-align: center; margin-top: 50px;">
                <p>© Lucio Flavio Santos.</p>
            </footer>
        }
        .main {
            background-color: #87CEEB; /* Fundo para o conteúdo principal */
            padding: 10px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1); /* Sombra suave */
        }
           .corner-buttons {
            position: fixed;
            top: 10px;
            right: 10px;
            display: flex;
            flex-direction: row-reverse;
        }

        .corner-buttons button {
            margin-left: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)


# Conteúdo do footer em HTML
footer_html = """
    <footer style="text-align: center; margin-top: 50px;">
        <p>© Seu Nome.</p>
    </footer>
"""

# Renderizar o HTML usando st.markdown
st.markdown(footer_html, unsafe_allow_html=True)


with open("css/styles.css") as f:
  st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Barra de menu

paginas = st.sidebar.selectbox("Escolha uma página", ("Mega Sena", "Curiosidades"))
# Lógica para mostrar diferentes conteúdos com base nos botões clicados
if paginas == 'Mega Sena':
    jogo()
if paginas == 'Curiosidades':
    conteudo()
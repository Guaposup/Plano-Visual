import streamlit as st
from PIL import Image
import base64

# Configuração da página
st.set_page_config(page_title="Centraliza", page_icon="🔗", layout="centered")

# Usuários cadastrados
usuarios = {
    "admin": {"senha": "1234", "perfil": "Administrador"},
    "Igor": {"senha": "senha123", "perfil": "Usuário"},
}

# Função para converter imagem local em base64
def get_base64_image(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

background_base64 = get_base64_image("logo.jpeg")

# Estilos CSS
st.markdown(f"""
<style>
    .stApp {{
        background: url("data:image/jpg;base64,{background_base64}") no-repeat center center fixed;
        background-size: cover;
    }}
    .main {{
        background-color: rgba(0, 0, 0, 0.75);
        padding: 2rem 1.5rem;
        border-radius: 14px;
        max-width: 320px;
        min-width: 250px;
        margin: 5rem auto;
        box-shadow: 0 4px 25px rgba(0, 0, 0, 0.7);
        text-align: center;
    }}
    a.link-button {{
        display: block;
        background-color: #111111;
        color: white !important;
        font-size: 15px;
        font-weight: 500;
        text-align: center;
        padding: 10px 0;
        margin: 8px auto;
        border-radius: 12px;
        width: 70%;
        text-decoration: none !important;
        transition: background-color 0.25s ease, transform 0.2s ease;
        user-select: none;
        box-shadow: 0 2px 6px rgba(0,0,0,0.5);
    }}
    a.link-button:hover {{
        background-color: #333333;
        transform: scale(1.03);
        box-shadow: 0 3px 12px rgba(0,0,0,0.7);
    }}
    h1 {{
        color: white;
        font-weight: 600;
        font-size: 1.8rem;
        user-select: none;
        text-align: center;
    }}
    .perfil {{
        color: #cccccc;
        font-size: 0.85rem;
        margin-top: -0.8rem;
        margin-bottom: 1.5rem;
        text-align: center;
    }}
    div.stTextInput > div, div.stTextInput {{
        max-width: 300px;
        margin: 0 auto;
    }}
    input[type="text"], input[type="password"] {{
        width: 100% !important;
        border-radius: 12px;
        padding: 6px 10px;
        font-size: 15px;
        box-sizing: border-box;
    }}
    div.stButton {{
        display: flex;
        justify-content: center;
        margin-top: 1rem;
    }}
    div.stButton > button {{
        width: 70%;
        max-width: 300px;
        border-radius: 12px;
        background-color: #111111;
        color: white;
        font-size: 15px;
        font-weight: 500;
        padding: 10px 0;
        cursor: pointer;
        border: none;
        box-shadow: 0 2px 6px rgba(0,0,0,0.5);
        transition: background-color 0.25s ease, transform 0.2s ease;
    }}
    div.stButton > button:hover {{
        background-color: #333333;
        transform: scale(1.03);
        box-shadow: 0 3px 12px rgba(0,0,0,0.7);
    }}
</style>
""", unsafe_allow_html=True)

# Sessão
if "logado" not in st.session_state:
    st.session_state.logado = False
    st.session_state.usuario = ""
    st.session_state.perfil = ""
    st.session_state.erro_login = False

# Tela de login
if not st.session_state.logado:
    
    st.markdown("<h1>Login</h1>", unsafe_allow_html=True)

    with st.form("login_form"):
        usuario = st.text_input("Usuário")
        senha = st.text_input("Senha", type="password")
        st.markdown('<div class="login-button-container">', unsafe_allow_html=True)
        login = st.form_submit_button("Entrar")
        st.markdown('</div>', unsafe_allow_html=True)


    if login:
        if usuario in usuarios and senha == usuarios[usuario]["senha"]:
            st.session_state.logado = True
            st.session_state.usuario = usuario
            st.session_state.perfil = usuarios[usuario]["perfil"]
            st.session_state.erro_login = False
            st.rerun()
        else:
            st.session_state.erro_login = True

    if st.session_state.erro_login:
        st.error("Usuário ou senha inválidos.")

    st.markdown('</div>', unsafe_allow_html=True)

# Tela principal após login
else:
    
    st.markdown('<h1>Centraliza</h1>', unsafe_allow_html=True)
    st.markdown(f'<div class="perfil">Bem-vindo, {st.session_state.usuario} | Perfil: {st.session_state.perfil}</div>', unsafe_allow_html=True)

    # Links disponíveis
    links = {
        "Solicitação de Proposta de Preço": "https://docs.google.com/forms/d/e/1FAIpQLSdLmjOhqaQCaKH9AZHBRJtyh0T6C0i46cWFc6_vYsqIuiAHJw/viewform?usp=dialog",
        "Solicitação de Uniformes": "https://docs.google.com/forms/d/e/1FAIpQLSc_QH0qI4Pcok0Uj41dllMlf7KWBNmUe0l2ZETevZaL1jRJSw/viewform",
        "✉ WebMail": "https://webmail-seguro.com.br/?_task=mail",
        "Controle de Validades": "https://docs.google.com/spreadsheets/d/1fTwGD1XpgB357RA75vgtKcv1rRiZ-wpjf7MtCMmidaA/edit?gid=336881860#gid=336881860"
    }

    for nome, url in links.items():
        st.markdown(f'<a class="link-button" href="{url}" target="_blank">{nome}</a>', unsafe_allow_html=True)

    if st.button("Sair"):
        st.session_state.logado = False
        st.session_state.usuario = ""
        st.session_state.perfil = ""
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

import streamlit as st
from agentes import AgenteAVS

st.set_page_config(page_title="AVS – Aroma Viral System", page_icon="🧪", layout="wide")

# Estilo para os botões e visual
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 20px; height: 3em; background-color: #FF4B4B; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🧪 AVS – Aroma Viral System")
st.subheader("Fábrica de Conteúdo do Almir")

api_key = st.secrets["GROQ_API_KEY"]
perfume = st.text_input("Qual perfume vamos transformar em viral hoje?", placeholder="Ex: Fakhar Black")

if st.button("🚀 GERAR CAMPANHA COMPLETA"):
    if not perfume:
        st.warning("Digite o nome do perfume!")
    else:
        avs = AgenteAVS(api_key)
        with st.status("Agentes trabalhando...", expanded=True) as status:
            res = avs.executar_flow(perfume)
            status.update(label="Campanha Gerada!", state="complete")
        
        # --- ÁREA DE CÓPIA RÁPIDA ---
        st.divider()
        st.subheader("📋 COPIAR TUDO (Clique no ícone à direita)")
        texto_para_copiar = f"CAMPANHA: {perfume}\n\n" + "\n\n".join(res)
        st.code(texto_para_copiar, language="text") # Este componente tem o botão de copiar nativo!

        # --- VISUALIZAÇÃO EM COLUNAS ---
        col1, col2 = st.columns(2)
        with col1:
            with st.expander("🎯 Estratégia e Ganchos", expanded=True):
                st.markdown(res[0])
                st.markdown(res[1])
        with col2:
            with st.expander("🎬 Criativos e Legendas", expanded=True):
                st.markdown(res[2])
                st.markdown(res[3])
                st.markdown(res[4])

st.sidebar.markdown("---")
st.sidebar.write("Sistema AVS v2.0 - Almir")

import streamlit as st
from agentes import AgenteAVS
import os

# Configuração da página
st.set_page_config(page_title="AVS – Aroma Viral System", page_icon="🧪", layout="wide")

st.title("🧪 AVS – Aroma Viral System")
st.subheader("O Sistema do Almir - Fábrica de Conteúdo 24h")

# Tenta pegar a chave dos Secrets do Streamlit
try:
    api_key = st.secrets["GROQ_API_KEY"]
except:
    st.error("ERRO: A chave GROQ_API_KEY não foi encontrada nos Secrets!")
    st.stop()

perfume = st.text_input("Qual perfume vamos transformar em viral hoje?", placeholder="Ex: Fakhar Black, Sauvage, etc.")

if st.button("🚀 GERAR CAMPANHA COMPLETA"):
    if not perfume:
        st.warning("Por favor, digite o nome de um perfume!")
    else:
        avs = AgenteAVS(api_key)
        with st.status("Agentes trabalhando na sua campanha...", expanded=True) as status:
            res = avs.executar_fluxo(perfume)
            status.update(label="Campanha Gerada com Sucesso!", state="complete")
        
        # Exibição organizada
        st.divider()
        c1, c2 = st.columns(2)
        with c1:
            st.info("📊 ESTRATÉGIA & GANCHOS")
            st.markdown(res[0]) # CEO
            st.markdown(res[1]) # Caçador
        with c2:
            st.success("🎬 ROTEIRO & PROMPTS")
            st.markdown(res[2]) # Engenheiro
            st.markdown(res[3]) # Analista Viral
            st.write("---")
            st.markdown(res[4]) # Algoritmo

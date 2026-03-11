import streamlit as st
from agentes import AgenteAVS

st.set_page_config(page_title="AVS – Aroma Viral System", page_icon="🧪", layout="wide")

st.title("🧪 AVS – Aroma Viral System")
st.subheader("Fábrica de Conteúdo do Almir")

# Verifica se a chave existe nos Secrets
if "GROQ_API_KEY" not in st.secrets:
    st.error("Configure a chave GROQ_API_KEY nos Secrets do Streamlit!")
    st.stop()

api_key = st.secrets["GROQ_API_KEY"]

perfume = st.text_input("Qual perfume vamos transformar em viral hoje?", placeholder="Ex: Fakhar Black")

if st.button("🚀 GERAR CAMPANHA COMPLETA"):
    if not perfume:
        st.warning("Por favor, digite o nome de um perfume!")
    else:
        try:
            avs = AgenteAVS(api_key)
            with st.status("Agentes trabalhando...", expanded=True) as status:
                res = avs.executar_fluxo(perfume)
                status.update(label="Campanha Gerada!", state="complete")
            
            st.divider()
            
            # Caixa de Cópia com botão nativo
            st.subheader("📋 COPIAR TUDO")
            texto_final = f"PRODUTO: {perfume}\n\n" + "\n\n".join(res)
            st.code(texto_final, language="text")

            # Exibição organizada
            c1, c2 = st.columns(2)
            with c1:
                st.info("🎯 Estratégia")
                st.markdown(res[0])
                st.markdown(res[1])
            with c2:
                st.success("🎬 Criativos")
                st.markdown(res[2])
                st.markdown(res[3])
                st.markdown(res[4])
        except Exception as e:
            st.error(f"Ocorreu um erro inesperado: {e}")

st.sidebar.write("AVS v2.2 - Estável")

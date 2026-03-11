import streamlit as st
from agentes import AgenteAVS

st.set_page_config(page_title="AVS – Aroma Viral System", page_icon="🧪", layout="wide")

st.title("🧪 AVS – Aroma Viral System")
st.subheader("Fábrica de Conteúdo do Almir")

if "GROQ_API_KEY" not in st.secrets:
    st.error("Configure a chave nos Secrets!")
    st.stop()

api_key = st.secrets["GROQ_API_KEY"]
perfume = st.text_input("Qual perfume vamos transformar em viral hoje?")

if st.button("🚀 GERAR CAMPANHA COMPLETA"):
    if not perfume:
        st.warning("Digite o nome do perfume!")
    else:
        avs = AgenteAVS(api_key)
        with st.status("Agentes trabalhando...", expanded=True) as status:
            # Chama a função correta: executar_fluxo
            res = avs.executar_fluxo(perfume)
            status.update(label="Campanha Gerada com Sucesso!", state="complete")
        
        st.divider()
        st.subheader("📋 COPIAR CONTEÚDO")
        texto_final = f"CAMPANHA: {perfume}\n\n" + "\n\n".join(res)
        
        # Este bloco st.code gera o botão de copiar automaticamente no canto superior direito
        st.code(texto_final, language="text")

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

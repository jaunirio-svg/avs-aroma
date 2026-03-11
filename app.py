import streamlit as st
from agentes import AgenteAVS

st.set_page_config(page_title="AVS – Sistema Autônomo de Luxo", page_icon="🧪", layout="wide")

st.title("🧪 AVS – Sistema Autônomo de Luxo")
st.subheader("Fábrica de Conteúdo do Almir - Inteligência Multi-Produto")

if "GROQ_API_KEY" not in st.secrets:
    st.error("Erro: Configure a GROQ_API_KEY nos Secrets!")
    st.stop()

api_key = st.secrets["GROQ_API_KEY"]
item = st.text_input("Qual produto vamos transformar em desejo hoje?", placeholder="Ex: Club de Nuit, Rolex, iPhone...")

if st.button("🚀 GERAR ESTRATÉGIA COMPLETA"):
    if not item:
        st.warning("Por favor, digite o nome de um produto!")
    else:
        avs = AgenteAVS(api_key)
        with st.status(f"Analisando '{item}'...", expanded=True) as status:
            res = avs.executar_fluxo(item)
            status.update(label=f"Campanha para {item} Concluída!", state="complete")
        
        st.divider()
        st.subheader("📋 ÁREA DE TRANSFERÊNCIA (Copiar Tudo)")
        texto_final = f"PRODUTO ANALISADO: {item}\n\n" + "\n\n".join(res)
        st.code(texto_final, language="text")

        st.subheader(f"📑 INTELIGÊNCIA DE MERCADO: {item}")
        
        with st.expander("👑 1. POSICIONAMENTO E DETALHES TÉCNICOS", expanded=True):
            st.write(res[0])
        with st.expander("🎬 2. ESTRATÉGIA DE VIRALIZAÇÃO", expanded=True):
            st.write(res[1])
            st.divider()
            st.write(res[3])
        with st.expander("📸 3. PROMPTS VISUAIS (Foco no Design)", expanded=False):
            st.write(res[2])
        with st.expander("📱 4. MARKETING E TAGS", expanded=False):
            st.write(res[4])

st.sidebar.info("v3.0 - Reconhecimento Automático Ativado.")
            st.markdown(res[1])
        with c2:
            st.success("🎬 Criativos")
            st.markdown(res[2])
            st.markdown(res[3])
            st.markdown(res[4])

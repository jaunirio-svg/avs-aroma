import streamlit as st
from agentes import AgenteAVS

st.set_page_config(page_title="AVS – Sistema Autônomo de Luxo", page_icon="🧪", layout="wide")

st.title("🧪 AVS – Sistema Autônomo de Luxo")
st.subheader("Inteligência Multi-Produto do Almir")

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
        
        exp1 = st.expander("👑 1. POSICIONAMENTO E DETALHES TÉCNICOS", expanded=True)
        exp1.write(res[0])
            
        exp2 = st.expander("🎬 2. ESTRATÉGIA DE VIRALIZAÇÃO", expanded=True)
        exp2.write(res[1])
        exp2.divider()
        exp2.write(res[3])
            
        exp3 = st.expander("📸 3. PROMPTS VISUAIS (Foco no Design)", expanded=False)
        exp3.write(res[2])
            
        exp4 = st.expander("📱 4. MARKETING E TAGS", expanded=False)
        exp4.write(res[4])

st.sidebar.info("v3.0 - Reconhecimento Automático Ativado.")

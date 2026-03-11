import streamlit as st
from agentes import AgenteAVS

st.set_page_config(page_title="AVS – Autonomia de Luxo", page_icon="💎", layout="wide")

# Estilização para um visual mais limpo
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; background-color: #d4af37; color: white; border-radius: 5px; }
    </style>
    """, unsafe_allow_html=True)

st.title("💎 AVS – Inteligência Autônoma de Luxo")
st.subheader("Plataforma Multi-Produto do Almir")

if "GROQ_API_KEY" not in st.secrets:
    st.error("Erro: Configure a API Key nos Secrets!")
    st.stop()

api_key = st.secrets["GROQ_API_KEY"]
item = st.text_input("Qual item de luxo vamos analisar?", placeholder="Ex: Asad, Rolex, Porsche, iPhone 15 Pro...")

if st.button("🚀 GERAR ESTRATÉGIA"):
    if not item:
        st.warning("Digite o nome de um produto.")
    else:
        avs = AgenteAVS(api_key)
        with st.status(f"Mapeando DNA de '{item}'...", expanded=True) as status:
            res = avs.executar_fluxo(item)
            status.update(label="Análise Concluída!", state="complete")
        
        st.divider()
        
        # Área de Copiar
        st.subheader("📋 Script Completo")
        st.code(f"PRODUTO: {item}\n\n" + "\n\n".join(res))

        # Visualização por Abas para ficar mais organizado
        tab1, tab2, tab3, tab4 = st.tabs(["👑 Estratégia", "📱 Viral", "📸 Visual", "✍️ Marketing"])
        
        with tab1:
            st.markdown(res[0])
        with tab2:
            st.markdown(res[1])
            st.divider()
            st.markdown(res[3])
        with tab3:
            st.markdown(res[2])
        with tab4:
            st.markdown(res[4])

st.sidebar.markdown("---")
st.sidebar.info("v4.0 - Filtro de Categoria Inteligente Ativado.")

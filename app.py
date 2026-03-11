import streamlit as st
from agentes import AgenteAVS

st.set_page_config(page_title="AVS – Aroma Viral System", page_icon="🧪", layout="wide")

st.title("🧪 AVS – Aroma Viral System")
st.subheader("Fábrica de Conteúdo do Almir")

# Puxa a chave dos Secrets
try:
    api_key = st.secrets["GROQ_API_KEY"]
except:
    st.error("Configure a GROQ_API_KEY nos Secrets do Streamlit!")
    st.stop()

perfume = st.text_input("Qual perfume vamos transformar em viral hoje?", placeholder="Ex: Fakhar Black")

if st.button("🚀 GERAR CAMPANHA COMPLETA"):
    if not perfume:
        st.warning("Digite o nome do perfume!")
    else:
        avs = AgenteAVS(api_key)
        with st.status("Agentes trabalhando na sua estratégia...", expanded=True) as status:
            # CORREÇÃO AQUI: o nome da função deve ser executar_fluxo
            res = avs.executar_fluxo(perfume)
            status.update(label="Campanha Gerada!", state="complete")
        
        # --- ÁREA DE CÓPIA RÁPIDA ---
        st.divider()
        st.subheader("📋 COPIAR CONTEÚDO (Clique no botão à direita da caixa cinza)")
        
        texto_completo = f"CAMPANHA: {perfume}\n\n"
        texto_completo += f"1. ESTRATÉGIA:\n{res[0]}\n\n"
        texto_completo += f"2. GANCHOS:\n{res[1]}\n\n"
        texto_completo += f"3. IMAGENS:\n{res[2]}\n\n"
        texto_completo += f"4. ROTEIROS:\n{res[3]}\n\n"
        texto_completo += f"5. LEGENDAS:\n{res[4]}"

        # O componente st.code já vem com o botão de cópia automática no Streamlit
        st.code(texto_completo, language="text")

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
st.sidebar.write("AVS v2.1 - Modo Luxo Ativado")

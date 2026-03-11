import streamlit as st
from agentes import AgenteAVS

st.set_page_config(page_title="AVS – Aroma Viral System", page_icon="🧪", layout="wide")

st.title("🧪 AVS – Aroma Viral System")
st.subheader("O Sistema do Almir - Fábrica de Conteúdo 24h")

api_key = st.secrets["GROQ_API_KEY"]

perfume = st.text_input("Qual perfume vamos transformar em viral hoje?", placeholder="Ex: Fakhar Black")

if st.button("🚀 GERAR CAMPANHA COMPLETA"):
    if not perfume:
        st.warning("Digite o nome de um perfume!")
    else:
        avs = AgenteAVS(api_key)
        with st.status("Agentes trabalhando...", expanded=True) as status:
            res = avs.executar_fluxo(perfume)
            status.update(label="Campanha Gerada!", state="complete")
        
        # Criamos um texto único com tudo para facilitar a cópia
        texto_completo = f"CAMPANHA: {perfume}\n\n" + "\n\n".join(res)
        
        st.divider()
        
        # NOVO: Botão para copiar o conteúdo inteiro de uma vez
        st.subheader("📋 Copie o Conteúdo Abaixo")
        st.text_area("Clique no ícone no canto superior direito desta caixa para copiar tudo:", 
                     value=texto_completo, height=300)

        c1, c2 = st.columns(2)
        with c1:
            st.info("📊 ESTRATÉGIA")
            st.markdown(res[0])
            st.markdown(res[1])
        with c2:
            st.success("🎬 CRIATIVOS")
            st.markdown(res[2])
            st.markdown(res[3])
            st.markdown(res[4])

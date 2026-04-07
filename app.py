import streamlit as st

# Configuração de Guerra: Foco Total no Dinheiro
st.set_page_config(page_title="Alerta de Lucro", page_icon="💰")

# 1. O IMPACTO (O que ele sente em 1 segundo)
st.markdown("<h3 style='text-align: center; color: gray;'>PREJUÍZO DETECTADO (PRÓXIMOS 30 DIAS)</h3>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: red; font-size: 50px;'>12.450,00 MT</h1>", unsafe_allow_html=True)

st.divider()

# 2. A PROVA (O que ele perde agora)
st.subheader("Itens Críticos:")
col1, col2 = st.columns([2, 1])
with col1:
    st.write("🔴 **Coartem (12 dias restantes)**")
    st.write("🔴 **Amoxicilina (19 dias restantes)**")
with col2:
    st.write("**5.400 MT**")
    st.write("**7.050 MT**")

st.divider()

# 3. A DECISÃO (Ação Imediata)
if st.button('🛡️ ESTANCAR ESTA PERDA AGORA', use_container_width=True):
    st.success("Relatório de Ação enviado para o WhatsApp do Gestor!")
    st.balloons() # Um pequeno toque de 'vitória' ao resolver o problema

st.caption("Baseado em stock típico de farmácias em Tete.")


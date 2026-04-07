import streamlit as st

# Design de "Urgência Financeira"
st.set_page_config(page_title="Alerta de Prejuízo", page_icon="⚠️")

# Título de Diagnóstico
st.markdown("<h4 style='text-align: center; color: #666;'>DIAGNÓSTICO DE STOCK: TETE</h4>", unsafe_allow_html=True)

# O NÚMERO QUE VENDE
st.markdown("<h1 style='text-align: center; color: #E74C3C; font-size: 45px;'>12.450,00 MT</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-weight: bold;'>PREJUÍZO EVITÁVEL (PRÓXIMOS 30 DIAS)</p>", unsafe_allow_html=True)

st.divider()

# PROVA REAL
st.write("### Itens em Risco Imediato:")
st.error("🔴 **Coartem 20/120** (Vence em 12 dias) -> **5.400 MT**")
st.error("🔴 **Amoxicilina 500mg** (Vence em 19 dias) -> **7.050 MT**")

st.divider()

# AÇÃO ÚNICA
if st.button('🛡️ ESTANCAR ESTA PERDA AGORA', use_container_width=True):
    st.success("Relatório de mitigação enviado ao sistema!")
    st.info("A aguardar integração com o inventário da farmácia...")

st.caption("Análise baseada em padrões de perda de farmácias locais.")

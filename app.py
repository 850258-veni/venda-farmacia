import streamlit as st

st.set_page_config(page_title="Recuperador de Lucro", page_icon="💰")

# ------------------ ESTADO ------------------
if "itens" not in st.session_state:
    st.session_state.itens = []

# ------------------ TÍTULO ------------------
st.markdown("## ⚡ DIAGNÓSTICO FINANCEIRO (60s)")

# ------------------ MODO RÁPIDO ------------------
with st.container():
    st.markdown("### 📊 Impacto Imediato")

    valor_estoque = st.number_input("Valor total em stock (MT)", min_value=1000, value=100000, step=5000)
    percentual_risco = st.slider("% em risco (estimado)", 1, 50, 10)

    prejuizo_estimado = valor_estoque * (percentual_risco / 100)

    st.markdown(f"""
    <div style="background-color:#ff4b4b;padding:20px;border-radius:10px">
        <h3 style="color:white;text-align:center;">VEREDITO FINANCEIRO</h3>
        <h1 style="color:white;text-align:center;">{prejuizo_estimado:,.2f} MT EM RISCO</h1>
        <p style="color:white;text-align:center;">Baseado em estimativa de {percentual_risco}% do stock.</p>
    </div>
    """, unsafe_allow_html=True)

# ------------------ PROVA REAL ------------------
st.markdown("### 🔍 Prova Real (1 Produto)")

col1, col2, col3 = st.columns(3)

with col1:
    nome = st.text_input("Medicamento")

with col2:
    dias = st.number_input("Dias para vencer", min_value=1, value=15)

with col3:
    valor = st.number_input("Valor do lote (MT)", min_value=1.0, value=5000.0)

if st.button("Adicionar Produto"):
    st.session_state.itens.append({
        "nome": nome,
        "dias": dias,
        "valor": valor
    })

# ------------------ TOTAL REAL ------------------
total_real = sum(item["valor"] for item in st.session_state.itens)

if total_real > 0:
    st.markdown(f"## 🚨 TOTAL REAL EM RISCO: {total_real:,.2f} MT")

# ------------------ LISTA + AÇÃO ------------------
for item in st.session_state.itens:
    st.write(f"### 🚩 {item['nome']}")

    perda_dia = item["valor"] / item["dias"]
    recuperavel = item["valor"] * 0.85

    st.warning(f"Perde {perda_dia:,.2f} MT por dia se não agir.")

    st.info(
        f"👉 Se NÃO agir: perde {item['valor']:,.2f} MT\n"
        f"👉 Se agir hoje (desconto 15%): recupera {recuperavel:,.2f} MT"
    )

# ------------------ AÇÃO FINAL ------------------
st.divider()

st.success("💡 DECISÃO: Cada dia parado aumenta o prejuízo. Ação hoje = dinheiro recuperado.")

# ------------------ BOTÃO LIMPAR ------------------
if st.button("Limpar Lista"):
    st.session_state.itens = []

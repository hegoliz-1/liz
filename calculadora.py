import streamlit as st

st.set_page_config(page_title="Neon Calc", page_icon="⚡")

# --- DISEÑO CYBERPUNK ---
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    /* Estilo del visor */
    .stTextInput>div>div>input {
        color: #00ff41; /* Verde Matrix */
        font-family: 'Courier New', monospace;
        font-size: 40px;
        text-align: right;
        background-color: #1a1c24;
        border: 2px solid #00ff41;
        border-radius: 10px;
        box-shadow: 0 0 10px #00ff41;
    }
    /* Estilo de los botones */
    .stButton>button {
        background-color: #262730;
        color: #ff00ff; /* Rosa Neon */
        border: 1px solid #ff00ff;
        border-radius: 5px;
        height: 60px;
        font-size: 22px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #ff00ff;
        color: white;
        box-shadow: 0 0 20px #ff00ff;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("⚡ Cyber-Calculator")

# Estado de la pantalla
if 'op' not in st.session_state:
    st.session_state.op = ""

# Visor (usamos un text_input de solo lectura para el diseño)
st.text_input("", value=st.session_state.op if st.session_state.op else "0", key="visor")

# Definición de botones en una lista de listas (filas)
botones = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

# Generación automática de la cuadrícula
for fila in botones:
    cols = st.columns(4)
    for i, tecla in enumerate(fila):
        with cols[i]:
            if st.button(tecla, key=f"btn_{tecla}_{i}"):
                if tecla == 'C':
                    st.session_state.op = ""
                elif tecla == '=':
                    try:
                        # Calculamos el resultado
                        st.session_state.op = str(round(eval(st.session_state.op), 4))
                    except:
                        st.session_state.op = "ERROR"
                else:
                    # Evitar repetir errores después de un fallo
                    if st.session_state.op == "ERROR":
                        st.session_state.op = ""
                    st.session_state.op += tecla
                st.rerun()

st.caption("Hecho con ❤️ en el futuro")
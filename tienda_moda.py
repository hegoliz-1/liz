import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Moda Femme | Colección 2026", layout="wide")

# --- ESTILO PERSONALIZADO ---
# Aplicamos un fondo morado suave y botones a juego
st.markdown("""
    <style>
    .main {
        background-color: #f3e5f5; /* Un lila muy claro para el fondo */
    }
    .stButton>button {
        border-radius: 15px;
        background-color: #7b1fa2; /* Morado intenso */
        color: white;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #4a148c;
        color: #e1bee7;
    }
    h1, h2, h3 {
        color: #4a148c;
    }
    </style>
    """, unsafe_allow_html=True)

# --- NAVEGACIÓN ---
choice = st.sidebar.selectbox("Explorar:", ["Inicio", "Catálogo Mujer", "Carrito"])

# --- PRODUCTOS DE ROPA (IMÁGENES PEQUEÑAS) ---
ropa_mujer = [
    {
        "nombre": "Vestido Floral de Verano",
        "precio": 45.0,
        "img": "data:image/jpeg;base64,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w=500",
        "desc": "Ligero, fresco y con un estampado vibrante."
    },
    {
        "nombre": "Blazer Ejecutivo Lila",
        "precio": 65.0,
        "img": "https://images.unsplash.com/photo-1591047139829-d91aecb6caea?w=500",
        "desc": "Elegancia moderna para la oficina."
    },
    {
        "nombre": "Jeans High Rise",
        "precio": 38.0,
        "img": "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?w=500",
        "desc": "Corte perfecto que estiliza tu figura."
    },
    {
        "nombre": "Conjunto Knit Soft",
        "precio": 55.0,
        "img": "https://images.unsplash.com/photo-1620799140408-edc6dcb6d633?w=500",
        "desc": "Comodidad total con un toque de lujo."
    },
    {
        "nombre": "Bolso de Mano 'Night'",
        "precio": 30.0,
        "img": "https://http2.mlstatic.com/D_NQ_NP_845749-MLU71044747252_082023-O.webpw=500",
        "desc": "El accesorio ideal para tus salidas nocturnas."
    },
    {
        "nombre": "Gafas de Sol Retro",
        "precio": 20.0,
        "img": "https://encrypted-tbn1.gstatic.com/shopping?q=tbn:ANd9GcRDn-sYxY8beYqYoA6YoTC9iRVgpJV5pBrAfph3bJrsLj-sIuSzZUVRmZkQZMtgGtzKelRa-RYXX1QOfhpKhaSzO1addROARyYTc0x4qgZ3W8g9nkw5WxTiKsE-rK2XSzPlgNOdOh0GxQ0&usqp=CAcw=500",
        "desc": "Protección con estilo vintage."
    }
]

# --- LÓGICA ---
if choice == "Inicio":
    st.title("👗 Moda Femme: Tu Estilo, Tu Regla")
    st.subheader("Nueva Colección Temporada 2026")
    # Banner de moda
    st.image("https://images.unsplash.com/photo-1490481651871-ab68de25d43d?w=1200", use_container_width=True)
    st.write("Descubre prendas diseñadas para empoderar y resaltar tu esencia única.")

elif choice == "Catálogo Mujer":
    st.title("Catálogo Exclusivo")
    st.write("Selecciona tus prendas favoritas.")
    
    # Usamos 3 columnas para que las imágenes se mantengan ordenadas y pequeñas
    cols = st.columns(3)
    
    for i, item in enumerate(ropa_mujer):
        with cols[i % 3]:
            # Ajuste a width=250 para que sean compactas pero legibles
            st.image(item["img"], width=250)
            st.subheader(item["nombre"])
            st.markdown(f"**{item['desc']}**")
            st.write(f"Precio: **${item['precio']}**")
            st.button("Añadir al Carrito", key=f"ropa_{i}")

elif choice == "Carrito":
    st.title("Tu Selección 🛒")
    st.write("Aquí aparecerán las prendas que elijas.")
    st.info("Tu carrito está vacío por ahora. ¡Ve al catálogo y elige algo increíble!")

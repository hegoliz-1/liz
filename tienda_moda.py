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
        "img": "https://images.unsplash.com/photo-1572804013307-a9a111d7273d?w=500",
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
import streamlit as st
from PIL import Image

# --- CONFIGURACIÓN DE PÁGINAS ---
def about_me():
    st.title("🏠 Acerca de Mí")
    st.write("""
    Esta es la página "Acerca de Mí". Aquí puedes incluir información sobre ti,
    tu proyecto o cualquier otro detalle relevante.
    """)

def dashboard():
    st.title("📊 Tablero de Datos")
    st.write("Esta es la página del tablero de datos.")

    # Ejemplo de un DataFrame
    import pandas as pd
    data = {
        "Nombre": ["Juan", "María", "Pedro"],
        "Edad": [25, 30, 35],
        "Ciudad": ["Madrid", "Barcelona", "Valencia"],
    }
    df = pd.DataFrame(data)
    st.dataframe(df)

def chatbot():
    st.title("🤖 Chat Bot")
    st.write("Esta es la página del Chat Bot.")

    # Ejemplo de un chat interactivo
    user_input = st.text_input("Escribe algo:")
    if user_input:
        st.write(f"El bot responde: ¡Hola! Has escrito '{user_input}'.")

# --- MENÚ FIJO CON BOTONES ESTILIZADOS ---

# Sidebar con logo y navegación
with st.sidebar:
    logo = Image.open("assets/0. logo.png")
    st.image(logo, width=200)

st.sidebar.markdown("### 🌟 Menú Principal")

# Contenedor para los botones
with st.sidebar:
    if st.button("🏠 Acerca de Mí", use_container_width=True):
        st.session_state.page = "about_me"
    if st.button("📊 Tablero de Datos", use_container_width=True):
        st.session_state.page = "dashboard"
   # Línea divisoria después de la segunda opción
    st.sidebar.markdown("---")

    if st.button("🤖 Chat Bot", use_container_width=True):
        st.session_state.page = "chatbot"
    
# --- ELEMENTOS COMPARTIDOS EN TODAS LAS PÁGINAS ---
try:
    # Usamos 'use_column_width=False' para evitar que ocupe todo el ancho, y especificamos el tamaño con 'width'
    st.image("assets/0. logo.png", width=100)  # Logo pequeño en la parte superior izquierda
except Exception:
    st.warning("No se pudo cargar el logo. Asegúrate de que el archivo '0. logo.png' esté en la carpeta 'assets/'.")
    
# Agregar un poco de espacio si es necesario para separar el logo de otros elementos
st.markdown("<br>", unsafe_allow_html=True)

st.sidebar.markdown("Hecho con ❤️ por [Michael Berríos Moreno](https://michaelberrios.carrd.co/#)")

# --- RENDERIZAR LA PÁGINA SELECCIONADA ---
if "page" not in st.session_state:
    st.session_state.page = "about_me"  # Página predeterminada

if st.session_state.page == "about_me":
    about_me()
elif st.session_state.page == "dashboard":
    dashboard()
elif st.session_state.page == "chatbot":
    chatbot()

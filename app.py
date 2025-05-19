import streamlit as st
from waybackpy import WaybackMachineSaveAPI

# Configuración de la página
st.set_page_config(page_title="Web Archiver", page_icon="📚")

# Título y descripción
st.title("🕵️ Web Page Archiver (WPA)")
st.markdown("""
Archiva cualquier página web en **Wayback Machine** y obtén un enlace permanente.
Ejemplo: [https://elarboldelafe.web.app/](https://elarboldelafe.web.app/)
""")

# Input de usuario
url = st.text_input("🔗 Ingresa la URL a archivar (ej: https://elarboldelafe.web.app/):")

if st.button("🚀 Archivar Página"):
    if url:
        try:
            # Guardar en Wayback Machine
            save_api = WaybackMachineSaveAPI(url, user_agent="streamlit-web-archiver")
            archived_url = save_api.save()
            
            # Mostrar resultados
            st.success(f"✅ **Página archivada correctamente!**")
            st.markdown(f"**Enlace archivado:** [{archived_url}]({archived_url})")
            
            # Vista previa (opcional)
            st.components.v1.iframe(archived_url, height=500, scrolling=True)
            
        except Exception as e:
            st.error(f"❌ Error al archivar: {e}")
    else:
        st.warning("⚠️ Por favor, ingresa una URL válida.")
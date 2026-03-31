import streamlit as st
import json
from pathlib import Path
from db import RecipeDatabase
from utils import display_recipe_card, display_ingredient_with_image

# Configuración de página
st.set_page_config(
    page_title="Mi Recetario",
    page_icon="🍳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado con tema luxury (crema/dorado/carbón)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&family=Cormorant+Garamond:wght@400;600&display=swap');
    
    * {
        font-family: 'Montserrat', sans-serif;
    }
    
    h1, h2, h3 {
        font-family: 'Cormorant Garamond', serif;
        color: #2c2c2c;
    }
    
    body {
        background-color: #faf8f3;
        color: #2c2c2c;
    }
    
    .recipe-card {
        background: linear-gradient(135deg, #ffffff 0%, #fef9f0 100%);
        border-left: 4px solid #d4af37;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(212, 175, 55, 0.1);
        margin: 15px 0;
    }
    
    .category-badge {
        display: inline-block;
        padding: 6px 12px;
        border-radius: 20px;
        font-size: 0.85em;
        font-weight: 600;
        margin-right: 8px;
    }
    
    .category-rapida {
        background-color: #e8f5e9;
        color: #2e7d32;
    }
    
    .category-intermedia {
        background-color: #fff3e0;
        color: #e65100;
    }
    
    .category-trabajosa {
        background-color: #fce4ec;
        color: #c2185b;
    }
    
    .category-futurelife {
        background-color: #e0f2f1;
        color: #00695c;
    }
    
    .ingredient-item {
        background-color: #fafafa;
        padding: 12px;
        border-radius: 6px;
        margin: 8px 0;
        border-left: 3px solid #d4af37;
    }
    
    .step-number {
        display: inline-block;
        background-color: #d4af37;
        color: white;
        width: 30px;
        height: 30px;
        border-radius: 50%;
        text-align: center;
        line-height: 30px;
        font-weight: bold;
        margin-right: 10px;
    }
    
    .recipe-meta {
        display: flex;
        gap: 20px;
        margin: 15px 0;
        font-size: 0.95em;
        color: #666;
    }
    
    .recipe-meta-item {
        display: flex;
        align-items: center;
        gap: 8px;
    }
    
    .difficulty-easy { color: #2e7d32; font-weight: 600; }
    .difficulty-medium { color: #e65100; font-weight: 600; }
    .difficulty-hard { color: #c2185b; font-weight: 600; }
    
    .sidebar-section {
        margin: 20px 0;
        padding: 15px;
        background-color: rgba(212, 175, 55, 0.05);
        border-radius: 8px;
    }
    </style>
    """, unsafe_allow_html=True)

# Inicializar base de datos
db = RecipeDatabase()

# Header
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown("<h1 style='margin-bottom: 0;'>🍳 Mi Recetario</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #666; margin-top: -10px;'>Recetas deliciosas organizadas por tiempo</p>", unsafe_allow_html=True)

# Sidebar - Navegación
with st.sidebar:
    st.markdown("<div class='sidebar-section'>", unsafe_allow_html=True)
    st.markdown("### 📂 Categorías")
    
    categorias = {
        "🚀 Rápidas": "rapida",
        "⏱️ Intermedias": "intermedia",
        "👨‍🍳 Trabajosas": "trabajosa",
        "🌟 FutureLife": "futurelife"
    }
    
    categoria_seleccionada = st.radio(
        "Elige una categoría",
        options=list(categorias.keys()),
        label_visibility="collapsed"
    )
    categoria_valor = categorias[categoria_seleccionada]
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Estadísticas
    st.markdown("<div class='sidebar-section'>", unsafe_allow_html=True)
    st.markdown("### 📊 Estadísticas")
    recipes = db.get_all_recipes()
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Recetas", len(recipes))
    with col2:
        cat_count = len([r for r in recipes if r['categoria'] == categoria_valor])
        st.metric(categoria_seleccionada.split()[1], cat_count)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Info
    st.markdown("<div class='sidebar-section'>", unsafe_allow_html=True)
    st.markdown("### ℹ️ Sobre esta app")
    st.caption("Recetario personal creado con Python y Streamlit. Todas tus recetas favoritas, organizadas y con fotos de ingredientes para que no haya errores.")
    st.markdown("</div>", unsafe_allow_html=True)

# Contenido principal
st.markdown(f"## {categoria_seleccionada}")

# Obtener recetas de la categoría seleccionada
recipes = db.get_recipes_by_category(categoria_valor)

if not recipes:
    st.info(f"📭 Aún no hay recetas en la categoría '{categoria_seleccionada.split()[1]}'")
else:
    # Filtro de búsqueda
    col1, col2 = st.columns([3, 1])
    with col1:
        search_term = st.text_input("🔍 Buscar receta...", placeholder="Ej: pasta, pollo, ensalada...")
    
    if search_term:
        recipes = [r for r in recipes if search_term.lower() in r['nombre'].lower()]
    
    # Mostrar recetas
    for recipe in recipes:
        with st.container():
            st.markdown("<div class='recipe-card'>", unsafe_allow_html=True)
            
            # Encabezado con nombre y categoría
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"### {recipe['nombre']}")
            with col2:
                cat_emoji = {
                    "rapida": "🚀",
                    "intermedia": "⏱️",
                    "trabajosa": "👨‍🍳",
                    "futurelife": "🌟"
                }
                cat_names = {
                    "rapida": "Rápida",
                    "intermedia": "Intermedia",
                    "trabajosa": "Trabajosa",
                    "futurelife": "FutureLife"
                }
                emoji = cat_emoji.get(recipe['categoria'], "")
                name = cat_names.get(recipe['categoria'], "")
                st.markdown(
                    f"<span class='category-badge category-{recipe['categoria']}'>{emoji} {name}</span>",
                    unsafe_allow_html=True
                )
            
            # Metadatos (tiempo, dificultad, porciones)
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.markdown(f"⏱️ **Tiempo**: {recipe['tiempo_minutos']} min")
            with col2:
                dif_class = f"difficulty-{recipe['dificultad']}"
                dif_text = {"facil": "Fácil", "media": "Media", "dificil": "Difícil"}
                st.markdown(f"<span class='{dif_class}'>📊 {dif_text.get(recipe['dificultad'], 'Media')}</span>", unsafe_allow_html=True)
            with col3:
                st.markdown(f"👥 **Porciones**: {recipe['porciones']}")
            with col4:
                if recipe.get('notas'):
                    st.markdown(f"📝 Notas")
            
            # Pestañas para ingredientes y pasos
            tab1, tab2 = st.tabs(["📋 Ingredientes", "👨‍🍳 Pasos"])
            
            with tab1:
                st.markdown("#### Ingredientes")
                for idx, ing in enumerate(recipe['ingredientes'], 1):
                    col1, col2, col3 = st.columns([1, 1, 2])
                    
                    with col1:
                        # Imagen del ingrediente
                        img_path = Path(f"assets/ingredients/{ing['imagen']}")
                        if img_path.exists():
                            st.image(str(img_path), width=80, use_column_width=False)
                        else:
                            st.markdown("🖼️ Sin foto")
                    
                    with col2:
                        st.markdown(f"**{ing['nombre']}**")
                        st.caption(f"{ing['cantidad']} {ing['unidad']}")
                    
                    with col3:
                        if ing.get('notas'):
                            st.caption(f"💡 {ing['notas']}")
            
            with tab2:
                st.markdown("#### Pasos de Preparación")
                for idx, paso in enumerate(recipe['pasos'], 1):
                    st.markdown(f"<span class='step-number'>{idx}</span> {paso}", unsafe_allow_html=True)
            
            # Notas adicionales
            if recipe.get('notas'):
                st.markdown("---")
                st.markdown(f"**📌 Notas especiales:** {recipe['notas']}")
            
            st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #999; font-size: 0.9em;'>"
    "🍳 Creado con amor para disfrutar cocinando juntos"
    "</p>",
    unsafe_allow_html=True
)

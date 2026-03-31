import streamlit as st
from pathlib import Path
from db import RecipeDatabase

st.set_page_config(page_title="Mi Recetario", layout="wide")

db = RecipeDatabase()

# =========================
# ASEGURAR CARPETA IMÁGENES
# =========================
Path("assets/ingredients").mkdir(parents=True, exist_ok=True)

# =========================
# TABS
# =========================
tab1, tab2 = st.tabs(["📖 Ver recetas", "➕ Añadir receta"])

# =========================
# VER RECETAS
# =========================
with tab1:
    st.title("🍳 Mi Recetario")

    categoria = st.selectbox(
        "Categoría",
        ["rapida", "intermedia", "trabajosa", "futurelife"]
    )

    recetas = db.get_recipes_by_category(categoria)

    for receta in recetas:
        st.subheader(receta["nombre"])

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### Ingredientes")
            for ing in receta["ingredientes"]:
                col_img, col_txt = st.columns([1, 3])

                with col_img:
                    img_path = Path(f"assets/ingredients/{ing['imagen']}")
                    if img_path.exists():
                        st.image(str(img_path), width=60)

                with col_txt:
                    st.markdown(f"**{ing['nombre']}**")
                    st.caption(f"{ing['cantidad']} {ing['unidad']}")

        with col2:
            st.markdown("### Pasos")
            for i, paso in enumerate(receta["pasos"], 1):
                st.markdown(f"{i}. {paso}")

        st.divider()

# =========================
# AÑADIR RECETA
# =========================
with tab2:
    st.title("➕ Nueva receta")

    nombre = st.text_input("Nombre de la receta")

    categoria = st.selectbox(
        "Categoría",
        ["rapida", "intermedia", "trabajosa", "futurelife"]
    )

    tiempo = st.number_input("Tiempo (minutos)", 0, 300, 30)
    dificultad = st.selectbox("Dificultad", ["facil", "media", "dificil"])
    porciones = st.number_input("Porciones", 1, 10, 2)
    notas = st.text_area("Notas (opcional)")

    st.markdown("## Ingredientes")

    ingredientes = []
    num_ing = st.number_input("Número de ingredientes", 1, 15, 3)

    for i in range(int(num_ing)):
        st.markdown(f"### Ingrediente {i+1}")

        nombre_ing = st.text_input("Nombre", key=f"n{i}")
        cantidad = st.number_input("Cantidad", key=f"c{i}")
        unidad = st.text_input("Unidad (g, ml, unidad...)", key=f"u{i}")

        imagen = st.file_uploader("Foto", type=["jpg", "png"], key=f"img{i}")

        nombre_archivo = ""

        if imagen is not None:
            nombre_archivo = imagen.name
            ruta = Path(f"assets/ingredients/{nombre_archivo}")

            with open(ruta, "wb") as f:
                f.write(imagen.getbuffer())

        ingredientes.append({
            "nombre": nombre_ing,
            "cantidad": cantidad,
            "unidad": unidad,
            "imagen": nombre_archivo,
            "notas": ""
        })

        st.divider()

    st.markdown("## Pasos")

    pasos_texto = st.text_area("Un paso por línea")

    if st.button("Guardar receta 💾"):

        pasos = [p for p in pasos_texto.split("\n") if p.strip() != ""]

        try:
            db.add_recipe(
                nombre=nombre,
                categoria=categoria,
                tiempo_minutos=tiempo,
                dificultad=dificultad,
                porciones=porciones,
                notas=notas,
                ingredientes=ingredientes,
                pasos=pasos
            )

            st.success("Receta guardada 💛")

        except Exception as e:
            st.error(f"Error: {e}")
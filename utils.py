import streamlit as st
from pathlib import Path

def display_recipe_card(recipe):
    """
    Muestra una tarjeta de receta con formato bonito
    """
    pass  # La funcionalidad está en app.py, esta función es para futuras extensiones

def display_ingredient_with_image(ingredient, col_width=80):
    """
    Muestra un ingrediente con su imagen
    """
    pass  # La funcionalidad está en app.py

def validate_image_path(filename):
    """
    Valida que la imagen existe en la carpeta de ingredientes
    """
    img_path = Path(f"assets/ingredients/{filename}")
    return img_path.exists()

def get_difficulty_color(dificultad):
    """Retorna el color según dificultad"""
    colors = {
        "facil": "#2e7d32",
        "media": "#e65100",
        "dificil": "#c2185b"
    }
    return colors.get(dificultad, "#2c2c2c")

def get_category_emoji(categoria):
    """Retorna emoji según categoría"""
    emojis = {
        "rapida": "🚀",
        "intermedia": "⏱️",
        "trabajosa": "👨‍🍳",
        "futurelife": "🌟"
    }
    return emojis.get(categoria, "📖")

def format_time_display(minutos):
    """Formatea el tiempo de preparación de forma legible"""
    if minutos < 60:
        return f"{minutos} min"
    else:
        horas = minutos // 60
        mins = minutos % 60
        if mins == 0:
            return f"{horas}h"
        else:
            return f"{horas}h {mins}min"

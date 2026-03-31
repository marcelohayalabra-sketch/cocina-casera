# 🍳 Mi Recetario - App de Recetas

Una aplicación de recetas moderna, diseñada para compartir tus mejores platos con fotos de ingredientes y pasos detallados.

## 📁 Estructura del Proyecto

```
recetario_app/
├── app.py                 # Aplicación principal de Streamlit
├── db.py                  # Módulo de base de datos SQLite
├── recipes.py             # Script para cargar/crear recetas
├── utils.py               # Funciones auxiliares
├── requirements.txt       # Dependencias de Python
├── recetas.db             # Base de datos (se crea automáticamente)
├── assets/
│   └── ingredients/       # Carpeta para fotos de ingredientes
└── .streamlit/
    └── config.toml        # Configuración de Streamlit (opcional)
```

## 🚀 Instalación Local

### 1. Clonar el repositorio
```bash
git clone https://github.com/tuusuario/recetario_app.git
cd recetario_app
```

### 2. Crear un entorno virtual
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Cargar recetas de ejemplo
```bash
python recipes.py --samples
```

### 5. Ejecutar la app
```bash
streamlit run app.py
```

La app se abrirá en `http://localhost:8501`

## 📸 Cómo Añadir Imágenes de Ingredientes

1. **Descarga las fotos de tus ingredientes**
   - Nombres claros: `tomate.jpg`, `ajo.jpg`, `pasta.jpg`, etc.
   - Formato recomendado: JPG o PNG
   - Tamaño: ~200x200px es suficiente

2. **Coloca las imágenes en la carpeta `assets/ingredients/`**
   ```
   assets/ingredients/
   ├── tomate.jpg
   ├── ajo.jpg
   ├── pasta.jpg
   ├── aceite_oliva.jpg
   └── ...
   ```

3. **Referencia en las recetas**
   - Al crear/importar una receta, el campo `imagen` debe coincidir exactamente con el nombre del archivo
   - Ejemplo: `"imagen": "tomate.jpg"`

## ➕ Añadir Recetas Personalizadas

### Opción 1: Interfaz interactiva
```bash
python recipes.py --add
```

Sigue las instrucciones en la terminal para crear tu receta paso a paso.

### Opción 2: Modificar `recipes.py` directamente
Edita el archivo `recipes.py` y añade una nueva función similar a `load_sample_recipes()`:

```python
db.add_recipe(
    nombre="Nombre de tu receta",
    categoria="rapida",  # rapida, intermedia, trabajosa, futurelife
    tiempo_minutos=30,
    dificultad="media",  # facil, media, dificil
    porciones=4,
    notas="Notas adicionales",
    ingredientes=[
        {"nombre": "Ingrediente", "cantidad": 100, "unidad": "g", "imagen": "ingrediente.jpg", "notas": "Notas"},
        # más ingredientes...
    ],
    pasos=[
        "Paso 1",
        "Paso 2",
        # más pasos...
    ]
)
```

## 🌐 Desplegar en Streamlit Cloud

### 1. Subir a GitHub
```bash
git add .
git commit -m "Initial commit: Recetario app"
git push origin main
```

### 2. Conectar a Streamlit Cloud
1. Ve a [Streamlit Cloud](https://streamlit.io/cloud)
2. Haz click en "New app"
3. Selecciona tu repositorio de GitHub
4. Elige `main` como rama y `app.py` como archivo principal
5. Click en "Deploy"

### 3. Compartir con tu esposa
Una vez desplegado, obtendrás una URL como:
```
https://tuusuario-recetario-app-xxxxxx.streamlit.app
```

Comparte esta URL con tu esposa. Ella podrá acceder desde cualquier dispositivo (móvil, tablet, ordenador) sin necesidad de instalar nada.

## 📝 Categorías de Recetas

- **🚀 Rápidas**: Menos de 30 minutos (ej: Pasta Aglio e Olio)
- **⏱️ Intermedias**: 30-60 minutos (ej: Tortilla de Patatas)
- **👨‍🍳 Trabajosas**: Más de 60 minutos o recetas complejas (ej: Paella Valenciana)
- **🌟 FutureLife**: Recetas modernas, innovadoras, saludables (ej: Buddha Bowls)

## 🎨 Personalización

### Cambiar colores/estilo
Edita el CSS en `app.py` sección `st.markdown()` bajo la línea de `set_page_config()`.

Colores actuales:
- Fondo: `#faf8f3` (crema)
- Acentos: `#d4af37` (dorado)
- Texto: `#2c2c2c` (carbón)

### Cambiar fuentes
Las fuentes están importadas de Google Fonts. Editables en el CSS:
- Titles: `Cormorant Garamond`
- Contenido: `Montserrat`

## 🔒 Privacidad y Seguridad

- La app es solo lectura para tu esposa (no puede editar ni eliminar recetas)
- La base de datos SQLite se aloja en el repositorio de GitHub
- Si quieres mayor privacidad, puedes hacer el repositorio privado
- La contraseña o autenticación se puede añadir en futuras versiones

## 🐛 Troubleshooting

### "No se cargan las imágenes"
- Verifica que las imágenes estén en `assets/ingredients/`
- Asegúrate que los nombres coincidan exactamente (mayúsculas/minúsculas)
- Formato soportado: JPG, PNG, GIF, WebP

### "Error al conectar a la base de datos"
- Elimina `recetas.db` y vuelve a crear con `python recipes.py --samples`
- Verifica permisos de escritura en la carpeta

### "La app tarda mucho en cargar"
- Si las imágenes son muy grandes, redimensiónalas
- Streamlit Cloud puede tardar más si usas muchas imágenes

## 📧 Soporte y Mejoras Futuras

Posibles mejoras:
- [ ] Sistema de calificaciones/favoritos
- [ ] Generador de lista de compra
- [ ] Filtros por ingredientes
- [ ] Historial de recetas cocinadas
- [ ] Compartir recetas por WhatsApp/Email
- [ ] Modo oscuro

## 📄 Licencia

Uso personal. ¡Que disfrutes cocinando con tu esposa! 🍽️

---

**Creado con ❤️ para disfrutar cocinando juntos**

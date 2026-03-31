# 🍳 Guía Rápida - Mi Recetario

## Paso 1️⃣ : Clonar en GitHub

1. Ve a github.com y crea un nuevo repositorio llamado `recetario_app` (puede ser privado)
2. Clone el repositorio en tu ordenador:
   ```bash
   git clone https://github.com/TU_USUARIO/recetario_app.git
   cd recetario_app
   ```

3. Copia todos estos archivos a esa carpeta:
   - `app.py`
   - `db.py`
   - `recipes.py`
   - `utils.py`
   - `requirements.txt`
   - `README.md`
   - `.gitignore`
   - `setup.sh` (para Linux/Mac)

4. Crea la carpeta `assets/ingredients/` (donde irán las fotos)

5. Sube a GitHub:
   ```bash
   git add .
   git commit -m "Mi Recetario - versión inicial"
   git push origin main
   ```

## Paso 2️⃣ : Probar Localmente (Opcional)

Si quieres probar en tu ordenador antes de subirlo a la nube:

```bash
# Instalar dependencias
pip install -r requirements.txt

# Cargar recetas de ejemplo
python recipes.py --samples

# Ejecutar la app
streamlit run app.py
```

Abre http://localhost:8501 en tu navegador.

## Paso 3️⃣ : Desplegar en Streamlit Cloud

1. Ve a https://streamlit.io/cloud
2. Haz click en "New app"
3. Conecta tu cuenta de GitHub
4. Selecciona:
   - Repository: `TU_USUARIO/recetario_app`
   - Branch: `main`
   - Main file path: `app.py`
5. Click "Deploy"

¡**Listo!** Tu app estará disponible en una URL como:
```
https://tuusuario-recetario-app-xxxxx.streamlit.app
```

Comparte esta URL con tu esposa. 📱

## Paso 4️⃣ : Añadir Tus Recetas

### Opción A: Usar la interfaz interactiva
```bash
python recipes.py --add
```
Contesta las preguntas y crea tu receta.

### Opción B: Editar `recipes.py` directamente
Copia una de las recetas de ejemplo y personalízala.

### Importante: Las imágenes de ingredientes
1. Descarga fotos JPG/PNG de tus ingredientes
2. Renómbralas simple: `tomate.jpg`, `ajo.jpg`, etc.
3. Colócalas en `assets/ingredients/`
4. Referencia en la receta: `"imagen": "tomate.jpg"`

## Paso 5️⃣ : Actualizar desde GitHub

Cada vez que hagas cambios:

```bash
# Realiza tus cambios (edita archivos, añade recetas, imágenes)

# Sube a GitHub
git add .
git commit -m "Añadida receta: Paella"
git push origin main
```

Streamlit Cloud **automáticamente** actualizará la app con los cambios. Solo espera 30-60 segundos.

---

## 📸 Recomendaciones para Imágenes

- **Formato**: JPG o PNG
- **Tamaño**: 200x200px - 400x400px (no muy pesadas)
- **Nombres claros sin espacios**: `tomate.jpg` ✓ | `tomate rojo.jpg` ✗

### Dónde conseguir imágenes
- Google Images (descarga)
- Freepik.com
- Pixabay.com
- Pexels.com
- O toma tú mismo las fotos de tus ingredientes 📸

---

## 🎯 Estructura Final

```
recetario_app/
├── app.py
├── db.py
├── recipes.py
├── utils.py
├── requirements.txt
├── README.md
├── .gitignore
├── setup.sh
├── recetas.db (se crea automáticamente)
├── assets/
│   └── ingredients/
│       ├── tomate.jpg
│       ├── ajo.jpg
│       ├── pasta.jpg
│       └── ... (más imágenes)
└── .streamlit/
    └── config.toml
```

---

## ❓ Preguntas Frecuentes

### "¿Puedo hacer privado el repositorio?"
Sí. Pero en Streamlit Cloud tendrás que conectar tu cuenta de GitHub.

### "¿Puedo editar recetas desde la app?"
Por ahora solo tu esposa puede **ver**. Para editar, edita `recipes.py` y sube a GitHub. En futuras versiones podemos añadir edición desde la app.

### "¿Dónde se guardan las recetas?"
En `recetas.db` (base de datos SQLite). Se sincroniza automáticamente con GitHub.

### "¿Las imágenes se suben también a GitHub?"
Sí, todo lo que está en `assets/ingredients/` se sube junto con los cambios.

### "¿Puede acceder desde el móvil?"
Sí, desde cualquier navegador (iOS o Android) accediendo a la URL de Streamlit Cloud.

---

## 📞 Soporte

Si algo no funciona:
1. Verifica que todos los archivos estén en la carpeta correcta
2. Comprueba los nombres de las imágenes (sensibles a mayúsculas)
3. Lee el mensaje de error en la consola (si ejecutas localmente)
4. Revisa el README.md para solución de problemas

---

**¡Que disfrutes cocinando! 🍽️👨‍🍳**

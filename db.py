import sqlite3
import json
from pathlib import Path
from datetime import datetime

class RecipeDatabase:
    def __init__(self, db_path="recetas.db"):
        self.db_path = db_path
        self.init_db()
    
    def init_db(self):
        """Inicializa la base de datos con las tablas necesarias"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Tabla de recetas
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS recetas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL UNIQUE,
                categoria TEXT NOT NULL,
                tiempo_minutos INTEGER,
                dificultad TEXT,
                porciones INTEGER,
                notas TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Tabla de ingredientes
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ingredientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                receta_id INTEGER NOT NULL,
                nombre TEXT NOT NULL,
                cantidad REAL NOT NULL,
                unidad TEXT,
                imagen TEXT,
                notas TEXT,
                FOREIGN KEY (receta_id) REFERENCES recetas(id) ON DELETE CASCADE
            )
        """)
        
        # Tabla de pasos
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pasos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                receta_id INTEGER NOT NULL,
                orden INTEGER NOT NULL,
                descripcion TEXT NOT NULL,
                FOREIGN KEY (receta_id) REFERENCES recetas(id) ON DELETE CASCADE
            )
        """)
        
        conn.commit()
        conn.close()
    
    def add_recipe(self, nombre, categoria, tiempo_minutos=0, dificultad="media", 
                   porciones=4, notas="", ingredientes=None, pasos=None):
        """
        Añade una nueva receta a la base de datos
        
        Args:
            nombre: Nombre de la receta
            categoria: 'rapida', 'intermedia', 'trabajosa', 'futurelife'
            tiempo_minutos: Tiempo de preparación
            dificultad: 'facil', 'media', 'dificil'
            porciones: Número de porciones
            notas: Notas adicionales
            ingredientes: Lista de dicts {nombre, cantidad, unidad, imagen, notas}
            pasos: Lista de strings con los pasos
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        try:
            cursor.execute("""
                INSERT INTO recetas (nombre, categoria, tiempo_minutos, dificultad, porciones, notas)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (nombre, categoria, tiempo_minutos, dificultad, porciones, notas))
            
            receta_id = cursor.lastrowid
            
            # Añadir ingredientes
            if ingredientes:
                for ing in ingredientes:
                    cursor.execute("""
                        INSERT INTO ingredientes (receta_id, nombre, cantidad, unidad, imagen, notas)
                        VALUES (?, ?, ?, ?, ?, ?)
                    """, (receta_id, ing['nombre'], ing['cantidad'], ing.get('unidad', ''),
                          ing.get('imagen', ''), ing.get('notas', '')))
            
            # Añadir pasos
            if pasos:
                for idx, paso in enumerate(pasos, 1):
                    cursor.execute("""
                        INSERT INTO pasos (receta_id, orden, descripcion)
                        VALUES (?, ?, ?)
                    """, (receta_id, idx, paso))
            
            conn.commit()
            return receta_id
        
        except sqlite3.IntegrityError:
            raise ValueError(f"Ya existe una receta con el nombre '{nombre}'")
        finally:
            conn.close()
    
    def get_all_recipes(self):
        """Obtiene todas las recetas"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM recetas ORDER BY nombre ASC")
        recipes = []
        
        for row in cursor.fetchall():
            recipe = self._format_recipe(row, conn)
            recipes.append(recipe)
        
        conn.close()
        return recipes
    
    def get_recipes_by_category(self, categoria):
        """Obtiene recetas por categoría"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM recetas WHERE categoria = ? ORDER BY nombre ASC", (categoria,))
        recipes = []
        
        for row in cursor.fetchall():
            recipe = self._format_recipe(row, conn)
            recipes.append(recipe)
        
        conn.close()
        return recipes
    
    def get_recipe_by_id(self, recipe_id):
        """Obtiene una receta por ID"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM recetas WHERE id = ?", (recipe_id,))
        row = cursor.fetchone()
        
        if row:
            recipe = self._format_recipe(row, conn)
            conn.close()
            return recipe
        
        conn.close()
        return None
    
    def _format_recipe(self, recipe_row, conn):
        """Formatea una receta con sus ingredientes y pasos"""
        cursor = conn.cursor()
        
        recipe_id = recipe_row[0]
        
        # Obtener ingredientes
        cursor.execute("SELECT nombre, cantidad, unidad, imagen, notas FROM ingredientes WHERE receta_id = ?", (recipe_id,))
        ingredientes = [
            {
                'nombre': row[0],
                'cantidad': row[1],
                'unidad': row[2],
                'imagen': row[3],
                'notas': row[4]
            }
            for row in cursor.fetchall()
        ]
        
        # Obtener pasos
        cursor.execute("SELECT descripcion FROM pasos WHERE receta_id = ? ORDER BY orden ASC", (recipe_id,))
        pasos = [row[0] for row in cursor.fetchall()]
        
        return {
            'id': recipe_row[0],
            'nombre': recipe_row[1],
            'categoria': recipe_row[2],
            'tiempo_minutos': recipe_row[3],
            'dificultad': recipe_row[4],
            'porciones': recipe_row[5],
            'notas': recipe_row[6],
            'created_at': recipe_row[7],
            'updated_at': recipe_row[8],
            'ingredientes': ingredientes,
            'pasos': pasos
        }
    
    def delete_recipe(self, recipe_id):
        """Elimina una receta"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("DELETE FROM recetas WHERE id = ?", (recipe_id,))
        conn.commit()
        conn.close()
    
    def update_recipe(self, recipe_id, nombre=None, categoria=None, tiempo_minutos=None,
                     dificultad=None, porciones=None, notas=None):
        """Actualiza los datos de una receta"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        updates = []
        params = []
        
        if nombre is not None:
            updates.append("nombre = ?")
            params.append(nombre)
        if categoria is not None:
            updates.append("categoria = ?")
            params.append(categoria)
        if tiempo_minutos is not None:
            updates.append("tiempo_minutos = ?")
            params.append(tiempo_minutos)
        if dificultad is not None:
            updates.append("dificultad = ?")
            params.append(dificultad)
        if porciones is not None:
            updates.append("porciones = ?")
            params.append(porciones)
        if notas is not None:
            updates.append("notas = ?")
            params.append(notas)
        
        if updates:
            updates.append("updated_at = CURRENT_TIMESTAMP")
            params.append(recipe_id)
            
            query = f"UPDATE recetas SET {', '.join(updates)} WHERE id = ?"
            cursor.execute(query, params)
            conn.commit()
        
        conn.close()
    
    def search_recipes(self, search_term):
        """Busca recetas por nombre"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        search_param = f"%{search_term}%"
        cursor.execute("SELECT * FROM recetas WHERE nombre LIKE ? ORDER BY nombre ASC", (search_param,))
        recipes = []
        
        for row in cursor.fetchall():
            recipe = self._format_recipe(row, conn)
            recipes.append(recipe)
        
        conn.close()
        return recipes

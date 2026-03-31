from db import RecipeDatabase

def load_sample_recipes():
    """Carga recetas de ejemplo en la base de datos"""
    db = RecipeDatabase()
    
    # Ejemplo 1: Pasta Aglio e Olio (Rápida)
    try:
        db.add_recipe(
            nombre="Pasta Aglio e Olio",
            categoria="rapida",
            tiempo_minutos=15,
            dificultad="facil",
            porciones=2,
            notas="Un clásico italiano simple pero delicioso",
            ingredientes=[
                {"nombre": "Pasta", "cantidad": 200, "unidad": "g", "imagen": "pasta.jpg", "notas": "Spaghetti o linguine"},
                {"nombre": "Ajo", "cantidad": 4, "unidad": "dientes", "imagen": "ajo.jpg", "notas": "Cortado en láminas finas"},
                {"nombre": "Aceite de oliva virgen extra", "cantidad": 100, "unidad": "ml", "imagen": "aceite_oliva.jpg", "notas": "De buena calidad"},
                {"nombre": "Guindilla roja", "cantidad": 1, "unidad": "pieza", "imagen": "guindilla.jpg", "notas": "Opcional, al gusto"},
                {"nombre": "Sal y pimienta", "cantidad": 1, "unidad": "pizca", "imagen": "sal.jpg", "notas": "Al gusto"},
            ],
            pasos=[
                "Hierve agua salada en una olla grande.",
                "Cocina la pasta hasta que esté al dente (9-10 minutos).",
                "Mientras tanto, calienta el aceite en una sartén a fuego bajo.",
                "Añade el ajo laminado y la guindilla. Deja que se dore sin quemarse.",
                "Escurre la pasta reservando una taza de agua de cocción.",
                "Añade la pasta al aceite con ajo. Mezcla bien.",
                "Si es necesario, añade un poco de agua de cocción para emulsionar.",
                "Sirve inmediatamente. Acabado con queso Pecorino si lo deseas.",
            ]
        )
        print("✓ Pasta Aglio e Olio añadida")
    except ValueError as e:
        print(f"✗ Pasta Aglio e Olio: {e}")
    
    # Ejemplo 2: Tortilla de Patatas (Intermedia)
    try:
        db.add_recipe(
            nombre="Tortilla de Patatas",
            categoria="intermedia",
            tiempo_minutos=30,
            dificultad="media",
            porciones=4,
            notas="La tortilla española clásica. Perfecto para comer o cenar.",
            ingredientes=[
                {"nombre": "Patatas", "cantidad": 600, "unidad": "g", "imagen": "patatas.jpg", "notas": "De tamaño mediano, peladas"},
                {"nombre": "Huevos", "cantidad": 5, "unidad": "piezas", "imagen": "huevos.jpg", "notas": "Frescos"},
                {"nombre": "Cebolla", "cantidad": 1, "unidad": "pieza", "imagen": "cebolla.jpg", "notas": "Cortada en rodajas finas (opcional)"},
                {"nombre": "Aceite de oliva", "cantidad": 150, "unidad": "ml", "imagen": "aceite_oliva.jpg", "notas": "Para freír"},
                {"nombre": "Sal", "cantidad": 1, "unidad": "pizca", "imagen": "sal.jpg", "notas": "Al gusto"},
            ],
            pasos=[
                "Pela las patatas y córtalas en rodajas finas (unos 3-4 mm).",
                "Si usas cebolla, córtala en rodajas finas.",
                "Calienta el aceite en una sartén grande a fuego medio-alto.",
                "Añade las patatas y cebolla (si la usas). Sofríe durante 15-20 minutos hasta que estén tiernas pero no doradas.",
                "Mientras se cocinan las patatas, bate los huevos en un bol grande con sal.",
                "Cuando las patatas estén listas, escúrrelas bien (reserva el aceite).",
                "Añade las patatas al bol con los huevos. Mezcla bien.",
                "En la misma sartén con un poco del aceite reservado, vierte la mezcla a fuego medio.",
                "Cocina 4-5 minutos hasta que el fondo esté dorado.",
                "Desliza la tortilla a un plato y, con cuidado, dale la vuelta en la sartén.",
                "Cocina el otro lado 2-3 minutos más.",
                "Sirve caliente, tibia o fría, cortada en porciones.",
            ]
        )
        print("✓ Tortilla de Patatas añadida")
    except ValueError as e:
        print(f"✗ Tortilla de Patatas: {e}")
    
    # Ejemplo 3: Paella (Trabajosa)
    try:
        db.add_recipe(
            nombre="Paella Valenciana",
            categoria="trabajosa",
            tiempo_minutos=60,
            dificultad="dificil",
            porciones=6,
            notas="Requiere atención constante. El secreto está en la técnica y los ingredientes frescos.",
            ingredientes=[
                {"nombre": "Arroz bomba", "cantidad": 300, "unidad": "g", "imagen": "arroz_bomba.jpg", "notas": "Variedad de arroz ideal para paella"},
                {"nombre": "Pollo", "cantidad": 400, "unidad": "g", "imagen": "pollo.jpg", "notas": "Cortado en trozos medianos"},
                {"nombre": "Conejo", "cantidad": 200, "unidad": "g", "imagen": "conejo.jpg", "notas": "Cortado en trozos (opcional, puede ser más pollo)"},
                {"nombre": "Judías verdes", "cantidad": 150, "unidad": "g", "imagen": "judias_verdes.jpg", "notas": "Troceadas"},
                {"nombre": "Tomate", "cantidad": 150, "unidad": "g", "imagen": "tomate.jpg", "notas": "Rallado o en salsa"},
                {"nombre": "Caldo de pollo", "cantidad": 750, "unidad": "ml", "imagen": "caldo.jpg", "notas": "Casero de preferencia"},
                {"nombre": "Aceite de oliva", "cantidad": 60, "unidad": "ml", "imagen": "aceite_oliva.jpg", "notas": ""},
                {"nombre": "Ajo", "cantidad": 2, "unidad": "dientes", "imagen": "ajo.jpg", "notas": "Picados"},
                {"nombre": "Pimentón", "cantidad": 1, "unidad": "cucharadita", "imagen": "pimenton.jpg", "notas": "Dulce"},
                {"nombre": "Azafrán", "cantidad": 1, "unidad": "pizca", "imagen": "azafran.jpg", "notas": "Disuelto en caldo caliente"},
                {"nombre": "Sal y pimienta", "cantidad": 1, "unidad": "pizca", "imagen": "sal.jpg", "notas": "Al gusto"},
            ],
            pasos=[
                "Calienta el caldo en una cacerola a fuego lento (mantenlo caliente durante todo el proceso).",
                "En una paellera o sartén grande, calienta el aceite a fuego medio-alto.",
                "Dora el pollo y conejo hasta que se doren los lados. Retira y reserva.",
                "En el mismo aceite, sofríe el ajo picado.",
                "Añade el tomate y cocina 5 minutos hasta que se reduzca.",
                "Añade el pimentón y mezcla bien (no dejes que se queme).",
                "Vuelve a añadir el pollo y conejo a la paellera.",
                "Vierte el arroz directamente en la paellera, removiendo 2-3 minutos para tostarlo.",
                "Añade el caldo caliente poco a poco, comenzando con el azafrán.",
                "Agrega las judías verdes. No remuevs más (este es el secreto).",
                "Deja que el arroz se cocine durante 20-25 minutos a fuego medio.",
                "El arroz debe absorber todo el líquido y los granos deben estar sueltos pero tiernos.",
                "Si es necesario, sube el fuego en los últimos 2-3 minutos para conseguir el 'socarrat' (fondo tostado).",
                "Retira del fuego y deja reposar 5 minutos cubierto.",
            ]
        )
        print("✓ Paella Valenciana añadida")
    except ValueError as e:
        print(f"✗ Paella Valenciana: {e}")
    
    # Ejemplo 4: Ensalada FutureLife (Innovadora)
    try:
        db.add_recipe(
            nombre="Ensalada Buddha Bowl",
            categoria="futurelife",
            tiempo_minutos=20,
            dificultad="facil",
            porciones=2,
            notas="Saludable, nutrición completa en un cuenco. Personalizable según gustos.",
            ingredientes=[
                {"nombre": "Espinaca fresca", "cantidad": 100, "unidad": "g", "imagen": "espinaca.jpg", "notas": "Base del cuenco"},
                {"nombre": "Quinoa cocida", "cantidad": 150, "unidad": "g", "imagen": "quinoa.jpg", "notas": "Previamente cocinada"},
                {"nombre": "Garbanzos tostados", "cantidad": 100, "unidad": "g", "imagen": "garbanzos.jpg", "notas": "De lata, drenados y tostados en sartén"},
                {"nombre": "Aguacate", "cantidad": 1, "unidad": "pieza", "imagen": "aguacate.jpg", "notas": "Cortado en rodajas"},
                {"nombre": "Zanahoria", "cantidad": 1, "unidad": "pieza", "imagen": "zanahoria.jpg", "notas": "Rallada o en bastoncillos"},
                {"nombre": "Remolacha", "cantidad": 100, "unidad": "g", "imagen": "remolacha.jpg", "notas": "Cocida y cortada en dados"},
                {"nombre": "Semillas de sésamo", "cantidad": 30, "unidad": "g", "imagen": "sesamo.jpg", "notas": "Tostadas"},
                {"nombre": "Tahini", "cantidad": 30, "unidad": "ml", "imagen": "tahini.jpg", "notas": "Para el aliño"},
                {"nombre": "Limón", "cantidad": 1, "unidad": "pieza", "imagen": "limon.jpg", "notas": "Jugo"},
                {"nombre": "Agua", "cantidad": 30, "unidad": "ml", "imagen": "agua.jpg", "notas": "Para diluir el tahini"},
                {"nombre": "Sal y pimienta", "cantidad": 1, "unidad": "pizca", "imagen": "sal.jpg", "notas": "Al gusto"},
            ],
            pasos=[
                "Si la quinoa no está cocinada, cuécela según las instrucciones del paquete.",
                "Coloca la espinaca fresca como base en un cuenco grande.",
                "Distribuye todos los ingredientes alrededor del cuenco: quinoa, garbanzos, aguacate, zanahoria, remolacha.",
                "Espolvorea las semillas de sésamo por encima.",
                "Para el aliño: mezcla el tahini con el jugo de limón y el agua hasta conseguir una consistencia cremosa.",
                "Condimenta con sal y pimienta.",
                "Vierte el aliño sobre el cuenco.",
                "Mezcla bien antes de comer o come 'de un lado a otro' si prefieres mantener la presentación.",
            ]
        )
        print("✓ Ensalada Buddha Bowl añadida")
    except ValueError as e:
        print(f"✗ Ensalada Buddha Bowl: {e}")

def add_custom_recipe():
    """Función interactiva para añadir una receta personalizada"""
    db = RecipeDatabase()
    
    print("\n=== AÑADIR RECETA PERSONALIZADA ===\n")
    
    nombre = input("Nombre de la receta: ")
    
    print("\nCategorías disponibles:")
    print("1. Rápidas (menos de 30 min)")
    print("2. Intermedias (30-60 min)")
    print("3. Trabajosas (más de 60 min)")
    print("4. FutureLife (innovadora/moderna)")
    
    cat_map = {"1": "rapida", "2": "intermedia", "3": "trabajosa", "4": "futurelife"}
    cat_choice = input("Elige categoría (1-4): ")
    categoria = cat_map.get(cat_choice, "intermedia")
    
    tiempo_minutos = int(input("Tiempo de preparación (minutos): "))
    
    print("\nDificultad:")
    print("1. Fácil")
    print("2. Media")
    print("3. Difícil")
    
    dif_map = {"1": "facil", "2": "media", "3": "dificil"}
    dif_choice = input("Elige dificultad (1-3): ")
    dificultad = dif_map.get(dif_choice, "media")
    
    porciones = int(input("Número de porciones: "))
    notas = input("Notas adicionales (opcional): ")
    
    # Ingredientes
    print("\n--- INGREDIENTES ---")
    ingredientes = []
    while True:
        print(f"\nIngrediente {len(ingredientes) + 1}:")
        nombre_ing = input("Nombre: ")
        if not nombre_ing:
            break
        
        cantidad = float(input("Cantidad: "))
        unidad = input("Unidad (g, ml, pieza, etc): ")
        imagen = input("Nombre de imagen (sin ruta, ej: tomate.jpg): ")
        notas_ing = input("Notas sobre ingrediente (opcional): ")
        
        ingredientes.append({
            "nombre": nombre_ing,
            "cantidad": cantidad,
            "unidad": unidad,
            "imagen": imagen,
            "notas": notas_ing
        })
    
    # Pasos
    print("\n--- PASOS DE PREPARACIÓN ---")
    pasos = []
    while True:
        print(f"\nPaso {len(pasos) + 1}:")
        paso = input("Descripción: ")
        if not paso:
            break
        pasos.append(paso)
    
    # Guardar
    try:
        db.add_recipe(
            nombre=nombre,
            categoria=categoria,
            tiempo_minutos=tiempo_minutos,
            dificultad=dificultad,
            porciones=porciones,
            notas=notas,
            ingredientes=ingredientes,
            pasos=pasos
        )
        print(f"\n✓ Receta '{nombre}' añadida correctamente!")
    except ValueError as e:
        print(f"\n✗ Error: {e}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "--samples":
            print("Cargando recetas de ejemplo...\n")
            load_sample_recipes()
        elif sys.argv[1] == "--add":
            add_custom_recipe()
    else:
        print("Uso:")
        print("  python recipes.py --samples    Cargar recetas de ejemplo")
        print("  python recipes.py --add        Añadir una receta personalizada")

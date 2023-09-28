class NodoArbol:
    def __init__(self, nombre, es_heroe):
        self.nombre = nombre
        self.es_heroe = es_heroe
        self.izquierdo = None
        self.derecho = None

def insertar(raiz, nombre, es_heroe):
    if raiz is None:
        return NodoArbol(nombre, es_heroe)
    if nombre < raiz.nombre:
        raiz.izquierdo = insertar(raiz.izquierdo, nombre, es_heroe)
    elif nombre > raiz.nombre:
        raiz.derecho = insertar(raiz.derecho, nombre, es_heroe)
    return raiz

def listar_villanos_en_orden(raiz):
    if raiz is not None:
        listar_villanos_en_orden(raiz.izquierdo)
        if not raiz.es_heroe:
            print(raiz.nombre)
        listar_villanos_en_orden(raiz.derecho)

def superheroes_con_c(raiz):
    if raiz is not None:
        superheroes_con_c(raiz.izquierdo)
        if raiz.es_heroe and raiz.nombre.startswith("C"):
            print(raiz.nombre)
        superheroes_con_c(raiz.derecho)

def contar_superheroes(raiz):
    count = 0
    if raiz is not None:
        if raiz.es_heroe:
            count += 1
        count += contar_superheroes(raiz.izquierdo)
        count += contar_superheroes(raiz.derecho)
    return count

def buscar_y_modificar(raiz, nombre_antiguo, nuevo_nombre):
    if raiz is None:
        return raiz
    if raiz.nombre == nombre_antiguo:
        raiz.nombre = nuevo_nombre
    elif nombre_antiguo < raiz.nombre:
        raiz.izquierdo = buscar_y_modificar(raiz.izquierdo, nombre_antiguo, nuevo_nombre)
    else:
        raiz.derecho = buscar_y_modificar(raiz.derecho, nombre_antiguo, nuevo_nombre)
    return raiz

def listar_superheroes_en_orden_descendente(raiz):
    if raiz is not None:
        listar_superheroes_en_orden_descendente(raiz.derecho)
        if raiz.es_heroe:
            print(raiz.nombre)
        listar_superheroes_en_orden_descendente(raiz.izquierdo)

def generar_bosque(raiz):
    arbol_heroes = None  
    arbol_villanos = None  
    
    def insertar_en_bosque(bosque, nombre, es_heroe):
        return insertar(bosque, nombre, es_heroe)
    
    if raiz is not None:
        arbol_heroes = insertar_en_bosque(arbol_heroes, raiz.nombre, raiz.es_heroe)
        arbol_villanos = insertar_en_bosque(arbol_villanos, raiz.nombre, not raiz.es_heroe)
        arbol_heroes = generar_bosque(raiz.izquierdo)
        arbol_villanos = generar_bosque(raiz.derecho)
    
    return arbol_heroes, arbol_villanos

def contar_nodos(raiz):
    if raiz is None:
        return 0
    return 1 + contar_nodos(raiz.izquierdo) + contar_nodos(raiz.derecho)

def barrido_ordenado_alfabeticamente(raiz):
    if raiz is not None:
        barrido_ordenado_alfabeticamente(raiz.izquierdo)
        print(raiz.nombre)
        barrido_ordenado_alfabeticamente(raiz.derecho)

raiz = None
raiz = insertar(raiz, "Spider-Man", True)
raiz = insertar(raiz, "Loki", False)
raiz = insertar(raiz, "Captain America", True)
raiz = insertar(raiz, "Doctor Strange", True)
raiz = insertar(raiz, "Thanos", False)

print("Listado de villanos en orden alfabético:")
listar_villanos_en_orden(raiz)

print("\nSuperhéroes cuyos nombres comienzan con 'C':")
superheroes_con_c(raiz)

print("\nCantidad de superhéroes en el árbol:", contar_superheroes(raiz))

raiz = buscar_y_modificar(raiz, "Doctor Strange", "Doctor Strange (Fixed)")

print("\nSuperhéroes en orden descendente:")
listar_superheroes_en_orden_descendente(raiz)

arbol_heroes, arbol_villanos = generar_bosque(raiz)

print("\nÁrbol de superhéroes:")
print("Cantidad de nodos en el árbol de superhéroes:", contar_nodos(arbol_heroes))
print("Listado de superhéroes en orden alfabético:")
barrido_ordenado_alfabeticamente(arbol_heroes)

print("\nÁrbol de villanos:")
print("Cantidad de nodos en el árbol de villanos:", contar_nodos(arbol_villanos))
print("Listado de villanos en orden alfabético:")
barrido_ordenado_alfabeticamente(arbol_villanos)

class NodoCriatura:
    def __init__(self, nombre, derrotada_por=None, descripcion=None, capturada=None):
        self.nombre = nombre
        self.derrotada_por = derrotada_por
        self.descripcion = descripcion
        self.capturada = capturada
        self.izquierdo = None
        self.derecho = None

def insertar_criatura(raiz, criatura):
    if raiz is None:
        return criatura
    if criatura.nombre < raiz.nombre:
        raiz.izquierdo = insertar_criatura(raiz.izquierdo, criatura)
    else:
        raiz.derecho = insertar_criatura(raiz.derecho, criatura)
    return raiz

def listar_inorden_con_derrotada(raiz):
    if raiz is not None:
        listar_inorden_con_derrotada(raiz.izquierdo)
        print(f"Criatura: {raiz.nombre}")
        if raiz.derrotada_por:
            print(f"Derrotada por: {', '.join(raiz.derrotada_por)}")
        listar_inorden_con_derrotada(raiz.derecho)

def cargar_descripcion(raiz, nombre_criatura, descripcion):
    if raiz is not None:
        if raiz.nombre == nombre_criatura:
            raiz.descripcion = descripcion
            return
        cargar_descripcion(raiz.izquierdo, nombre_criatura, descripcion)
        cargar_descripcion(raiz.derecho, nombre_criatura, descripcion)

def mostrar_informacion_criatura(raiz, nombre_criatura):
    if raiz is not None:
        if raiz.nombre == nombre_criatura:
            print(f"Nombre: {raiz.nombre}")
            if raiz.descripcion:
                print(f"Descripción: {raiz.descripcion}")
            if raiz.derrotada_por:
                print(f"Derrotada por: {', '.join(raiz.derrotada_por)}")
            if raiz.capturada:
                print(f"Capturada por: {raiz.capturada}")
            return
        mostrar_informacion_criatura(raiz.izquierdo, nombre_criatura)
        mostrar_informacion_criatura(raiz.derecho, nombre_criatura)

def heroes_mas_victoriosos(raiz):
    heroes = {}  

    def contar_victorias(raiz):
        nonlocal heroes
        if raiz is not None:
            if raiz.derrotada_por:
                for heroe in raiz.derrotada_por:
                    if heroe in heroes:
                        heroes[heroe] += 1
                    else:
                        heroes[heroe] = 1
            contar_victorias(raiz.izquierdo)
            contar_victorias(raiz.derecho)

    contar_victorias(raiz)

    heroes_ordenados = sorted(heroes.items(), key=lambda x: x[1], reverse=True)

    return heroes_ordenados[:3]

def listar_criaturas_derrotadas_por_heracles(raiz):
    criaturas_derrotadas = []

    def buscar_criaturas_heracles(raiz):
        if raiz is not None:
            if raiz.derrotada_por and "Heracles" in raiz.derrotada_por:
                criaturas_derrotadas.append(raiz.nombre)
            buscar_criaturas_heracles(raiz.izquierdo)
            buscar_criaturas_heracles(raiz.derecho)

    buscar_criaturas_heracles(raiz)

    return criaturas_derrotadas

def listar_criaturas_no_derrotadas(raiz):
    criaturas_no_derrotadas = []

    def buscar_criaturas_no_derrotadas(raiz):
        if raiz is not None:
            if not raiz.derrotada_por:
                criaturas_no_derrotadas.append(raiz.nombre)
            buscar_criaturas_no_derrotadas(raiz.izquierdo)
            buscar_criaturas_no_derrotadas(raiz.derecho)

    buscar_criaturas_no_derrotadas(raiz)

    return criaturas_no_derrotadas

def modificar_criaturas_atrapadas_por_heracles(raiz):
    def marcar_criaturas_atrapadas(raiz):
        if raiz is not None:
            if raiz.nombre in ["Cerbero", "Toro de Creta", "Cierva Cerinea", "Jabalí de Erimanto"]:
                if not raiz.capturada:
                    raiz.capturada = "Heracles"
            marcar_criaturas_atrapadas(raiz.izquierdo)
            marcar_criaturas_atrapadas(raiz.derecho)

    marcar_criaturas_atrapadas(raiz)

def busqueda_por_coincidencia(raiz, clave):
    coincidencias = []

    def buscar_coincidencias(raiz):
        if raiz is not None:
            if clave in raiz.nombre:
                coincidencias.append(raiz.nombre)
            buscar_coincidencias(raiz.izquierdo)
            buscar_coincidencias(raiz.derecho)

    buscar_coincidencias(raiz)

    return coincidencias

def eliminar_basilisco_y_sirenas(raiz):
    def eliminar_nodo(raiz, nombre):
        if raiz is None:
            return raiz
        if nombre < raiz.nombre:
            raiz.izquierdo = eliminar_nodo(raiz.izquierdo, nombre)
        elif nombre > raiz.nombre:
            raiz.derecho = eliminar_nodo(raiz.derecho, nombre)
        else:
            if raiz.izquierdo is None:
                return raiz.derecho
            elif raiz.derecho is None:
                return raiz.izquierdo
            raiz.nombre = min_valor_nodo(raiz.derecho)
            raiz.derecho = eliminar_nodo(raiz.derecho, raiz.nombre)
        return raiz

    def min_valor_nodo(raiz):
        actual = raiz
        while actual.izquierdo is not None:
            actual = actual.izquierdo
        return actual.nombre

    raiz = eliminar_nodo(raiz, "Basilisco")
    raiz = eliminar_nodo(raiz, "Sirenas")

def modificar_aves_del_estinfalo(raiz):
    def modificar_nodo(raiz, nombre):
        if raiz is None:
            return raiz
        if nombre < raiz.nombre:
            raiz.izquierdo = modificar_nodo(raiz.izquierdo, nombre)
        elif nombre > raiz.nombre:
            raiz.derecho = modificar_nodo(raiz.derecho, nombre)
        else:
            if not raiz.descripcion:
                raiz.descripcion = "Heracles derrotó a varias de estas aves."
        return raiz

    raiz = modificar_nodo(raiz, "Aves del Estínfalo")

def modificar_nombre_ladon(raiz):
    def modificar_nodo(raiz, nombre):
        if raiz is None:
            return raiz
        if nombre < raiz.nombre:
            raiz.izquierdo = modificar_nodo(raiz.izquierdo, nombre)
        elif nombre > raiz.nombre:
            raiz.derecho = modificar_nodo(raiz.derecho, nombre)
        else:
            raiz.nombre = "Dragón Ladón"
        return raiz

    raiz = modificar_nodo(raiz, "Ladón")

def listado_por_nivel(raiz):
    if raiz is None:
        return

    nivel_actual = 0
    cola = [(raiz, nivel_actual)]

    while cola:
        nodo, nivel = cola.pop(0)

        if nivel > nivel_actual:
            nivel_actual = nivel
            print()

        print(f"Nivel {nivel}: {nodo.nombre}", end=", ")

        if nodo.izquierdo:
            cola.append((nodo.izquierdo, nivel + 1))
        if nodo.derecho:
            cola.append((nodo.derecho, nivel + 1))

def mostrar_criaturas_capturadas_por_heracles(raiz, criaturas_heracles):
    if raiz is not None:
        if raiz.nombre in criaturas_heracles:
            if raiz.capturada:
                print(f"{raiz.nombre} fue capturada por {raiz.capturada}")
        mostrar_criaturas_capturadas_por_heracles(raiz.izquierdo, criaturas_heracles)
        mostrar_criaturas_capturadas_por_heracles(raiz.derecho, criaturas_heracles)

raiz = None

criaturas = [
    NodoCriatura("Ceto"),
    NodoCriatura("Cerda de Cromión", ["Teseo"]),
    NodoCriatura("Tifón", ["Zeus"]),
    NodoCriatura("Ortro", ["Heracles"]),
    NodoCriatura("Equidna", ["Argos Panoptes"]),
    NodoCriatura("Toro de Creta", ["Teseo"]),
    NodoCriatura("Dino"),
    NodoCriatura("Jabalí de Calidón", ["Atalanta"]),
    NodoCriatura("Pefredo"),
    NodoCriatura("Carcinos"),
    NodoCriatura("Enio"),
    NodoCriatura("Gerión", ["Heracles"]),
    NodoCriatura("Escila"),
    NodoCriatura("Cloto"),
    NodoCriatura("Caribdis"),
    NodoCriatura("Láquesis"),
    NodoCriatura("Euríale"),
    NodoCriatura("Átropos"),
    NodoCriatura("Esteno"),
    NodoCriatura("Minotauro de Creta", ["Teseo"]),
    NodoCriatura("Medusa", ["Perseo"]),
    NodoCriatura("Harpías"),
    NodoCriatura("Ladón", ["Heracles"]),
    NodoCriatura("Argos Panoptes", ["Hermes"]),
    NodoCriatura("Águila del Cáucaso"),
    NodoCriatura("Aves del Estínfalo"),
    NodoCriatura("Quimera", ["Belerofonte"]),
    NodoCriatura("Talos", ["Medea"]),
    NodoCriatura("Hidra de Lerna", ["Heracles"]),
    NodoCriatura("Sirenas"),
    NodoCriatura("León de Nemea", ["Heracles"]),
    NodoCriatura("Pitón", ["Apolo"]),
    NodoCriatura("Esfinge", ["Edipo"]),
    NodoCriatura("Cierva de Cerinea"),
    NodoCriatura("Dragón de la Cólquida"),
    NodoCriatura("Basilisco"),
    NodoCriatura("Cerbero"),
    NodoCriatura("Jabalí de Erimanto"),
]

for criatura in criaturas:
    raiz = insertar_criatura(raiz, criatura)
    
print("a. Listado inorden de las criaturas y quienes las derrotaron:")
listar_inorden_con_derrotada(raiz)

cargar_descripcion(raiz, "Talos", "Criatura de bronce que protegía la isla de Creta")

print("\nc. Información de la criatura Talos:")
mostrar_informacion_criatura(raiz, "Talos")

print("\nd. Los 3 héroes o dioses más victoriosos:")
heroes_victoriosos = heroes_mas_victoriosos(raiz)
for i, (heroe, victorias) in enumerate(heroes_victoriosos, 1):
    print(f"{i}. {heroe} ({victorias} victorias)")

print("\ne. Criaturas derrotadas por Heracles:")
criaturas_derrotadas_heracles = listar_criaturas_derrotadas_por_heracles(raiz)
for criatura in criaturas_derrotadas_heracles:
    print(criatura)

print("\nf. Criaturas no derrotadas:")
criaturas_no_derrotadas = listar_criaturas_no_derrotadas(raiz)
for criatura in criaturas_no_derrotadas:
    print(criatura)

modificar_criaturas_atrapadas_por_heracles(raiz)

print("\ng. Búsqueda por coincidencia (nombre que contiene 'ro'):")
coincidencias = busqueda_por_coincidencia(raiz, "ro")
for coincidencia in coincidencias:
    print(coincidencia)

eliminar_basilisco_y_sirenas(raiz)

modificar_aves_del_estinfalo(raiz)

modificar_nombre_ladon(raiz)

print("\nm. Listado por nivel del árbol:")
listado_por_nivel(raiz)

print("\nn. Criaturas capturadas por Heracles:")
criaturas_heracles = [
    "Talos",
    "Toro de Creta",
    "Cierva Cerinea",
    "Jabalí de Erimanto",
    "Hidra de Lerna",
    "León de Nemea",
]
mostrar_criaturas_capturadas_por_heracles(raiz, criaturas_heracles)

class NodoJedi:
    def __init__(self, nombre, especie, nacimiento, color_sable, ranking, maestros):
        self.nombre = nombre
        self.especie = especie
        self.nacimiento = nacimiento
        self.color_sable = color_sable
        self.ranking = ranking
        self.maestros = maestros
        self.izquierdo = None
        self.derecho = None

# Crear objetos Jedi
jedi1 = NodoJedi("Yoda", "Unknown", "896 BBY", "verde", "Jedi Master", ["None"])
jedi2 = NodoJedi("Luke Skywalker", "Human", "19 BBY", "verde", "Jedi Knight", ["Obi-Wan Kenobi", "Yoda"])
jedi3 = NodoJedi("Obi-Wan Kenobi", "Human", "57 BBY", "azul", "Jedi Master", ["Qui-Gon Jinn"])
jedi4 = NodoJedi("Qui-Gon Jinn", "Human", "92 BBY", "verde", "Jedi Master", ["None"])
jedi5 = NodoJedi("Anakin Skywalker", "Human", "41 BBY", "azul", "Jedi Knight", ["Obi-Wan Kenobi"])
jedi6 = NodoJedi("Ahsoka Tano", "Togruta", "36 BBY", "verde", "Jedi Knight", ["Anakin Skywalker"])
# Agrega más Jedi aquí según tus necesidades

# Función para insertar un Jedi en el árbol por nombre
def insertar_por_nombre(raiz, jedi):
    if raiz is None:
        return jedi
    if jedi.nombre < raiz.nombre:
        raiz.izquierdo = insertar_por_nombre(raiz.izquierdo, jedi)
    else:
        raiz.derecho = insertar_por_nombre(raiz.derecho, jedi)
    return raiz

# Función para insertar un Jedi en el árbol por ranking
def insertar_por_ranking(raiz, jedi):
    if raiz is None:
        return jedi
    if jedi.ranking < raiz.ranking:
        raiz.izquierdo = insertar_por_ranking(raiz.izquierdo, jedi)
    else:
        raiz.derecho = insertar_por_ranking(raiz.derecho, jedi)
    return raiz

# Función para insertar un Jedi en el árbol por especie
def insertar_por_especie(raiz, jedi):
    if raiz is None:
        return jedi
    if jedi.especie < raiz.especie:
        raiz.izquierdo = insertar_por_especie(raiz.izquierdo, jedi)
    else:
        raiz.derecho = insertar_por_especie(raiz.derecho, jedi)
    return raiz

# Crear los árboles de acceso por nombre, ranking y especie e insertar los Jedi
raiz_nombre = None
raiz_ranking = None
raiz_especie = None

jedis = [jedi1, jedi2, jedi3, jedi4, jedi5, jedi6]  # Agrega más Jedi a esta lista según tus necesidades

for jedi in jedis:
    raiz_nombre = insertar_por_nombre(raiz_nombre, jedi)
    raiz_ranking = insertar_por_ranking(raiz_ranking, jedi)
    raiz_especie = insertar_por_especie(raiz_especie, jedi)

# Funciones adicionales para el código original

# Función para realizar un barrido inorden del árbol por nombre y ranking
def barrido_inorden_nombre(raiz):
    if raiz is not None:
        barrido_inorden_nombre(raiz.izquierdo)
        print("Nombre:", raiz.nombre, "Ranking:", raiz.ranking)
        barrido_inorden_nombre(raiz.derecho)

def barrido_inorden_ranking(raiz):
    if raiz is not None:
        barrido_inorden_ranking(raiz.izquierdo)
        print("Nombre:", raiz.nombre, "Ranking:", raiz.ranking)
        barrido_inorden_ranking(raiz.derecho)

# Función para realizar un barrido por nivel del árbol por ranking y especie
def barrido_por_nivel(raiz):
    if raiz is None:
        return
    cola = [raiz]
    while cola:
        nodo = cola.pop(0)
        print("Nombre:", nodo.nombre, "Ranking:", nodo.ranking, "Especie:", nodo.especie)
        if nodo.izquierdo:
            cola.append(nodo.izquierdo)
        if nodo.derecho:
            cola.append(nodo.derecho)

# Función para mostrar toda la información de un Jedi
def mostrar_informacion_jedi(raiz, nombre):
    if raiz is not None:
        if raiz.nombre == nombre:
            print("Nombre:", raiz.nombre)
            print("Especie:", raiz.especie)
            print("Año de nacimiento:", raiz.nacimiento)
            print("Color de sable de luz:", raiz.color_sable)
            print("Ranking:", raiz.ranking)
            print("Maestros:", ", ".join(raiz.maestros))
        mostrar_informacion_jedi(raiz.izquierdo, nombre)
        mostrar_informacion_jedi(raiz.derecho, nombre)

# Función para mostrar todos los Jedi con ranking "Jedi Master"
def mostrar_jedi_master(raiz):
    if raiz is not None:
        mostrar_jedi_master(raiz.izquierdo)
        if raiz.ranking == "Jedi Master":
            print("Nombre:", raiz.nombre, "Ranking:", raiz.ranking)
        mostrar_jedi_master(raiz.derecho)

# Función para listar todos los Jedi que utilizaron sable de luz color verde
def listar_jedi_color_verde(raiz):
    if raiz is not None:
        listar_jedi_color_verde(raiz.izquierdo)
        if raiz.color_sable == "verde":
            print("Nombre:", raiz.nombre, "Color de sable de luz:", raiz.color_sable)
        listar_jedi_color_verde(raiz.derecho)

# Función para listar todos los Jedi cuyos maestros están en el archivo
def listar_jedi_con_maestros(raiz, maestros):
    if raiz is not None:
        listar_jedi_con_maestros(raiz.izquierdo, maestros)
        if any(maestro in raiz.maestros for maestro in maestros):
            print("Nombre:", raiz.nombre, "Maestros:", ", ".join(raiz.maestros))
        listar_jedi_con_maestros(raiz.derecho, maestros)

# Función para mostrar todos los Jedi de especie "Togruta" o "Cerean"
def mostrar_jedi_especies(raiz, especie1, especie2):
    if raiz is not None:
        mostrar_jedi_especies(raiz.izquierdo, especie1, especie2)
        if raiz.especie == especie1 or raiz.especie == especie2:
            print("Nombre:", raiz.nombre, "Especie:", raiz.especie)
        mostrar_jedi_especies(raiz.derecho, especie1, especie2)

# Función para listar los Jedi que comienzan con la letra A o contienen un "-"
def listar_jedi_letra_A_o_guion(raiz):
    if raiz is not None:
        listar_jedi_letra_A_o_guion(raiz.izquierdo)
        if raiz.nombre.startswith("A") or "-" in raiz.nombre:
            print("Nombre:", raiz.nombre)
        listar_jedi_letra_A_o_guion(raiz.derecho)

# Realizar las operaciones solicitadas

print("Barrido Inorden por Nombre:")
barrido_inorden_nombre(raiz_nombre)

print("\nBarrido Inorden por Ranking:")
barrido_inorden_ranking(raiz_ranking)

print("\nBarrido por Nivel por Ranking y Especie:")
barrido_por_nivel(raiz_ranking)
barrido_por_nivel(raiz_especie)

print("\nInformación de Yoda:")
mostrar_informacion_jedi(raiz_nombre, "Yoda")

print("\nInformación de Luke Skywalker:")
mostrar_informacion_jedi(raiz_nombre, "Luke Skywalker")

print("\nJedi con ranking 'Jedi Master':")
mostrar_jedi_master(raiz_ranking)

print("\nJedi con sable de luz color verde:")
listar_jedi_color_verde(raiz_nombre)

maestros = set(["Obi-Wan Kenobi", "Qui-Gon Jinn"])
print("\nJedi cuyos maestros están en el archivo:")
listar_jedi_con_maestros(raiz_nombre, maestros)

print("\nJedi de especie 'Togruta' o 'Cerean':")
mostrar_jedi_especies(raiz_especie, "Togruta", "Cerean")

print("\nJedi que comienzan con la letra A o contienen un '-':")
listar_jedi_letra_A_o_guion(raiz_nombre)

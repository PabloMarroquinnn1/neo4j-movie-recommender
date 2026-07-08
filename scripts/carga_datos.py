from neo4j import GraphDatabase
from faker import Faker
import random
import csv
import os

fake = Faker('es_MX')
URI = "bolt://localhost:7687"
AUTH = ("neo4j", "peliculas123")

driver = GraphDatabase.driver(URI, auth=AUTH)

DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

# ── Datos base ──────────────────────────────────────────────────────
GENEROS = [
    ("Accion", "Peliculas con secuencias de accion y adrenalina"),
    ("Comedia", "Peliculas con humor y situaciones comicas"),
    ("Drama", "Peliculas con conflictos emocionales profundos"),
    ("Terror", "Peliculas de miedo y suspenso"),
    ("Ciencia Ficcion", "Peliculas de tecnologia y futuros alternativos"),
    ("Romance", "Peliculas centradas en relaciones amorosas"),
    ("Thriller", "Peliculas de suspenso e intriga"),
    ("Animacion", "Peliculas animadas para todas las edades"),
    ("Documental", "Peliculas basadas en hechos reales"),
    ("Fantasia", "Peliculas con elementos magicos y mundos imaginarios"),
    ("Aventura", "Peliculas de exploracion y travesias"),
    ("Misterio", "Peliculas con enigmas por resolver"),
    ("Historia", "Peliculas basadas en eventos historicos"),
    ("Musical", "Peliculas con canciones y coreografias"),
    ("Deportes", "Peliculas sobre competencias y atletas"),
]

TITULOS_PELICULAS = [
    "El ultimo viaje", "Sombras del pasado", "La gran aventura", "Codigo rojo",
    "Entre dos mundos", "El despertar", "La tormenta perfecta", "Mas alla del horizonte",
    "El secreto del lago", "Voces en la oscuridad", "El guardian eterno", "La caida",
    "Tiempo prestado", "El ultimo testigo", "Luz y oscuridad", "El regreso",
    "La promesa rota", "En el limite", "El camino perdido", "La verdad oculta",
    "Sin salida", "El precio de la gloria", "Fragmentos", "La decision",
    "El ultimo heroe", "Mas fuerte que el destino", "La noche infinita", "Origen",
    "El peso del silencio", "La frontera", "Renacimiento", "El eco del pasado",
    "La ultima oportunidad", "Sueños rotos", "El laberinto", "La batalla final",
    "Instinto", "El prisionero", "La sombra del mal", "Conexion fatal",
    "El elegido", "Mas alla del bien", "La trampa", "El punto de quiebre",
    "Sangre fria", "El espejo roto", "La redencion", "Tierra de nadie",
    "El horizonte perdido", "La conspiración", "Doble identidad", "El umbral",
    "Fuera de control", "La señal", "El ultimo acto", "Tormenta de fuego",
    "La herencia maldita", "Punto ciego", "El cazador", "La maldicion",
    "Sin rastro", "El codigo olvidado", "La venganza", "Oscuridad total",
    "El infiltrado", "La zona roja", "Colapso", "El testigo silencioso",
    "La fuga", "Abismo", "El oraculo", "La marca del diablo",
    "Impacto", "El ultimo recurso", "La pesadilla", "Zona de guerra",
    "El legado", "La trampa mortal", "Detonacion", "El tiempo se acaba",
    "La oscuridad interior", "Furia imparable", "El punto final", "La amenaza",
    "Sin identidad", "El precio del poder", "La caida libre", "Explosion",
    "El juego mortal", "La red", "Bajo cero", "El silencio roto",
    "La ultima frontera", "Sombra y luz", "El destino marcado", "La fuerza del mal",
    "Colision", "El guerrero", "La verdad prohibida", "Zona de peligro",
    "El infierno verde", "La persecucion", "Torbellino", "La segunda oportunidad",
    "Sin memoria", "El proyecto secreto", "La cadena rota", "Insurreccion",
    "El ladrón de sueños", "La profecia", "Cero absoluto", "El guardian",
    "La mente oscura", "Desolacion", "El ultimo comando", "La isla perdida",
    "Sin piedad", "El cruce", "La tela de araña", "Evasion total",
    "El monstruo interior", "La guerra fria", "Punto de no retorno", "El enviado",
    "La venganza perfecta", "Caos total", "El vigilante", "La clave perdida",
    "Sin escape", "El vacio", "La sombra del pasado", "Colisión de mundos",
    "El ultimo susurro", "La bestia", "Territorio enemigo", "El riesgo calculado",
    "La oscuridad eterna", "Fuga imposible", "El precio de la verdad", "La señal perdida",
    "Sin retorno", "El despertador", "La alianza", "Implosion",
    "El mensajero", "La rueda del destino", "Punto critico", "El ultimo grito",
    "La sombra del futuro", "Sin fronteras", "El error fatal", "La noche de los lobos",
    "Zona prohibida", "El cazador de almas", "La espiral", "Derrumbe",
    "El tercer ojo", "La ultima batalla", "Sin cuartel", "El abismo oscuro",
    "La caja de pandora", "Golpe mortal", "El testamento", "La maquina del tiempo",
    "Sin salida aparente", "El poder oculto", "La amenaza silenciosa", "Descenso",
    "El ultimo dia", "La fuerza interior", "Sin tregua", "El maestro del engano",
    "La trampa final", "Combustion", "El observador", "La red de mentiras",
    "Sin identidad conocida", "El ultimo paso", "La noche sin fin", "Fractura",
    "El espiritu guerrero", "La zona gris", "Sin piedad ni gloria", "El codigo negro",
    "La ultima esperanza", "Tormenta interior", "El regreso del mal", "La conexion",
    "Sin nombre", "El doble juego", "La fuerza del destino", "Impacto final",
    "El mundo al reves", "La guerra de sombras", "Punto sin retorno", "El espejo oscuro",
    "La voz del silencio", "Sin limite", "El cazador solitario", "La herida abierta",
    "Zona de exclusion", "El precio del miedo", "La noche del cazador", "Descarga",
    "El tiempo muerto", "La confusion total", "Sin rumbo", "El detonador",
    "La primera linea", "Caida libre", "El ultimo tren", "La mente en blanco",
]

NACIONALIDADES = ["Mexicano", "Argentino", "Colombiano", "Espanol", "Estadounidense",
                  "Brasileno", "Chileno", "Peruano", "Venezolano", "Frances",
                  "Italiano", "Aleman", "Japones", "Coreano", "Britanico"]

PAISES = ["Mexico", "Argentina", "Colombia", "Espana", "Estados Unidos",
          "Brasil", "Chile", "Peru", "Venezuela", "Francia",
          "Italia", "Alemania", "Japon", "Corea del Sur", "Reino Unido",
          "Guatemala", "Costa Rica", "Panama", "Ecuador", "Bolivia"]

print("Generando datos...")

# ── Generar usuarios ────────────────────────────────────────────────
usuarios = []
emails_usados = set()
for i in range(500):
    while True:
        email = fake.email()
        if email not in emails_usados:
            emails_usados.add(email)
            break
    usuarios.append({
        "nombre": fake.name(),
        "email": email,
        "edad": random.randint(15, 70),
        "pais": random.choice(PAISES)
    })

with open(f"{DATA_DIR}/usuarios.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["nombre", "email", "edad", "pais"])
    writer.writeheader()
    writer.writerows(usuarios)

print(f"500 usuarios generados")

# ── Generar actores ─────────────────────────────────────────────────
actores = []
nombres_actores = set()
for i in range(100):
    while True:
        nombre = fake.name()
        if nombre not in nombres_actores:
            nombres_actores.add(nombre)
            break
    actores.append({
        "nombre": nombre,
        "fecha_nacimiento": str(fake.date_of_birth(minimum_age=20, maximum_age=80)),
        "nacionalidad": random.choice(NACIONALIDADES)
    })

with open(f"{DATA_DIR}/actores.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["nombre", "fecha_nacimiento", "nacionalidad"])
    writer.writeheader()
    writer.writerows(actores)

print(f"100 actores generados")

# ── Generar directores ──────────────────────────────────────────────
directores = []
nombres_directores = set()
for i in range(50):
    while True:
        nombre = fake.name()
        if nombre not in nombres_directores and nombre not in nombres_actores:
            nombres_directores.add(nombre)
            break
    directores.append({
        "nombre": nombre,
        "fecha_nacimiento": str(fake.date_of_birth(minimum_age=30, maximum_age=80)),
        "nacionalidad": random.choice(NACIONALIDADES)
    })

with open(f"{DATA_DIR}/directores.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["nombre", "fecha_nacimiento", "nacionalidad"])
    writer.writeheader()
    writer.writerows(directores)

print(f"50 directores generados")

# ── Generar generos ─────────────────────────────────────────────────
with open(f"{DATA_DIR}/generos.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["nombre", "descripcion"])
    writer.writeheader()
    for nombre, desc in GENEROS:
        writer.writerow({"nombre": nombre, "descripcion": desc})

print(f"15 generos generados")

# ── Generar peliculas ───────────────────────────────────────────────
peliculas = []
for i in range(200):
    peliculas.append({
        "titulo": TITULOS_PELICULAS[i],
        "anio": random.randint(1990, 2024),
        "duracion": random.randint(80, 180),
        "sinopsis": fake.text(max_nb_chars=200)
    })

with open(f"{DATA_DIR}/peliculas.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["titulo", "anio", "duracion", "sinopsis"])
    writer.writeheader()
    writer.writerows(peliculas)

print(f"200 peliculas generadas")

# ── Generar relaciones ──────────────────────────────────────────────
emails = [u["email"] for u in usuarios]
titulos = [p["titulo"] for p in peliculas]
nombres_gen = [g[0] for g in GENEROS]
nombres_act = [a["nombre"] for a in actores]
nombres_dir = [d["nombre"] for d in directores]

# Pelicula - Genero
pel_gen = []
for titulo in titulos:
    for g in random.sample(nombres_gen, random.randint(1, 3)):
        pel_gen.append({"titulo": titulo, "genero": g})

with open(f"{DATA_DIR}/pelicula_genero.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["titulo", "genero"])
    writer.writeheader()
    writer.writerows(pel_gen)

# Actor - Pelicula
personajes = ["El heroe", "El villano", "El amigo", "La protagonista", "El mentor",
              "El traidor", "La detective", "El cientifico", "La madre", "El lider"]
act_pel = []
usados = set()
for titulo in titulos:
    for actor in random.sample(nombres_act, random.randint(2, 5)):
        key = (actor, titulo)
        if key not in usados:
            usados.add(key)
            act_pel.append({
                "actor": actor,
                "titulo": titulo,
                "personaje": random.choice(personajes)
            })

with open(f"{DATA_DIR}/actor_pelicula.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["actor", "titulo", "personaje"])
    writer.writeheader()
    writer.writerows(act_pel)

# Director - Pelicula
dir_pel = []
for titulo in titulos:
    dir_pel.append({"director": random.choice(nombres_dir), "titulo": titulo})

with open(f"{DATA_DIR}/director_pelicula.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["director", "titulo"])
    writer.writeheader()
    writer.writerows(dir_pel)

# Usuario - Califico
calificaciones = []
usados_cal = set()
for email in emails:
    for titulo in random.sample(titulos, random.randint(3, 15)):
        key = (email, titulo)
        if key not in usados_cal:
            usados_cal.add(key)
            calificaciones.append({
                "email": email,
                "titulo": titulo,
                "puntuacion": random.randint(1, 5),
                "fecha": str(fake.date_between(start_date="-3y", end_date="today")),
                "comentario": fake.sentence()
            })

with open(f"{DATA_DIR}/calificaciones.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["email", "titulo", "puntuacion", "fecha", "comentario"])
    writer.writeheader()
    writer.writerows(calificaciones)

# Usuario - Vio
vistas = []
usados_vis = set()
for email in emails:
    for titulo in random.sample(titulos, random.randint(5, 20)):
        key = (email, titulo)
        if key not in usados_vis:
            usados_vis.add(key)
            vistas.append({
                "email": email,
                "titulo": titulo,
                "fecha_visualizacion": str(fake.date_between(start_date="-3y", end_date="today")),
                "completo": random.choice(["true", "false"])
            })

with open(f"{DATA_DIR}/vistas.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["email", "titulo", "fecha_visualizacion", "completo"])
    writer.writeheader()
    writer.writerows(vistas)

# Usuario - Amigo
amistades = []
usados_am = set()
for email in emails:
    amigos = random.sample([e for e in emails if e != email], random.randint(2, 8))
    for amigo in amigos:
        key = tuple(sorted([email, amigo]))
        if key not in usados_am:
            usados_am.add(key)
            amistades.append({
                "email1": email,
                "email2": amigo,
                "fecha_amistad": str(fake.date_between(start_date="-5y", end_date="today"))
            })

with open(f"{DATA_DIR}/amistades.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["email1", "email2", "fecha_amistad"])
    writer.writeheader()
    writer.writerows(amistades)

# Usuario - Le gusta genero
le_gusta = []
usados_lg = set()
for email in emails:
    for genero in random.sample(nombres_gen, random.randint(2, 5)):
        key = (email, genero)
        if key not in usados_lg:
            usados_lg.add(key)
            le_gusta.append({
                "email": email,
                "genero": genero,
                "nivel_interes": random.randint(1, 5)
            })

with open(f"{DATA_DIR}/le_gusta.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["email", "genero", "nivel_interes"])
    writer.writeheader()
    writer.writerows(le_gusta)

print("Todos los CSVs generados. Cargando en Neo4j...")

# ── Cargar en Neo4j ─────────────────────────────────────────────────
def cargar(query, archivo, descripcion):
    with driver.session() as session:
        result = session.run(query)
        summary = result.consume()
        print(f"{descripcion}: {summary.counters}")

BASE = "file:///usuarios.csv"

cargar("""
LOAD CSV WITH HEADERS FROM 'file:///usuarios.csv' AS row
MERGE (u:Usuario {email: row.email})
SET u.nombre = row.nombre,
    u.edad = toInteger(row.edad),
    u.pais = row.pais
""", "usuarios.csv", "Usuarios")

cargar("""
LOAD CSV WITH HEADERS FROM 'file:///actores.csv' AS row
MERGE (a:Actor {nombre: row.nombre})
SET a.fecha_nacimiento = row.fecha_nacimiento,
    a.nacionalidad = row.nacionalidad
""", "actores.csv", "Actores")

cargar("""
LOAD CSV WITH HEADERS FROM 'file:///directores.csv' AS row
MERGE (d:Director {nombre: row.nombre})
SET d.fecha_nacimiento = row.fecha_nacimiento,
    d.nacionalidad = row.nacionalidad
""", "directores.csv", "Directores")

cargar("""
LOAD CSV WITH HEADERS FROM 'file:///generos.csv' AS row
MERGE (g:Genero {nombre: row.nombre})
SET g.descripcion = row.descripcion
""", "generos.csv", "Generos")

cargar("""
LOAD CSV WITH HEADERS FROM 'file:///peliculas.csv' AS row
MERGE (p:Pelicula {titulo: row.titulo})
SET p.anio = toInteger(row.anio),
    p.duracion = toInteger(row.duracion),
    p.sinopsis = row.sinopsis
""", "peliculas.csv", "Peliculas")

cargar("""
LOAD CSV WITH HEADERS FROM 'file:///pelicula_genero.csv' AS row
MATCH (p:Pelicula {titulo: row.titulo})
MATCH (g:Genero {nombre: row.genero})
MERGE (p)-[:PERTENECE_A]->(g)
""", "pelicula_genero.csv", "Pelicula-Genero")

cargar("""
LOAD CSV WITH HEADERS FROM 'file:///actor_pelicula.csv' AS row
MATCH (a:Actor {nombre: row.actor})
MATCH (p:Pelicula {titulo: row.titulo})
MERGE (a)-[r:ACTUO_EN {personaje: row.personaje}]->(p)
""", "actor_pelicula.csv", "Actor-Pelicula")

cargar("""
LOAD CSV WITH HEADERS FROM 'file:///director_pelicula.csv' AS row
MATCH (d:Director {nombre: row.director})
MATCH (p:Pelicula {titulo: row.titulo})
MERGE (d)-[:DIRIGIO]->(p)
""", "director_pelicula.csv", "Director-Pelicula")

cargar("""
LOAD CSV WITH HEADERS FROM 'file:///calificaciones.csv' AS row
MATCH (u:Usuario {email: row.email})
MATCH (p:Pelicula {titulo: row.titulo})
MERGE (u)-[r:CALIFICO {fecha: row.fecha}]->(p)
SET r.puntuacion = toInteger(row.puntuacion),
    r.comentario = row.comentario
""", "calificaciones.csv", "Calificaciones")

cargar("""
LOAD CSV WITH HEADERS FROM 'file:///vistas.csv' AS row
MATCH (u:Usuario {email: row.email})
MATCH (p:Pelicula {titulo: row.titulo})
MERGE (u)-[r:VIO {fecha_visualizacion: row.fecha_visualizacion}]->(p)
SET r.completo = (row.completo = 'true')
""", "vistas.csv", "Vistas")

cargar("""
LOAD CSV WITH HEADERS FROM 'file:///amistades.csv' AS row
MATCH (u1:Usuario {email: row.email1})
MATCH (u2:Usuario {email: row.email2})
MERGE (u1)-[r:ES_AMIGO_DE {fecha_amistad: row.fecha_amistad}]->(u2)
""", "amistades.csv", "Amistades")

cargar("""
LOAD CSV WITH HEADERS FROM 'file:///le_gusta.csv' AS row
MATCH (u:Usuario {email: row.email})
MATCH (g:Genero {nombre: row.genero})
MERGE (u)-[r:LE_GUSTA]->(g)
SET r.nivel_interes = toInteger(row.nivel_interes)
""", "le_gusta.csv", "Le_Gusta")

driver.close()
print("Carga completa.")
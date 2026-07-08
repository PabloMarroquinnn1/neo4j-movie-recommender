// ============================================================
// Consulta 6: Peliculas mas populares de un genero especifico
// ============================================================
// Como usar:
// 1. Abrir Neo4j Browser en http://localhost:7474
// 2. Copiar y pegar esta consulta
// 3. Reemplazar el nombre del genero segun necesidad
//
// Generos disponibles:
// Accion, Comedia, Drama, Terror, Ciencia Ficcion, Romance,
// Thriller, Animacion, Documental, Fantasia, Aventura,
// Misterio, Historia, Musical, Deportes
// ============================================================

MATCH (u:Usuario)-[:VIO]->(p:Pelicula)-[:PERTENECE_A]->(g:Genero)
WHERE g.nombre = 'Accion'
RETURN p.titulo, count(u) as visualizaciones
ORDER BY visualizaciones DESC
LIMIT 10

// ============================================================
// Consulta de recomendacion inteligente basada en amigos
// Peliculas que los amigos calificaron bien y el usuario
// todavia no ha visto ni calificado
// ============================================================

// MATCH (u:Usuario {email: 'nayeliroldan@example.com'})-[:ES_AMIGO_DE]-(amigo:Usuario)-[c:CALIFICO]->(p:Pelicula)
// WHERE c.puntuacion >= 4
// AND NOT (u)-[:VIO]->(p)
// AND NOT (u)-[:CALIFICO]->(p)
// RETURN p.titulo,
//        avg(c.puntuacion) as puntuacion_amigos,
//        count(amigo) as amigos_que_la_vieron
// ORDER BY puntuacion_amigos DESC, amigos_que_la_vieron DESC
// LIMIT 10

// ============================================================
// Analisis de redes: Peliculas altamente conectadas
// Peliculas con mas actores y directores reconocidos
// ============================================================

// MATCH (p:Pelicula)
// OPTIONAL MATCH (a:Actor)-[:ACTUO_EN]->(p)
// OPTIONAL MATCH (d:Director)-[:DIRIGIO]->(p)
// RETURN p.titulo,
//        count(DISTINCT a) as actores,
//        count(DISTINCT d) as directores,
//        count(DISTINCT a) + count(DISTINCT d) as conexiones_totales
// ORDER BY conexiones_totales DESC
// LIMIT 10

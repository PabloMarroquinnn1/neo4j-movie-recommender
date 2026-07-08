// ============================================================
// Consulta 1: Peliculas calificadas por un usuario con
// puntuacion mayor a 4
// ============================================================
// Como usar:
// 1. Abrir Neo4j Browser en http://localhost:7474
// 2. Copiar y pegar esta consulta
// 3. Reemplazar el email con uno real del sistema
//
// Para obtener un email real ejecutar primero:
// MATCH (u:Usuario) RETURN u.email LIMIT 5
// ============================================================

MATCH (u:Usuario)-[c:CALIFICO]->(p:Pelicula)
WHERE u.email = 'nayeliroldan@example.com'
AND c.puntuacion > 4
RETURN p.titulo, c.puntuacion, c.fecha, c.comentario
ORDER BY c.puntuacion DESC

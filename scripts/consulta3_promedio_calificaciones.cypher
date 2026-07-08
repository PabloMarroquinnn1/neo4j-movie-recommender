// ============================================================
// Consulta 3: Promedio de calificaciones de una pelicula
// ============================================================
// Como usar:
// 1. Abrir Neo4j Browser en http://localhost:7474
// 2. Copiar y pegar esta consulta
// 3. Reemplazar el titulo con uno real del sistema
//
// Para obtener titulos reales ejecutar primero:
// MATCH (p:Pelicula) RETURN p.titulo LIMIT 10
// ============================================================

MATCH (u:Usuario)-[c:CALIFICO]->(p:Pelicula)
WHERE p.titulo = 'La batalla final'
RETURN p.titulo,
       avg(c.puntuacion) as promedio,
       count(c) as total_calificaciones

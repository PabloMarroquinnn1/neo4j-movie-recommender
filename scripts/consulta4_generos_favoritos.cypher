// ============================================================
// Consulta 4: Generos favoritos de un usuario basados
// en sus calificaciones
// Pablo Alejandro Marroquin Cutz - 202200214
// ============================================================
// Como usar:
// 1. Abrir Neo4j Browser en http://localhost:7474
// 2. Copiar y pegar esta consulta
// 3. Reemplazar el email con uno real del sistema
//
// Esta consulta atraviesa 3 nodos:
// Usuario -> Pelicula -> Genero
// El genero con mayor promedio es el favorito del usuario
// ============================================================

MATCH (u:Usuario)-[c:CALIFICO]->(p:Pelicula)-[:PERTENECE_A]->(g:Genero)
WHERE u.email = 'nayeliroldan@example.com'
RETURN g.nombre,
       avg(c.puntuacion) as promedio,
       count(c) as peliculas_calificadas
ORDER BY promedio DESC

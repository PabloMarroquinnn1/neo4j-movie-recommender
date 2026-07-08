// ============================================================
// Consulta 2: Peliculas que vieron los amigos de un usuario
// pero que el usuario aun no ha visto
// Pablo Alejandro Marroquin Cutz - 202200214
// ============================================================
// Como usar:
// 1. Abrir Neo4j Browser en http://localhost:7474
// 2. Copiar y pegar esta consulta
// 3. Reemplazar el email con uno real del sistema
//
// Nota: el patron -[:ES_AMIGO_DE]- sin flecha trata la
// amistad como bidireccional, buscando en ambas direcciones
// ============================================================

MATCH (u:Usuario)-[:ES_AMIGO_DE]-(amigo:Usuario)-[:VIO]->(p:Pelicula)
WHERE u.email = 'nayeliroldan@example.com'
AND NOT (u)-[:VIO]->(p)
RETURN DISTINCT p.titulo, p.anio, p.duracion
LIMIT 10

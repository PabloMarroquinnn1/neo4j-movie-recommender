// ============================================================
// Consulta 5: Ruta mas corta entre dos usuarios
// Grados de separacion en la red social
// Pablo Alejandro Marroquin Cutz - 202200214
// ============================================================
// Como usar:
// 1. Abrir Neo4j Browser en http://localhost:7474
// 2. Copiar y pegar esta consulta
// 3. Reemplazar ambos emails con emails reales del sistema
//
// Interpretacion del resultado:
// grados_de_separacion = 1 -> son amigos directos
// grados_de_separacion = 2 -> tienen un amigo en comun
// grados_de_separacion = 3+ -> conectados por intermediarios
// Sin resultado -> no estan conectados en la red
//
// Usa el algoritmo BFS (Breadth-First Search) de forma nativa
// ============================================================

MATCH (u1:Usuario {email: 'nayeliroldan@example.com'}),
      (u2:Usuario {email: 'abelardoalcala@example.com'})
MATCH path = shortestPath((u1)-[:ES_AMIGO_DE*]-(u2))
RETURN [n IN nodes(path) | n.nombre] as ruta,
       length(path) as grados_de_separacion

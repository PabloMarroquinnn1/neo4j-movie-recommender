// RecomendaDB: Constraints and indexes
// Run from Neo4j Browser at http://localhost:7474

CREATE CONSTRAINT usuario_email IF NOT EXISTS
FOR (u:Usuario) REQUIRE u.email IS UNIQUE;

CREATE CONSTRAINT pelicula_titulo IF NOT EXISTS
FOR (p:Pelicula) REQUIRE p.titulo IS UNIQUE;

CREATE CONSTRAINT genero_nombre IF NOT EXISTS
FOR (g:Genero) REQUIRE g.nombre IS UNIQUE;

CREATE CONSTRAINT actor_nombre IF NOT EXISTS
FOR (a:Actor) REQUIRE a.nombre IS UNIQUE;

CREATE CONSTRAINT director_nombre IF NOT EXISTS
FOR (d:Director) REQUIRE d.nombre IS UNIQUE;

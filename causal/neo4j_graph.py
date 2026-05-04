from neo4j import GraphDatabase

class Neo4jGraph:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def add_edge(self, src, dst, weight):
        with self.driver.session() as session:
            session.run(
                """
                MERGE (a:Event {name:$src})
                MERGE (b:Event {name:$dst})
                MERGE (a)-[r:CAUSES]->(b)
                SET r.weight = coalesce(r.weight,0) + $weight
                """,
                src=src, dst=dst, weight=weight
            )

    def get_root_causes(self):
        with self.driver.session() as session:
            result = session.run(
                """
                MATCH (n)
                RETURN n.name AS name, size((n)-->) AS score
                ORDER BY score DESC LIMIT 5
                """
            )
            return [r["name"] for r in result]
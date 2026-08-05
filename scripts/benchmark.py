from neo4j import GraphDatabase
import time

URI = "bolt+s://db-0317f2e2.databases.cognodb.com"
USERNAME = "cognodb"
PASSWORD = "8601477ce8fc1c46a6291e0b19d4c6f7"

driver = GraphDatabase.driver(
    URI,
    auth=(USERNAME, PASSWORD)
)

queries = {
    "count_nodes": """
        MATCH (n)
        RETURN count(n)
    """,

    "count_relationships": """
        MATCH ()-[r]->()
        RETURN count(r)
    """,

    "one_hop": """
        MATCH (u)-[]->(v)
        WHERE id(u)=2
        RETURN v
        LIMIT 20
    """
}

with driver.session() as session:

    for name, query in queries.items():

        start = time.time()

        result = session.run(query)

        list(result)

        end = time.time()

        print(
            name,
            ":",
            round((end - start) * 1000, 2),
            "ms"
        )

driver.close()
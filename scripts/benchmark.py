from neo4j import GraphDatabase
import time

URI = "bolt+s://db-0317f2e2.databases.cognodb.com"
USERNAME = "cognodb"
PASSWORD = "8601477ce8fc1c46a6291e0b19d4c6f7"

driver = GraphDatabase.driver(
    URI,
    auth=(USERNAME, PASSWORD)
)

query = """
MATCH (u)-[r]->(v)
WHERE id(u) = 2
RETURN id(v) AS connected_user
LIMIT 20
"""

start = time.time()

with driver.session() as session:
    result = session.run(query)

    print("Connected users:")

    for record in result:
        print(record["connected_user"])

end = time.time()

print("Execution time:", end - start, "seconds")

driver.close()
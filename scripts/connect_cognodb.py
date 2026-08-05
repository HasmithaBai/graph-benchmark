from neo4j import GraphDatabase

URI = "bolt+s://db-0317f2e2.databases.cognodb.com"
USERNAME = "cognodb"
PASSWORD = "8601477ce8fc1c46a6291e0b19d4c6f7"

driver = GraphDatabase.driver(
    URI,
    auth=(USERNAME, PASSWORD)
)

driver.verify_connectivity()

print("Connected successfully!")

driver.close()
from neo4j import GraphDatabase

URI = "YOUR_COGNODB_URI"
USERNAME = "YOUR_COGNODB_USERNAME"
PASSWORD = "YOUR_COGNODB_PASSWORD"

driver = GraphDatabase.driver(
    URI,
    auth=(USERNAME, PASSWORD)
)

driver.verify_connectivity()

print("Connected successfully!")

driver.close()

from neo4j import GraphDatabase
import pandas as pd

# Neo4j connection details

URI = "YOUR_NEO4J_URI"
USERNAME = "YOUR_NEO4J_USERNAME"
PASSWORD = "YOUR_NEO4J_PASSWORD"

# Connect to Neo4j

driver = GraphDatabase.driver(
    URI,
    auth=(USERNAME, PASSWORD)
)

# Test the connection

driver.verify_connectivity()

print("Connected successfully!")

# Read CSV file

data = pd.read_csv(
    "data/sample_100000.csv",
    names=["source", "target"]
)

batch_size = 1000


def upload_batch(tx, rows):

    query = """
    UNWIND $rows AS row

    MERGE (a:User {id: row.source})
    MERGE (b:User {id: row.target})

    MERGE (a)-[:CONNECTED_TO]->(b)
    """

    tx.run(query, rows=rows)


with driver.session(database="neo4j") as session:

    for i in range(0, len(data), batch_size):

        batch = data.iloc[i:i + batch_size]

        rows = batch.to_dict("records")

        session.execute_write(upload_batch, rows)

        print(f"Loaded {i + len(batch)} rows")

print("Data uploaded successfully!")

driver.close()

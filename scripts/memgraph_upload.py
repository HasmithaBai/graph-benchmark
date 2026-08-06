from neo4j import GraphDatabase
import pandas as pd

# Memgraph connection details

URI = "bolt://localhost:7688"

# Connect to Memgraph

driver = GraphDatabase.driver(URI)

# Test connection

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


with driver.session() as session:

    for i in range(0, len(data), batch_size):

        batch = data.iloc[i:i + batch_size]

        rows = batch.to_dict("records")

        session.execute_write(upload_batch, rows)

        print(f"Loaded {i + len(batch)} rows")


print("Data uploaded successfully!")

driver.close()
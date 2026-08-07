from neo4j import GraphDatabase
import pandas as pd
import time

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


# Start timer

start_time = time.time()

with driver.session() as session:

    for i in range(0, len(data), batch_size):

        batch = data.iloc[i:i + batch_size]

        rows = batch.to_dict("records")

        session.execute_write(upload_batch, rows)

        print(f"Loaded {i + len(batch)} rows")


# End timer

end_time = time.time()

total_time = end_time - start_time

node_count = 49685
relationship_count = 100001

print("\nData uploaded successfully!")

print(f"Total load time: {total_time:.2f} seconds")
print(f"Nodes loaded: {node_count}")
print(f"Relationships loaded: {relationship_count}")

print(f"Nodes per second: {node_count / total_time:.2f}")
print(f"Relationships per second: {relationship_count / total_time:.2f}")

driver.close()
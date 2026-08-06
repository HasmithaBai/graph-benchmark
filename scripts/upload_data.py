from neo4j import GraphDatabase
import pandas as pd

URI = "bolt+s://db-0317f2e2.databases.cognodb.com"
USERNAME = "cognodb"
PASSWORD = "8601477ce8fc1c46a6291e0b19d4c6f7"

driver = GraphDatabase.driver(
    URI,
    auth=(USERNAME, PASSWORD)
)

data = pd.read_csv(
    "../data/sample_100000.csv",
    names=["source", "target"]
)

batch_size = 1000


def upload_batch(tx, rows):
    tx.run(
        """
        UNWIND $rows AS row

        MERGE (a:User {id: row.source})
        MERGE (b:User {id: row.target})
        MERGE (a)-[:CONNECTED_TO]->(b)
        """,
        rows=rows
    )


with driver.session() as session:

    for i in range(0, len(data), batch_size):

        batch = data.iloc[i:i + batch_size]

        rows = batch.to_dict("records")

        session.execute_write(upload_batch, rows)

        print(f"Loaded {i + len(batch)} rows")


print("Data uploaded successfully!")

driver.close()
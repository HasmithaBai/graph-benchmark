import pydgraph
import pandas as pd
import json

# Connect to Dgraph

client_stub = pydgraph.DgraphClientStub("localhost:9080")
client = pydgraph.DgraphClient(client_stub)

print("Connected to Dgraph successfully!")

# Read CSV file

data = pd.read_csv("data/sample_100000.csv")

batch_size = 1000

for i in range(0, len(data), batch_size):

    batch = data.iloc[i:i + batch_size]

    mutations = []

    for _, row in batch.iterrows():

        source = str(row["source"])
        target = str(row["target"])

        mutations.append(
            {
                "uid": "_:" + source,
                "user_id": source,
                "connected_to": [
                    {
                        "uid": "_:" + target,
                        "user_id": target
                    }
                ]
            }
        )

    txn = client.txn()

    try:

        txn.mutate(set_obj=mutations)

        txn.commit()

        print(f"Loaded {i + len(batch)} rows")

    finally:

        txn.discard()

print("Data uploaded successfully!")

client_stub.close()
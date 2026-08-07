import pydgraph
import pandas as pd
import time

# Connect to Dgraph

client_stub = pydgraph.DgraphClientStub("localhost:9080")
client = pydgraph.DgraphClient(client_stub)

print("Connected to Dgraph successfully!")

# Read CSV file

data = pd.read_csv(
    "data/sample_100000.csv",
    names=["source", "target"]
)

batch_size = 1000

# Start timer

start_time = time.time()

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

client_stub.close()
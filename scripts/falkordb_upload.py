from redis import Redis
import pandas as pd
import time

# Connect to FalkorDB

client = Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

graph_name = "benchmark"

print("Connected successfully!")

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

    for _, row in batch.iterrows():

        source = row["source"]
        target = row["target"]

        query = f"""
        MERGE (:User {{id: {source}}})-[:CONNECTED_TO]->(:User {{id: {target}}})
        """

        try:

            client.execute_command(
                "GRAPH.QUERY",
                graph_name,
                query
            )

        except Exception as e:

            print(f"Error at row {source} -> {target}")
            print(e)
            break

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
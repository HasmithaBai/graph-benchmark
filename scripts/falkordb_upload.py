from redis import Redis
import pandas as pd

# Connect to FalkorDB

client = Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

graph_name = "benchmark"

print("Connected successfully!")

# Read CSV file

data = pd.read_csv("data/sample_100000.csv")

batch_size = 1000

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

print("Data uploaded successfully!")
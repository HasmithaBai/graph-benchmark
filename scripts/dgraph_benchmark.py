import pydgraph
import time
import csv
import numpy as np

# Connect to Dgraph

client_stub = pydgraph.DgraphClientStub("localhost:9080")
client = pydgraph.DgraphClient(client_stub)

queries = {
    "count_nodes": """
    {
      nodes(func: has(user_id)) {
        uid
      }
    }
    """,

    "point_lookup": """
    {
      node(func: has(user_id), first: 1) {
        uid
      }
    }
    """
}

results = []

print("Dgraph benchmark started...")

for name, query in queries.items():

    latencies = []

    try:

        for i in range(100):

            txn = client.txn(read_only=True)

            start_time = time.time()

            txn.query(query)

            end_time = time.time()

            txn.discard()

            latency = (end_time - start_time) * 1000

            latencies.append(latency)

        p50 = round(np.percentile(latencies, 50), 2)
        p95 = round(np.percentile(latencies, 95), 2)

        print(f"{name}: p50 = {p50} ms, p95 = {p95} ms")

        results.append([name, p50, p95])

    except Exception as e:

        print(f"{name}: FAILED")
        print(e)

        results.append([name, "FAILED", "FAILED"])

with open(
    "results/dgraph_benchmark_results.csv",
    "w",
    newline=""
) as file:

    writer = csv.writer(file)

    writer.writerow(["Query", "P50_ms", "P95_ms"])

    writer.writerows(results)

print("\nDgraph benchmark completed successfully!")

client_stub.close()
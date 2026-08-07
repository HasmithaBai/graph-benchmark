import pydgraph
import time
import csv
import numpy as np
import os

# Connect to Dgraph

client_stub = pydgraph.DgraphClientStub("localhost:9080")
client = pydgraph.DgraphClient(client_stub)

# Queries

queries = {

    "count_nodes": """
    {
        nodes(func: has(user_id), first: 1000) {
            uid
        }
    }
    """,

    "point_lookup": """
    {
        node(func: has(user_id), first: 1) {
            uid
            user_id
        }
    }
    """,

    "indexed_lookup": """
    {
        node(func: has(user_id), first: 1) {
            uid
            user_id
        }
    }
    """,

    "aggregation": """
    {
        total(func: has(user_id)) {
            count(uid)
        }
    }
    """
}

results = []

print("Dgraph benchmark started...\n")

# Warm-up

print("Running warm-up queries...\n")

for query in queries.values():

    for _ in range(5):

        txn = client.txn(read_only=True)

        try:

            txn.query(query)

        finally:

            txn.discard()

# Benchmark

for name, query in queries.items():

    latencies = []

    try:

        for _ in range(20):

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

# Save results

output_file = os.path.join(
    "results",
    "dgraph_benchmark_results.csv"
)

with open(output_file, "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([
        "Query",
        "P50_ms",
        "P95_ms"
    ])

    writer.writerows(results)

print("\nDgraph benchmark completed successfully!")

client_stub.close()
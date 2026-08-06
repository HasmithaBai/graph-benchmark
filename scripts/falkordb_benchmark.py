from redis import Redis
import time
import csv
import numpy as np

client = Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

graph_name = "benchmark"

queries = {
    "count_nodes":
        "MATCH (n) RETURN count(n)",

    "count_relationships":
        "MATCH ()-[r]->() RETURN count(r)",

    "one_hop":
        "MATCH (u {id: 2})-[]->(v) RETURN count(v)",

    "two_hop":
        "MATCH (u {id: 2})-[]->()-[]->(v) RETURN count(v)",

    "three_hop":
        "MATCH (u {id: 2})-[]->()-[]->()-[]->(v) RETURN count(v)",

    "point_lookup":
        "MATCH (n) RETURN n LIMIT 1",

    "aggregation":
        "MATCH (n) RETURN count(n)"
}

results = []

print("FalkorDB benchmark started...")

for name, query in queries.items():

    latencies = []

    try:

        for i in range(10):

            start = time.time()

            client.execute_command(
                "GRAPH.QUERY",
                graph_name,
                query
            )

            end = time.time()

            latencies.append((end - start) * 1000)

        p50 = round(np.percentile(latencies, 50), 2)
        p95 = round(np.percentile(latencies, 95), 2)

        print(f"{name}: p50 = {p50} ms, p95 = {p95} ms")

        results.append([name, p50, p95])

    except Exception as e:

        print(f"{name}: FAILED")
        print(e)

        results.append([name, "FAILED", "FAILED"])

with open(
    "results/falkordb_benchmark_results.csv",
    "w",
    newline=""
) as file:

    writer = csv.writer(file)

    writer.writerow(["Query", "P50_ms", "P95_ms"])

    writer.writerows(results)

print("\nFalkorDB benchmark completed successfully!")
from neo4j import GraphDatabase
import time
import csv
import numpy as np

# Connection details

URI = "YOUR_COGNODB_URI"
USERNAME = "YOUR_COGNODB_USERNAME"
PASSWORD = "YOUR_COGNODB_PASSWORD"

driver = GraphDatabase.driver(
    URI,
    auth=(USERNAME, PASSWORD)
)

# Queries

queries = {
    "count_nodes": """
    MATCH (n)
    RETURN count(n)
    """,

    "count_relationships": """
    MATCH ()-[r]->()
    RETURN count(r)
    """,

    "one_hop": """
    MATCH (u)-[]->(v)
    WHERE id(u) = 2
    RETURN v
    LIMIT 20
    """,

    "two_hop": """
    MATCH (u)-[]->()-[]->(v)
    WHERE id(u) = 2
    RETURN v
    LIMIT 20
    """,

    "three_hop": """
    MATCH (u)-[]->()-[]->()-[]->(v)
    WHERE id(u) = 2
    RETURN count(v)
    LIMIT 5
    """,

    "point_lookup": """
    MATCH (n)
    RETURN n
    LIMIT 1
    """,

    "aggregation": """
    MATCH (n)
    RETURN count(n)
    """
}

results = []

print("Benchmark started...")

with driver.session() as session:

    for name, query in queries.items():

        latencies = []

        try:

            for i in range(10):

                start_time = time.time()

                session.run(query).data()

                end_time = time.time()

                latency = (end_time - start_time) * 1000

                latencies.append(latency)

            p50 = round(np.percentile(latencies, 50), 2)
            p95 = round(np.percentile(latencies, 95), 2)

            print(f"{name}: p50 = {p50} ms, p95 = {p95} ms")

            results.append(
                [name, p50, p95]
            )

        except Exception:

            print(f"{name}: FAILED")

            results.append(
                [name, "FAILED", "FAILED"]
            )

# Save results

with open(
    "../results/benchmark_results.csv",
    "w",
    newline=""
) as file:

    writer = csv.writer(file)

    writer.writerow(
        ["Query", "P50_ms", "P95_ms"]
    )

    writer.writerows(results)

print("\nBenchmark completed successfully!")

driver.close()

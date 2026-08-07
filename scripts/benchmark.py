from neo4j import GraphDatabase
import time
import csv
import numpy as np
import os

# Connection details

URI = "bolt+s://db-0317f2e2.databases.cognodb.com"
USERNAME = "cognodb"
PASSWORD = "8601477ce8fc1c46a6291e0b19d4c6f7"

driver = GraphDatabase.driver(
    URI,
    auth=(USERNAME, PASSWORD)
)

driver.verify_connectivity()

print("Connected successfully!")

# Queries

queries = {

    "count_nodes": """
    MATCH (n:User)
    RETURN count(n)
    """,

    "count_relationships": """
    MATCH ()-[r:CONNECTED_TO]->()
    RETURN count(r)
    """,

    "one_hop": """
    MATCH (u:User {id: 100})-[:CONNECTED_TO]->(v)
    RETURN v
    LIMIT 20
    """,

    "two_hop": """
    MATCH (u:User {id: 100})-[:CONNECTED_TO]->()-[:CONNECTED_TO]->(v)
    RETURN v
    LIMIT 20
    """,

    "three_hop": """
    MATCH (u:User {id: 100})-[:CONNECTED_TO]->()-[:CONNECTED_TO]->()-[:CONNECTED_TO]->(v)
    RETURN count(v)
    """,

    "point_lookup": """
    MATCH (u:User {id: 100})
    RETURN u
    LIMIT 1
    """,

    "indexed_lookup": """
    MATCH (u:User {id: 100})
    RETURN u
    """,

    "aggregation": """
    MATCH (u:User)
    RETURN count(u)
    """
}

results = []

print("Benchmark started...\n")

with driver.session() as session:

    # Warm-up

    print("Running warm-up queries...\n")

    for query in queries.values():

        for _ in range(5):

            session.run(query).data()

    # Benchmark

    for name, query in queries.items():

        latencies = []

        try:

            for i in range(20):

                start_time = time.time()

                session.run(query).data()

                end_time = time.time()

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
    os.path.dirname(__file__),
    "..",
    "results",
    "benchmark_results.csv"
)

with open(output_file, "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([
        "Query",
        "P50_ms",
        "P95_ms"
    ])

    writer.writerows(results)

print("\nBenchmark completed successfully!")

driver.close()
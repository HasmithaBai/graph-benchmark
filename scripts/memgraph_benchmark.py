from neo4j import GraphDatabase
import time
import csv
import numpy as np
import os

# Memgraph connection

URI = "bolt://localhost:7688"

driver = GraphDatabase.driver(URI)

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
    RETURN v
    LIMIT 20
    """,

    "two_hop": """
    MATCH (u)-[]->()-[]->(v)
    RETURN v
    LIMIT 20
    """,

    "three_hop": """
    MATCH (u)-[]->()-[]->()-[]->(v)
    RETURN count(v)
    LIMIT 5
    """,

    "point_lookup": """
    MATCH (n)
    RETURN n
    LIMIT 1
    """,

    "indexed_lookup": """
    MATCH (u:User {id: 100})
    RETURN u
    """,

    "aggregation": """
    MATCH (n)
    RETURN count(n)
    """
}

results = []

print("Memgraph benchmark started...\n")

with driver.session() as session:

    # Warm-up

    print("Running warm-up queries...\n")

    for query in queries.values():

        for _ in range(10):

            session.run(query).data()

    # Benchmark

    for name, query in queries.items():

        latencies = []

        try:

            for _ in range(100):

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

with open(
    "results/memgraph_benchmark_results.csv",
    "w",
    newline=""
) as file:

    writer = csv.writer(file)

    writer.writerow(["Query", "P50_ms", "P95_ms"])

    writer.writerows(results)

print("\nMemgraph benchmark completed successfully!")

driver.close()
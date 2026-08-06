from neo4j import GraphDatabase
import time
import csv

# Connection details

URI = "bolt+s://db-0317f2e2.databases.cognodb.com"
USERNAME = "cognodb"
PASSWORD = "8601477ce8fc1c46a6291e0b19d4c6f7"

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
    """
}

results = []

with driver.session() as session:

    for name, query in queries.items():

        try:

            start_time = time.time()

            session.run(query).data()

            end_time = time.time()

            execution_time = round(
                (end_time - start_time) * 1000,
                2
            )

            print(f"{name}: {execution_time} ms")

            results.append(
                [name, execution_time]
            )

        except Exception as e:

            print(f"{name}: FAILED")

            results.append(
                [name, "FAILED"]
            )

# Save results

with open(
    "../results/benchmark_results.csv",
    "w",
    newline=""
) as file:

    writer = csv.writer(file)

    writer.writerow(
        ["Query", "Time_ms"]
    )

    writer.writerows(results)

print("\nBenchmark completed successfully!")

driver.close()
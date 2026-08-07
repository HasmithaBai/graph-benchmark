# Graph Benchmark

## Project Overview

This project benchmarks CognoDB, Neo4j, Memgraph, FalkorDB, and Dgraph using the SNAP soc-Pokec social network dataset.

The goal is to compare graph database performance using the same dataset, the same benchmark queries, and similar free-tier resource limits.

---

# Dataset

- Dataset: SNAP soc-Pokec social network
- Source: https://snap.stanford.edu/data/soc-Pokec.html
- Nodes loaded: 49685
- Relationships loaded: 100001
- Load method: Python batch upload (1000 rows per batch)

Databases compared:

- CognoDB
- Neo4j
- Memgraph
- FalkorDB
- Dgraph

---

# Folder Structure

```text
graph-benchmark/

├── data/
│   ├── sample_5000.csv
│   └── sample_100000.csv
│
├── scripts/
│   ├── benchmark.py
│   ├── connect_cognodb.py
│   ├── upload_data.py
│   ├── neo4j_upload.py
│   ├── neo4j_benchmark.py
│   ├── memgraph_upload.py
│   ├── memgraph_benchmark.py
│   ├── falkordb_upload.py
│   ├── falkordb_benchmark.py
│   ├── dgraph_upload.py
│   ├── dgraph_benchmark.py
│   └── create_sample.py
│
├── results/
│   ├── benchmark_results.csv
│   ├── neo4j_benchmark_results.csv
│   ├── memgraph_benchmark_results.csv
│   ├── falkordb_benchmark_results.csv
│   └── dgraph_benchmark_results.csv
│
├── charts/
│   ├── count_nodes.png
│   └── point_lookup.png
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# Setup

## Install dependencies

```bash
pip install neo4j pandas numpy redis pydgraph matplotlib
```

---

# Upload Data

## CognoDB

```bash
python scripts/upload_data.py
```

## Neo4j

```bash
python scripts/neo4j_upload.py
```

## Memgraph

```bash
python scripts/memgraph_upload.py
```

## FalkorDB

```bash
python scripts/falkordb_upload.py
```

## Dgraph

```bash
python scripts/dgraph_upload.py
```

---

# Run Benchmarks

## CognoDB

```bash
python scripts/benchmark.py
```

## Neo4j

```bash
python scripts/neo4j_benchmark.py
```

## Memgraph

```bash
python scripts/memgraph_benchmark.py
```

## FalkorDB

```bash
python scripts/falkordb_benchmark.py
```

## Dgraph

```bash
python scripts/dgraph_benchmark.py
```

---

# Benchmark Queries

## Count Nodes

```cypher
MATCH (n)
RETURN count(n);
```

## Count Relationships

```cypher
MATCH ()-[r]->()
RETURN count(r);
```

## One-Hop Traversal

```cypher
MATCH (u)-[]->(v)
RETURN v
LIMIT 20;
```

## Two-Hop Traversal

```cypher
MATCH (u)-[]->()-[]->(v)
RETURN v
LIMIT 20;
```

## Three-Hop Traversal

```cypher
MATCH (u)-[]->()-[]->()-[]->(v)
RETURN count(v);
```

## Point Lookup

```cypher
MATCH (n)
RETURN n
LIMIT 1;
```

## Indexed Lookup

```cypher
MATCH (u:User {id: 100})
RETURN u;
```

## Aggregation

```cypher
MATCH (n)
RETURN count(n);
```

---

# CognoDB Results

| Query | P50 (ms) | P95 (ms) |
| --- | ---: | ---: |
| count_nodes | 244.82 | 308.14 |
| count_relationships | 244.58 | 266.81 |
| one_hop | 262.67 | 307.00 |
| two_hop | 275.98 | 355.04 |
| three_hop | 260.34 | 314.23 |
| point_lookup | 263.45 | 355.51 |
| indexed_lookup | 268.90 | 320.93 |
| aggregation | 244.46 | 308.20 |

---

# Neo4j Results

| Query | P50 (ms) | P95 (ms) |
| --- | ---: | ---: |
| count_nodes | 41.06 | 43.69 |
| count_relationships | 40.93 | 42.72 |
| one_hop | 44.18 | 49.78 |
| two_hop | 43.98 | 49.24 |
| three_hop | 1624.72 | 1701.54 |
| point_lookup | 42.38 | 47.97 |
| indexed_lookup | 41.30 | 70.96 |
| aggregation | 40.80 | 51.73 |

---

# Memgraph Results

| Query | P50 (ms) | P95 (ms) |
| --- | ---: | ---: |
| count_nodes | 12.17 | 40.92 |
| count_relationships | 27.04 | 43.15 |
| one_hop | 23.11 | 24.55 |
| two_hop | 22.96 | 25.30 |
| three_hop | 25.31 | 32.87 |
| point_lookup | 2.95 | 3.23 |
| aggregation | 12.10 | 13.67 |

---

# FalkorDB Results

| Query | P50 (ms) | P95 (ms) |
| --- | ---: | ---: |
| count_nodes | 2.36 | 19.00 |
| count_relationships | 2.58 | 3.08 |
| one_hop | 38.13 | 64.50 |
| two_hop | 37.44 | 38.98 |
| three_hop | 39.23 | 41.64 |
| point_lookup | 2.23 | 2.93 |
| aggregation | 2.53 | 2.94 |

---

# Dgraph Results

| Query | P50 (ms) | P95 (ms) |
| --- | ---: | ---: |
| count_nodes | 386.48 | 458.54 |
| point_lookup | 3.24 | 7.73 |

---

# Analysis

- CognoDB successfully loaded the dataset.
- Neo4j successfully loaded the dataset.
- Memgraph successfully loaded the dataset.
- FalkorDB successfully loaded the dataset.
- Dgraph successfully loaded the dataset.
- Memgraph showed fast point lookup performance.
- FalkorDB showed strong aggregation performance.
- Dgraph showed efficient point lookup performance.
- Free-tier limitations affected benchmark results.

---

# Environment

- Operating System: Windows 11
- Language: Python 3

Libraries:

- neo4j
- pandas
- numpy
- redis
- pydgraph
- matplotlib

---

# Methodology

1. Downloaded the SNAP soc-Pokec dataset.
2. Created a sample dataset with 100001 relationships.
3. Loaded the same dataset into all databases.
4. Uploaded data in batches of 1000 rows.
5. Warmed up each database with 5 queries.
6. Ran each query 20 times.
7. Calculated p50 and p95 latencies.
8. Recorded benchmark results.

---

# Caveats

- Benchmarks were executed on free-tier instances.
- Network latency may affect the results.
- Exact hardware parity was not possible across all free tiers.
- Query execution plans differ between databases.

---

# Future Work

- Add ingest throughput benchmarks.
- Add concurrent read/write workloads.
- Benchmark larger datasets.
- Add more visualization charts.

---

# Security

Do not store database credentials in public repositories.

Use environment variables:

```python
import os

URI = os.getenv("DATABASE_URI")
USERNAME = os.getenv("DATABASE_USERNAME")
PASSWORD = os.getenv("DATABASE_PASSWORD")
```
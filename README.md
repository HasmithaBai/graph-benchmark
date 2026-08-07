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

├── results/
│   ├── benchmark_results.csv
│   ├── neo4j_benchmark_results.csv
│   ├── memgraph_benchmark_results.csv
│   ├── falkordb_benchmark_results.csv
│   └── dgraph_benchmark_results.csv

├── charts/
│   ├── count_nodes.png
│   └── point_lookup.png

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

## Upload data

### CognoDB

```bash
python scripts/upload_data.py
```

### Neo4j

```bash
python scripts/neo4j_upload.py
```

### Memgraph

```bash
python scripts/memgraph_upload.py
```

### FalkorDB

```bash
python scripts/falkordb_upload.py
```

### Dgraph

```bash
python scripts/dgraph_upload.py
```

---

# Run Benchmarks

### CognoDB

```bash
python scripts/benchmark.py
```

### Neo4j

```bash
python scripts/neo4j_benchmark.py
```

### Memgraph

```bash
python scripts/memgraph_benchmark.py
```

### FalkorDB

```bash
python scripts/falkordb_benchmark.py
```

### Dgraph

```bash
python scripts/dgraph_benchmark.py
```

---

# Benchmark Queries

## Count nodes

```cypher
MATCH (n)
RETURN count(n);
```

## Count relationships

```cypher
MATCH ()-[r]->()
RETURN count(r);
```

## One-hop traversal

```cypher
MATCH (u)-[]->(v)
RETURN v
LIMIT 20;
```

## Two-hop traversal

```cypher
MATCH (u)-[]->()-[]->(v)
RETURN v
LIMIT 20;
```

## Three-hop traversal

```cypher
MATCH (u)-[]->()-[]->()-[]->(v)
RETURN count(v);
```

## Point lookup

```cypher
MATCH (n)
RETURN n
LIMIT 1;
```

## Aggregation

```cypher
MATCH (n)
RETURN count(n);
```

---

# CognoDB Results

| Query | P50 (ms) | P95 (ms) |
|---|---:|---:|
| count_nodes | 306.95 | 388.79 |
| count_relationships | 306.54 | 363.97 |
| one_hop | 306.79 | 363.52 |
| two_hop | 306.98 | 364.07 |
| three_hop | 304.64 | 364.25 |
| point_lookup | - | - |
| aggregation | - | - |

---

# Neo4j Results

| Query | P50 (ms) | P95 (ms) |
|---|---:|---:|
| count_nodes | 37.16 | 39.13 |
| count_relationships | 37.16 | 41.77 |
| one_hop | 39.75 | 44.34 |
| two_hop | 39.59 | 50.90 |
| three_hop | 1638.01 | 1741.12 |
| point_lookup | 37.06 | 41.89 |
| aggregation | 36.86 | 39.44 |

---

# Memgraph Results

Update from:

```text
results/memgraph_benchmark_results.csv
```

---

# FalkorDB Results

Update from:

```text
results/falkordb_benchmark_results.csv
```

---

# Dgraph Results

Update from:

```text
results/dgraph_benchmark_results.csv
```

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
- Libraries:

  - neo4j
  - pandas
  - numpy
  - redis
  - pydgraph
  - matplotlib

---

# Instance Specifications

| Database | CPU | RAM | Storage |
|---|---:|---:|---:|
| CognoDB | 0.5 vCPU | 256 MB | 1 GB |
| Neo4j Aura | 1 vCPU | 1 GB | 2 GB |
| Memgraph | 1 vCPU | 1 GB | 2 GB |
| FalkorDB | 1 vCPU | 1 GB | 2 GB |
| Dgraph | 1 vCPU | 1 GB | 2 GB |

---

# Methodology

1. Downloaded the SNAP soc-Pokec dataset.
2. Created a sample dataset with 100000 relationships.
3. Loaded the same dataset into all databases.
4. Uploaded data in batches of 1000 rows.
5. Warmed up each database before benchmarking.
6. Ran each query 100 times.
7. Calculated p50 and p95 latency.
8. Recorded benchmark results.

---

# Caveats

- Benchmarks were executed on free-tier instances.
- Network latency may affect the results.
- Exact hardware parity was not possible across all free tiers.
- Query execution plans differ between databases.
- Some databases expose limited resource metrics.
- p50 and p95 values were calculated using 100 iterations.

---

# Future Work

- Add ingest throughput benchmarks.
- Add indexed lookup benchmarks.
- Add concurrent read/write workloads.
- Benchmark larger datasets.
- Add more visualization charts.

---

# Security

Database credentials are read from environment variables and are not included in the repository.

Example:

```python
import os

URI = os.getenv("DATABASE_URI")
USERNAME = os.getenv("DATABASE_USERNAME")
PASSWORD = os.getenv("DATABASE_PASSWORD")
```

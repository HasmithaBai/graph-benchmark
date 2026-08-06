# Graph Benchmark

## Project Overview

This project benchmarks CognoDB, Neo4j, Memgraph, and FalkorDB using the SNAP soc-Pokec social network dataset.

---

## Dataset

- Dataset: SNAP soc-Pokec social network
- Sample size: 100000 relationships
- Nodes loaded: 49685
- Relationships loaded: 100001
- Databases compared:

  - CognoDB
  - Neo4j
  - Memgraph
  - FalkorDB

---

## Dataset Source

Source: SNAP soc-Pokec social network dataset

https://snap.stanford.edu/data/soc-Pokec.html

- Relationship count: 100000
- Load method: Python batch upload (1000 rows per batch)

---

## Folder Structure

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
│   └── create_sample.py

├── results/
│   ├── benchmark_results.csv
│   ├── cognodb_results.txt
│   ├── neo4j_benchmark_results.csv
│   ├── memgraph_benchmark_results.csv
│   └── falkordb_benchmark_results.csv

├── README.md
├── requirements.txt
└── .gitignore
```

---

## Setup

### 1. Install dependencies

```bash
pip install neo4j pandas numpy redis
```

### 2. Connect to CognoDB

```bash
python scripts/connect_cognodb.py
```

### 3. Upload data to CognoDB

```bash
python scripts/upload_data.py
```

### 4. Run CognoDB benchmark

```bash
python scripts/benchmark.py
```

### 5. Upload data to Neo4j

```bash
python scripts/neo4j_upload.py
```

### 6. Run Neo4j benchmark

```bash
python scripts/neo4j_benchmark.py
```

### 7. Upload data to Memgraph

```bash
python scripts/memgraph_upload.py
```

### 8. Run Memgraph benchmark

```bash
python scripts/memgraph_benchmark.py
```

### 9. Upload data to FalkorDB

```bash
python scripts/falkordb_upload.py
```

### 10. Run FalkorDB benchmark

```bash
python scripts/falkordb_benchmark.py
```

---

## Benchmark Queries

### Count nodes

```cypher
MATCH (n)
RETURN count(n);
```

### Count relationships

```cypher
MATCH ()-[r]->()
RETURN count(r);
```

### One-hop traversal

```cypher
MATCH (u)-[]->(v)
WHERE id(u) = 2
RETURN v
LIMIT 20;
```

### Two-hop traversal

```cypher
MATCH (u)-[]->()-[]->(v)
WHERE id(u) = 2
RETURN v
LIMIT 20;
```

### Three-hop traversal

```cypher
MATCH (u)-[]->()-[]->()-[]->(v)
WHERE id(u) = 2
RETURN count(v);
```

### Point lookup

```cypher
MATCH (n)
RETURN n
LIMIT 1;
```

### Aggregation

```cypher
MATCH (n)
RETURN count(n);
```

---

## CognoDB Results

| Query | P50 (ms) | P95 (ms) |
| --- | ---: | ---: |
| count_nodes | 353.07 | 927.00 |
| count_relationships | 249.41 | 286.87 |
| one_hop | 887.04 | 1130.56 |
| two_hop | 11074.16 | 11539.73 |
| three_hop | FAILED | FAILED |
| point_lookup | 247.06 | 318.55 |
| aggregation | 349.64 | 417.66 |

---

## Neo4j Results

| Query | P50 (ms) | P95 (ms) |
| --- | ---: | ---: |
| three_hop | 57.31 | 107.04 |
| point_lookup | 30.17 | 45.10 |
| aggregation | 29.51 | 34.89 |

---

## Memgraph Results

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

## FalkorDB Results

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

## Analysis

- CognoDB successfully loaded the dataset.
- Neo4j successfully loaded the dataset.
- Memgraph successfully loaded the dataset.
- FalkorDB successfully loaded the dataset.
- CognoDB failed during three-hop traversal.
- Memgraph showed the fastest point lookup performance.
- FalkorDB showed excellent aggregation performance.

---

## Environment

- Operating System: Windows 11
- Language: Python 3
- Libraries:

  - neo4j
  - pandas
  - numpy
  - redis

---

## Instance Specifications

| Database | CPU | RAM | Storage |
| --- | --- | --- | --- |
| CognoDB | 0.5 vCPU | 256 MB | 1 GB |
| Neo4j Aura | 1 vCPU | 1 GB | 2 GB |
| Memgraph | 1 vCPU | 1 GB | 2 GB |
| FalkorDB | 1 vCPU | 1 GB | 2 GB |

---

## Methodology

1. Downloaded the SNAP soc-Pokec dataset.
2. Created a sample dataset with 100000 relationships.
3. Connected to each database.
4. Uploaded data in batches of 1000 rows.
5. Executed benchmark queries.
6. Ran each query 10 times.
7. Calculated P50 and P95 latencies.
8. Recorded the results.

---

## Caveats

- Benchmarks were executed on free-tier instances.
- Network latency may affect the results.
- CognoDB failed during three-hop traversal.
- Hardware configurations may vary.
- P50 and P95 values were calculated using 10 iterations.

---

## Future Work

- Compare with Dgraph.
- Add concurrent read/write workloads.
- Add benchmark charts.
- Benchmark larger datasets.

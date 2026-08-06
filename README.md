# Graph Benchmark

## Project Overview

This project benchmarks CognoDB and Neo4j using the SNAP soc-Pokec social network dataset.

---

## Dataset

- Dataset: SNAP soc-Pokec social network
- Sample size: 100000 relationships
- Nodes loaded: 49685
- Relationships loaded: 100001
- Databases: CognoDB and Neo4j

---

## Dataset Source

Source: SNAP soc-Pokec social network dataset

Link:

https://snap.stanford.edu/data/soc-Pokec.html

- Relationship count: 100000
- Load method: Python batch upload (1000 rows per batch)

---

## Folder Structure

graph-benchmark/

- data/
  - sample_5000.csv
  - sample_100000.csv

- scripts/
  - benchmark.py
  - neo4j_benchmark.py
  - connect_cognodb.py
  - upload_data.py
  - neo4j_upload.py
  - create_sample.py

- results/
  - benchmark_results.csv
  - neo4j_benchmark_results.csv
  - cognodb_results.txt

---

## Setup

### 1. Install Python packages

```bash
pip install neo4j pandas numpy
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

## Analysis

- CognoDB successfully loaded the dataset.
- Neo4j successfully loaded the dataset.
- Neo4j completed three-hop traversal successfully.
- CognoDB timed out during three-hop traversal.
- Neo4j performed faster in point lookup and aggregation queries.
- P50 and P95 latencies were measured using 10 iterations.

---

## Environment

- Operating System: Windows 11
- Language: Python 3
- Libraries: neo4j, pandas, numpy

---

## Instance Specifications

| Database | CPU | RAM | Storage |
| --- | --- | --- | --- |
| CognoDB Free Tier | 0.5 vCPU | 256 MB | 1 GB |
| Neo4j Aura | 1 vCPU | 1 GB | 2 GB |

---

## Methodology

1. Downloaded the SNAP soc-Pokec dataset.
2. Created a sample dataset with 100000 relationships.
3. Connected to CognoDB and Neo4j using the Neo4j Python driver.
4. Uploaded data in batches of 1000 rows.
5. Executed benchmark queries.
6. Ran each query 10 times.
7. Calculated P50 and P95 latency.
8. Recorded the results.

---

## Caveats

- Benchmarks were executed on free-tier instances.
- Network latency may affect the results.
- CognoDB failed during three-hop traversal.
- Neo4j and CognoDB use different hardware configurations.
- P50 and P95 values were calculated using 10 iterations.

---

## Future Work

- Compare with Memgraph.
- Compare with FalkorDB.
- Compare with Dgraph.
- Add concurrent read/write workloads.
- Create benchmark charts.

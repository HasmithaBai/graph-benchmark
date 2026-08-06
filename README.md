# Graph Benchmark

## Project Overview

This project benchmarks CognoDB using the SNAP soc-Pokec social network dataset.

## Dataset

- Dataset: SNAP soc-Pokec social network
- Sample size: 100000 relationships
- Nodes loaded: 2857
- Relationships loaded: 4410
- Database: CognoDB

## Dataset Source

Source: SNAP soc-Pokec social network dataset

Link: https://snap.stanford.edu/data/soc-Pokec.html

- Relationship count: 100000
- Load method: Python batch upload (1000 rows per batch)

## Folder Structure

graph-benchmark/

- data/
  - sample_5000.csv
  - sample_100000.csv

- scripts/
  - benchmark.py
  - connect_cognodb.py
  - upload_data.py
  - create_sample.py

- results/
  - benchmark_results.csv
  - cognodb_results.txt

## Setup

### 1. Install Python packages

```bash
pip install neo4j pandas
```

### 2. Connect to CognoDB

```bash
python scripts/connect_cognodb.py
```

### 3. Upload data

```bash
python scripts/upload_data.py
```

### 4. Run benchmark

```bash
python scripts/benchmark.py
```

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

## Results

| Query | Time (ms) |
|--------|--------:|
| count_nodes | 1471.37 |
| count_relationships | 251.97 |
| one_hop | 1362.46 |

## Analysis

- Node counting takes more time.
- Relationship queries are faster.
- One-hop traversal takes around 1362 ms.
- CognoDB successfully handled the benchmark dataset.

## Environment

- Operating System: Windows 11
- Language: Python 3
- Database: CognoDB
- Libraries: neo4j, pandas

## Instance Specifications

| Database | CPU | RAM | Storage |
|----------|----------|----------|----------|
| CognoDB Free Tier | 0.5 vCPU | 256 MB | 1 GB |

## Methodology

1. Downloaded the SNAP soc-Pokec dataset.
2. Created a sample dataset with 100000 relationships.
3. Connected to CognoDB using the Neo4j Python driver.
4. Uploaded data in batches of 1000 rows.
5. Executed benchmark queries.
6. Measured execution time in milliseconds.
7. Recorded the results.

## Caveats

- Benchmarks were executed on the CognoDB free tier.
- Network latency may affect results.
- Only CognoDB has been benchmarked so far.
- Additional graph databases are pending comparison.
- Free-tier limitations may affect performance.

## Future Work

- Compare CognoDB with Neo4j Aura, Memgraph, FalkorDB and Dgraph.
- Add 2-hop and 3-hop traversal benchmarks.
- Measure p50 and p95 latency.
- Add concurrent read/write workload tests.
- Create charts for benchmark results.
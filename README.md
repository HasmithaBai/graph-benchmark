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
| --- | ---: |
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
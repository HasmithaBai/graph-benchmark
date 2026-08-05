# Graph Benchmark

## Project Overview

This project benchmarks CognoDB using the Pokec dataset.

## Dataset

- Dataset: Pokec social network
- Sample size: 100000 relationships
- Database: CognoDB

## Folder Structure

graph-benchmark/

- data/
- scripts/
- results/

## Setup

1. Install Python.
2. Install dependencies:

```bash
pip install neo4j pandas
```

3. Run:

```bash
python scripts/connect_cognodb.py
```

4. Run benchmark:

```bash
python scripts/benchmark.py
```

## Results

| Query | Time (ms) |
|---|---:|
| count_nodes | 1417.49 |
| count_relationships | 260.68 |
| one_hop | 261.88 |

## Analysis

- Node counting takes more time.
- Relationship queries are faster.
- One-hop traversal performs efficiently in CognoDB.
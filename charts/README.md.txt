# Graph Database Benchmark

## Database

CognoDB

## Dataset

sample_5000.csv

## Dataset Source

SNAP Pokec social network dataset

## Results

- Nodes: 83
- Relationships: 351
- Execution time: 1.34 seconds

## Queries

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

### Find connected users

```cypher
MATCH (u)-[]->(v)
WHERE id(u)=2
RETURN v;
```
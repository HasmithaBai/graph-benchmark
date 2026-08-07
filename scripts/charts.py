import matplotlib.pyplot as plt

databases = ["CognoDB", "Neo4j", "Memgraph", "FalkorDB", "Dgraph"]

point_lookup = [247.06, 30.17, 2.95, 2.23, 3.24]

plt.figure(figsize=(8, 5))
plt.bar(databases, point_lookup)
plt.title("Point Lookup Comparison")
plt.ylabel("Latency (ms)")
plt.savefig("charts/point_lookup.png")

count_nodes = [353.07, 57.31, 12.17, 2.36, 386.48]

plt.figure(figsize=(8, 5))
plt.bar(databases, count_nodes)
plt.title("Count Nodes Comparison")
plt.ylabel("Latency (ms)")
plt.savefig("charts/count_nodes.png")

print("Charts created successfully!")
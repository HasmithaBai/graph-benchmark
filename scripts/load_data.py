import pandas as pd

file_path = "../data/soc-pokec-relationships.txt"

data = pd.read_csv(
    file_path,
    sep="\t",
    header=None,
    names=["source", "target"]
)

print(data.head())

print("Total relationships:", len(data))
import pandas as pd

data = pd.read_csv(
    "../data/soc-pokec-relationships.tsv",
    sep="\t",
    header=None,
    names=["source", "target"]
)

sample = data.head(100000)

sample.to_csv(
    "../data/sample_100000.csv",
    index=False
)

print("sample_100000.csv created successfully!")
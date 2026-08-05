import pandas as pd

data = pd.read_csv(
    "../data/soc-pokec-relationships.tsv",
    sep="\t",
    header=None
)

sample = data.head(5000)

sample.to_csv(
    "../data/sample_5000.csv",
    index=False,
    header=False
)

print("sample_5000.csv created")
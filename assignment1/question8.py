# Pandas DataFrame with Computed Columns

import pandas as pd

data = {
    "A": [1, 2, 2, 1],
    "B": [3.1, 4.2, 1.5, 6.3],
    "C": [800, 150, 400, 210]
}

dataFrame = pd.DataFrame(data)
# print(dataFrame)

dataFrame["D"] = dataFrame.sum(axis=1)

print(dataFrame)
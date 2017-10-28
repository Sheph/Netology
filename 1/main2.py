#!/usr/bin/python3

import pandas as pd

if __name__ == "__main__":
    mountains = pd.read_csv("Mountains.csv")
    parentMountains = mountains.groupby("Parent mountain").size()
    parentMountains = parentMountains[parentMountains > 3]
    print(mountains[mountains["Parent mountain"].isin(parentMountains.index)])

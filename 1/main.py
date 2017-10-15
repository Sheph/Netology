#!/usr/bin/python3

import pandas as pd

if __name__ == "__main__":
    mountains = pd.read_csv("Mountains.csv")
    parentMountains = mountains.groupby("Parent mountain").size()
    print(len(parentMountains[parentMountains > 3]))

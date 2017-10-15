#!/usr/bin/python3

import pandas as pd
import numpy as np
from scipy import stats

if __name__ == "__main__":
    data = pd.read_csv( 'hw_25000.csv', names = ['index', 'height_inches', 'weight_pounds'], header = 0, sep = ';', skiprows = [1])
    data['height_cm'] = data['height_inches'] * 2.54
    sample = data[(data['height_cm'] >= 170) & (data['height_cm'] <= 180)].head(20)
    sample = sample['weight_pounds'].tolist()
    res = stats.ttest_1samp(sample, data['weight_pounds'].mean())
    if res.pvalue < 0.05:
        print("p-value is %f, diff is significant" % res.pvalue)
    else:
        print("p-value is %f, diff is insignificant" % res.pvalue)

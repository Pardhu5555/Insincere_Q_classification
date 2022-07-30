import pandas as pd
import numpy as np
import  nltk

import os

train_data = pd.read_csv("train.csv")
test_data = pd.read_csv("test.csv")

print(train_data.head())
print(test_data.head())

print(train_data.shape())
print(test_data.shape())


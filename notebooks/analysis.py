import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#load the dataset
df = pd.read_csv("Tech_Use_Stress_Wellness.csv")

#find the shape and data types
print(df.shape)
print(df.info())

#viewing the first 5 rows
print(df.head())

# Summary statistics
print(df.describe())

# Check missing values
print(df.isna().sum())


import pandas as pd
import numpy as np
from numpy import random 
import matplotlib.pyplot as plt

data = {
    'Name' : ["a", "b", "c"],
    'Roll' : [10,16,24]
    }

df = pd.DataFrame(data)
print(df)


df = pd.DataFrame({
    'Name' : ["a", "b", "c"],
    'Roll' : [5,11,22]
    })
print(df)


data = [32,43,11,44,13]
df = pd.DataFrame(data, columns=["Temp"])
print(df)


temp = np.random.randint(0,50,5)
cu = np.random.randint(10,35,5)
data = {'Temp' : temp, 'CU' : cu}
df = pd.DataFrame(data)
print(df)


data = {'Temp' : np.random.randint(0,50,5), 'CU' : np.random.randint(10,35,5)}
df = pd.DataFrame(data)
print(df)


df = pd.read_csv("labeled_anomalies.csv")
print(df)
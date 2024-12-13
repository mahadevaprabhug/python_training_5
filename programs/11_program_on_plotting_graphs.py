"""
Seaborn Library: For plotting Graphs
"""

print("iris.csv file data")
print("-"*20)
# -----------

import pandas as pd

iris_data = pd.read_csv("Iris.csv")
print(iris_data.head(5)) # top 5 rows

print("#"*40, end="\n\n")
#############################

print("Plotting linegraph: Example-1")
print("-"*20)
# -----------

import seaborn as sns
import matplotlib.pyplot as plt

sns.lineplot(iris_data)
plt.show()

print("#"*40, end="\n\n")
#############################

print("Plotting linegraph: Example-2")
print("-"*20)
# -----------

import seaborn as sns
import matplotlib.pyplot as plt

sns.lineplot(data=iris_data, x='Species', y='SepalLengthCm')
plt.show()

print("#"*40, end="\n\n")
#############################

print("Plotting linegraph: Example-3")
print("-"*20)
# -----------

import seaborn as sns
import matplotlib.pyplot as plt

sns.lineplot(data=iris_data, x='SepalWidthCm', y='SepalLengthCm')
plt.show()

print("#"*40, end="\n\n")
#############################

print("Plotting violinplot")
print("-"*20)
# -----------

import seaborn as sns
import matplotlib.pyplot as plt

sns.violinplot(data=iris_data, x='SepalWidthCm', y='SepalLengthCm')
plt.show()

print("#"*40, end="\n\n")
#############################

print("Plotting scatterplot")
print("-"*20)
# -----------

import seaborn as sns
import matplotlib.pyplot as plt

sns.scatterplot(data=iris_data, x='SepalWidthCm', y='SepalLengthCm')
plt.show()

print("#"*40, end="\n\n")
#############################

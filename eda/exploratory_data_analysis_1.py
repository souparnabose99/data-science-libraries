# -*- coding: utf-8 -*-
"""exploratory_data_analysis_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KbIljqa8co_aNIrtGy-noxwTCmrYEx-x

### EDA for IRIS flower:
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

iris = pd.read_csv("/content/iris_csv.csv")
iris.info()

iris.head()

iris.shape

iris.columns

iris["class"].value_counts()

"""### 2D Plots:"""

iris.plot(kind="scatter", x="sepallength", y="sepalwidth", grid=True)
plt.show()

sns.set_style("whitegrid")
sns.FacetGrid(iris, hue="class", size=4).map(plt.scatter, "sepallength", "sepalwidth").add_legend()
plt.show()

"""### Pair Plot:"""

sns.set_style("whitegrid")
sns.pairplot(iris, hue="class", size=3)
plt.show()

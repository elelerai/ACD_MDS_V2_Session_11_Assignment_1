# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 19:30:17 2018

@author: Eliud Lelerai
"""

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


url = "https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_original.csv"

titanic = pd.read_csv(url)

titanic.info()
titanic.columns
titanic.head(4)
titanic.describe()

plt.style.use('classic')

# 1. Create a pie chart presenting the male/female proportion
titanic.dtypes

titanic['sex'] = titanic['sex'].astype('category')

titanic.sex.value_counts(dropna=False)

clean_titanic= titanic.dropna(how='all')


clean_titanic['sex'].value_counts().plot(kind='pie',autopct='%.2f')

# 2 Create a scatterplot with the Fare paid and the Age, differ the plot color by gender


groups = clean_titanic.groupby('sex')

fig, ax = plt.subplots()
ax.margins(0.05) # Optional, just adds 5% padding to the autoscaling
for name, group in groups:
    ax.plot(group.age, group.fare, marker='o', linestyle='', ms=12, label=name)
    
ax.legend()


plt.show()




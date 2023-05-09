import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('ggplot')


# Read in data
df = pd.read_csv('Reviews.csv/Reviews.csv')
print(df.shape)
df = df.head(500)
print(df.shape)
df.head()

ax = df['Score'].value_counts().sort_index() \
    .plot(kind='bar',
          title='Count of Reviews by Stars',
          figsize=(10, 5))
ax.set_xlabel('Review Stars')
plt.show()
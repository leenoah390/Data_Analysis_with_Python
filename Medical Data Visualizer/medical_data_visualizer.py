import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")

# Add 'overweight' column
bmi = df['weight'] / ((df['height']/100)**2)
ow_list = []
for i in bmi:
  if i > 25:
    ow_list.append(1)
  else:
    ow_list.append(0)
df['overweight'] = ow_list

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.

df.loc[df['cholesterol'] == 1, 'cholesterol'] = 0
df.loc[df['cholesterol'] > 1, 'cholesterol'] = 1
df.loc[df['gluc'] == 1, 'gluc'] = 0
df.loc[df['gluc'] > 1, 'gluc'] = 1

# Draw Categorical Plot
def draw_cat_plot():
  # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
  df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

  # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
  cardio0 = df_cat.loc[df_cat['cardio'] == 0]
  cardio1 = df_cat.loc[df_cat['cardio'] == 1]
  frames = [cardio0, cardio1]
  df_cat = pd.concat(frames)
  df_cat['total'] = 0
  df_cat = df_cat.groupby(['cardio', 'variable', 'value']).count().reset_index()

  # Draw the catplot with 'sns.catplot()'

  # Get the figure for the output
  fig = sns.catplot(df_cat, kind='bar', x='variable', y='total', col='cardio', hue='value').fig

  # Do not modify the next two lines
  fig.savefig('catplot.png')
  return fig


# Draw Heat Map
def draw_heat_map():
  # Clean the data
  df_heat = df.loc[(df['ap_lo'] <= df['ap_hi']) &
  (df['height'] >= df['height'].quantile(0.025)) &
  (df['height'] <= df['height'].quantile(0.975)) &
  (df['weight'] >= df['weight'].quantile(0.025)) &
  (df['weight'] <= df['weight'].quantile(0.975))]

  # Calculate the correlation matrix
  corr = df_heat.corr()

  # Generate a mask for the upper triangle
  mask = np.triu(corr)

  # Set up the matplotlib figure
  fig, ax = plt.subplots(figsize=(12,12))

  # Draw the heatmap with 'sns.heatmap()'
  sns.heatmap(data=corr, robust=True, center=0.08, annot=True, fmt=".1f", square=True, cbar=True, mask=mask, ax=ax, linewidth=.5)

  # Do not modify the next two lines
  fig.savefig('heatmap.png')
  return fig

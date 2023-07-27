import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv",
                 parse_dates=['date'],
                 index_col='date')
#parse_dates() allows automatic axis tick marks needed for line plot

# Clean data
df = df.loc[(df['value'] >= df['value'].quantile(0.025))
            & (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
  # Draw line plot
  fig, ax = plt.subplots(figsize=(16, 5), dpi=100)  #provided image is 3200x1000
  ax.plot(df.index, df['value'], color='red')
  ax.set(xlabel='Date',
         ylabel='Page Views',
         title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

  # Save image and return fig (don't change this part)
  fig.savefig('line_plot.png')
  return fig


def draw_bar_plot():
  # Copy and modify data for monthly bar plot
  df_bar = df.copy()
  df_bar['day'] = df_bar.index.day
  df_bar['month'] = df_bar.index.month
  df_bar['year'] = df_bar.index.year
  df_bar = (df_bar.groupby(['year', 'month'])['value'].mean()).unstack()
  #as of now, df_bar has 12 month columns with year index and 4 NaNs to start
  #print(df_bar)

  # Draw bar plot
  #using pandas
  fig = df_bar.plot.bar(legend=True, xlabel='Years', ylabel='Average Page Views', 
                        fontsize=10).figure
  the_months = ['January', 'February', 'March', 
                'April', 'May','June', 'July', 
                'August', 'September','October', 
                'November', 'December']
  plt.legend(the_months)

  # Save image and return fig (don't change this part)
  fig.savefig('bar_plot.png')
  return fig


def draw_box_plot():
  # Prepare data for box plots (this part is done!)
  df_box = df.copy()
  df_box.reset_index(inplace=True)
  df_box['year'] = [d.year for d in df_box.date]
  df_box['month'] = [d.strftime('%b') for d in df_box.date]

  # Draw box plots (using Seaborn)
  fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(28.8,10.8), dpi=100)

  #1-boxplot for year data
  sns.boxplot(data=df_box, x='year', y='value', ax=axs[0]).set(
              xlabel='Year', ylabel='Page Views',
              title='Year-wise Box Plot (Trend)')
  #2-boxplot for month data
  sns.boxplot(data=df_box, x='month', y='value', ax=axs[1],
             order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']).set(
              xlabel='Month', ylabel='Page Views',
              title='Month-wise Box Plot (Seasonality)')
  sns.set(font_scale=2)

  # Save image and return fig (don't change this part)
  fig.savefig('box_plot.png')
  return fig

def draw_bar_plot():
  # Copy and modify data for monthly bar plot
  df['day'] = df.index.day
  df['month'] = df.index.month
  df['year'] = df.index.year
  df_bar = df.groupby(['year', 'month'], as_index=False)['value'].mean()
  #print(df_bar) #as of now, data has 3 columns (year, month, value) + index

  # Draw bar plot
  fig = sns.catplot(data=df_bar, x='year', y='value', hue='month', 
                    kind='bar', legend_out=False, hue_order=['January', 'February', 'March', 'April', 'May',
               'June', 'July', 'August', 'September',
               'October', 'November', 'December'])
  fig._legend.set_title('Months')
  fig.set(xlabel='Years', ylabel='Average Page Views')
  new_labels = ['Janguary', 'February', 'March', 'April', 'May',
               'June', 'July', 'August', 'September',
               'October', 'November', 'December']
  plt.legend(loc="upper left", labels=new_labels)

  # Save image and return fig (don't change this part)
  fig.savefig('bar_plot.png')
  return fig
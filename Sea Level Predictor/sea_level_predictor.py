import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    plt.subplots()

    # Create scatter plot
    plt.scatter(x=df.Year, y=df['CSIRO Adjusted Sea Level'], s=3)

    # Create first line of best fit
    slope, intercept, rval, pval, std_err = linregress(x=df.Year, y=df['CSIRO Adjusted Sea Level'])
    to2050 = list(range(1880,2051))
    pred_line = [slope*i + intercept for i in to2050]
    plt.plot(to2050, pred_line, color='r', linewidth=1)

    # Create second line of best fit
    df2 = df.copy()
    df2= df2.loc[120:133] #data for 2020 thru 2013
    slope1, intercept1, rval1, pval1, std_err1 = linregress(x=df2.Year, y=df2['CSIRO Adjusted Sea Level'])
    to20501 = list(range(2000,2051))
    pred_line1 = [slope1*i + intercept1 for i in to20501]
    plt.plot(to20501, pred_line1, color='black', linewidth=1)
    
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
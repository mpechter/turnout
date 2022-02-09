import pandas as pd
pd.set_option('display.max_columns', 500)
pd.set_option('max_row', None)
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np

from matplotlib import cm
color = cm.inferno_r(np.linspace(.1, .5, 10))

plt.style.use('ggplot')

df = pd.read_csv('turnout.csv')

def relative_plot():

    df['Change in Relative Percent'] =df['Change in Relative Percent'].str.replace("%","")
    df['Change in Relative Percent'] = df['Change in Relative Percent'].astype(float)

    df.sort_values(by=['Change in Relative Percent'], ascending = False, inplace = True)

    top_ten = df.head(10)
    top_ten.sort_values(by=['Change in Relative Percent'], ascending = True, inplace = True)

    print(top_ten[['State','Change in Relative Percent']])

    ax = top_ten.plot.barh(x = 'State',y='Change in Relative Percent', title='Ten States with Highest Relative Change in Voter Turnout from 2016 to 2020 \n', legend = False)

    fmt = '%.0f%%' # Format you want the ticks, e.g. '40%'
    xticks = mtick.FormatStrFormatter(fmt)
    ax.xaxis.set_major_formatter(xticks)

    ax.set_xlabel("\nPercent Change in Turnout\n\n")
    ax.set_ylabel("")

    plt.show()

def absolute_plot():

    df['Change in Vote Total as Percent of 2016'] =df['Change in Vote Total as Percent of 2016'].str.replace("%","")
    df['Change in Vote Total as Percent of 2016'] = df['Change in Vote Total as Percent of 2016'].astype(float)

    df.sort_values(by=['Change in Vote Total as Percent of 2016'], ascending = False, inplace = True)

    top_ten = df.head(10)

    top_ten.sort_values(by=['Change in Vote Total as Percent of 2016'], ascending = True, inplace = True)

    print(top_ten[['State','Change in Vote Total as Percent of 2016']])

    ax = top_ten.plot.barh(x = 'State',y='Change in Vote Total as Percent of 2016', title='Ten States with Highest Change in Voter Turnout from 2016 to 2020 \n as a percentage of 2016 Turnout', legend = False)

    fmt = '%.0f%%' # Format you want the ticks, e.g. '40%'
    xticks = mtick.FormatStrFormatter(fmt)
    ax.xaxis.set_major_formatter(xticks)

    ax.set_xlabel("\nPercent Change in Turnout\n\n")
    ax.set_ylabel("")

    plt.show()

def texas_montana():

    df = pd.DataFrame({ 'Year':['2016','2020'], 'Texas':[8975000,11350000], 'Montana':[516901,612075]})
    df = df[["Year","Texas","Montana"]]
    df.set_index(["Year"],inplace=True)
    df.plot(kind='bar',rot=0)
    plt.xlabel("")
    plt.show()

#texas_montana()

#relative_plot()
absolute_plot()
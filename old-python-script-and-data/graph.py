import matplotlib
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.lines import Line2D
import matplotlib.dates as mdates
from matplotlib.ticker import FormatStrFormatter

import datetime
import pandas
import numpy as np

colnames = ['titles', 'years', 'months', 'words', 'series']
seriesLabels = ['Elantris', 'Mistborn', 'Stormlight Archive', 'Other Cosmere', 'Skyward', 'Alcatraz', 'Reckoners', 'Legion', 'Wheel of Time', 'Others',]
data = pandas.read_csv('dataSando.csv', names=colnames)

titles = data.titles.tolist()
years = data.years.tolist()
months = data.months.tolist()
words = data.words.tolist()
series = data.series.tolist()

seriesColors = list(mcolors.TABLEAU_COLORS.items())
seriesColors = [color[0] for color in seriesColors]

#seriesColors =["#000000","#009292","#ff6db6", "#490092","#006ddb","#b66dff","#6db6ff", "#920000","#db6d00","#24ff24"]


wordTotal = np.cumsum(words)/1000000.

xdates = [datetime.datetime.strptime(str(int(year))+str(int(month)),'%Y%m') for year, month in zip(years, months)]

yOffsets = [0] * 50
yOffsets[5] = -30 
yOffsets[7] = 10 
yOffsets[13] = -40 
yOffsets[15] = -60 
yOffsets[17] = -40 
yOffsets[19] = -40 
yOffsets[23] = -40 
yOffsets[25] = -60 
yOffsets[29] = -50 
yOffsets[31] = -30 
yOffsets[33] = -10 
yOffsets[35] = 10 
yOffsets[37] = 30 
yOffsets[39] = 30 
yOffsets[41] = -60 
yOffsets[43] = -20 
yOffsets[45] = -10 
yOffsets[47] = 30 
yOffsets[49] = -40 

yOffsets[10] = -20 
yOffsets[12] = -10 
yOffsets[14] = -110 
yOffsets[16] = -80 
yOffsets[18] = -40 
yOffsets[20] = -0 
yOffsets[22] = 20 
yOffsets[24] = 50 
yOffsets[26] = 10 
yOffsets[28] = 60 
yOffsets[30] = -20 
yOffsets[34] = 10 
yOffsets[36] = 30 
yOffsets[38] = 60 
yOffsets[40] = -10 
yOffsets[42] = -10 
yOffsets[44] = 20 
yOffsets[46] = 30 
yOffsets[48] = 60 


xOffsets = [0] * 50
xOffsets[19] = 20
xOffsets[23] = 90
xOffsets[39] = 120

legend_lines = [Line2D([0], [0], color=color, lw=4) for i, color in enumerate(seriesColors) ]

fig = plt.figure()
ax = plt.subplot(111)
plt.plot(xdates, wordTotal,'o-', linewidth=4,markerfacecolor='w', markeredgewidth=2, markersize=7)
plt.title('Sanderson Timeline',fontsize=35)
plt.ylabel('Cummulative number of words published',fontsize=25)
plt.xlabel('Publication Year', fontsize=25)
ax.yaxis.set_major_formatter(FormatStrFormatter('%.f'+' Mio.'))

ax.legend(legend_lines, seriesLabels)

plt.grid()

for i, title in enumerate(titles):
    if i == 0:
        continue
    yOffset = 3*i if i%2==1 else -3*(50-i)
    xOffset = -200 if i%2==1 else 200
    ha = "right" if i%2==1 else "left"
    va = "bottom" if i%2==1 else "top"
    #ha="center"
    #va="center"
    ax.annotate(title, xy=(mdates.date2num(xdates[i]), wordTotal[i]), xycoords='data', xytext=(xOffset + xOffsets[i], yOffset + yOffsets[i]), textcoords='offset pixels', arrowprops=dict(facecolor='black', width=1, headwidth=7, shrink=0.08), ha=ha, va=va, bbox=dict(boxstyle="round",  fc=seriesColors[series[i]], alpha = 0.7),)


total_per_series = data.groupby(['series'])['words'].sum().tolist()

sort_idx = sorted(range(len(total_per_series)), key=lambda k: total_per_series[k], reverse=True)
total_per_series = sorted(total_per_series,reverse=True)
ordered_seriesLabels = [seriesLabels[i] for i in sort_idx]
ordered_colors = [seriesColors[i] for i in sort_idx]

x_pos = np.arange(len(seriesLabels))

fig, ax = plt.subplots()
bar_plot = plt.bar(x_pos, total_per_series, align='center', alpha=0.7, color=ordered_colors)

def autolabel(rects):
    for idx,rect in enumerate(bar_plot):
        ax.text(rect.get_x() + rect.get_width()/2., 20000,
                ordered_seriesLabels[idx],
                ha='center', va='bottom', rotation=90, fontsize=15, weight='bold')

autolabel(bar_plot)

ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: str(round(x/1000000.,2))+" Mio."))
plt.title("Size of Sanderson's series'",fontsize=35)
plt.ylabel('Published words',fontsize=25)
plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,
    top=False,         
    labelbottom=False)

barSeries =  data.groupby(['series','years'])['words'].sum()
index = barSeries.index.values
values = barSeries.tolist()

rawBarData = [[index[i][0], index[i][1], val] for i, val in enumerate(values)]

barData = np.array([[0]*17]*10)
for point in rawBarData:
    barData[point[0]][point[1]-2004] = point[2] 


fig, ax = plt.subplots()
bottom = np.zeros(17)
ind = np.arange(17)    # the x locations for the groups
for elem, color in zip(barData, seriesColors):
    plt.bar(ind[1:], elem[1:], 0.8, bottom=bottom[1:], color=color)
    bottom += elem

ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: str(int(round(x/1000.)))+"k"))
ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: str(int(round(x+2004, 0)))))
plt.title("Published Words per year",fontsize=35)
plt.ylabel('Published Words',fontsize=25)
plt.xlabel('Year',fontsize=25)
ax.legend(legend_lines, seriesLabels, loc=2)
plt.show()

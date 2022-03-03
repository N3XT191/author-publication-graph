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
seriesLabels = [ 'Mistborn', 'Stormlight Archive', 'Other Cosmere', 'Skyward', 'Alcatraz', 'Reckoners', 'Legion', 'Wheel of Time', 'Others']
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

# yOffsets = [0] * 100
# yOffsets[3] = 10 
# yOffsets[5] = 10 
# yOffsets[7] = 20 
# yOffsets[13] = -20 
# yOffsets[15] = -60 
# yOffsets[17] = -40 
# yOffsets[19] = -20 
# yOffsets[23] = -40 
# yOffsets[25] = -60 
# yOffsets[29] = -50 
# yOffsets[31] = -30 
# yOffsets[33] = -10 
# yOffsets[35] = 10 
# yOffsets[37] = 30 
# yOffsets[39] = 30 
# yOffsets[41] = -60 
# yOffsets[43] = -20 
# yOffsets[45] = 10 
# yOffsets[47] = 30 
# yOffsets[49] = -40 
# yOffsets[55] = -80 
# yOffsets[57] = -80 

# yOffsets[10] = -20 
# yOffsets[12] = -10 
# yOffsets[14] = -60 
# yOffsets[16] = -20 
# yOffsets[18] = -40 
# yOffsets[20] = -0 
# yOffsets[22] = 20 
# yOffsets[24] = 50 
# yOffsets[26] = 10 
# yOffsets[28] = 60 
# yOffsets[30] = -40 
# yOffsets[32] = -10 
# yOffsets[34] = 0 
# yOffsets[36] = 20 
# yOffsets[38] = 70 
# yOffsets[40] = -10 
# yOffsets[42] = -10 
# yOffsets[44] = 20 
# yOffsets[46] = 30 
# yOffsets[48] = 0 
# yOffsets[50] = -40 
# yOffsets[54] = -40 
# yOffsets[56] = -40 
yOffsets = [0] * 100
yOffsets[4] = 10
yOffsets[10] = -20
yOffsets[12] = -20
yOffsets[14] = -110
yOffsets[16] = -90
yOffsets[18] = -50
yOffsets[20] = -10
yOffsets[22] = 10
yOffsets[24] = 40
yOffsets[30] = -60
yOffsets[32] = -30
yOffsets[34] = -20
yOffsets[36] = -10
yOffsets[38] = 20
yOffsets[40] = -20
yOffsets[44] = -30
yOffsets[46] = -20
yOffsets[48] = 20
yOffsets[50] = -30
yOffsets[52] = -15

yOffsets[33] = -30
yOffsets[35] = -20
yOffsets[37] = -10
yOffsets[41] = -50
yOffsets[43] = -20
yOffsets[45] = -10
yOffsets[49] = -50
yOffsets[51] = -15


# xOffsets = [0] * 100
# xOffsets[19] = 20
# xOffsets[23] = 90
# xOffsets[39] = 120
# xOffsets[41] = 20
xOffsets = [0] * 100
xOffsets[1] = 30
xOffsets[45] = -30
xOffsets[50] = -30
xOffsets[52] = -30
xOffsets[55] = -15
xOffsets[57] = -15
xOffsets[59] = -15

legend_lines = [Line2D([0], [0], color=color, lw=15) for i, color in enumerate(seriesColors) ]

fig = plt.figure()
ax = plt.subplot(111)
plt.plot(xdates, wordTotal,'o-', linewidth=4,markerfacecolor='w', markeredgewidth=2, markersize=7)
plt.title('Sanderson Timeline',fontsize=35)
plt.ylabel('Cummulative number of words published',fontsize=25)
plt.xlabel('Publication Year', fontsize=25)
ax.yaxis.set_major_formatter(FormatStrFormatter('%.f'+'M'))

ax.legend(legend_lines, seriesLabels,fontsize=20)

plt.axvline(x=(mdates.date2num(xdates[54])-100), ymin=0, ymax=8, color='black')

plt.grid()

for i, title in enumerate(titles):
    if i == 0 or words[i]<30000 :
        continue
    yOffset = 3*i if i%2==1 else -3*(53-i)
    #yOffset = 3*i if i%2==1 else -3*(50-i)
    xOffset = -3*(53-i) if i%2==1 else 3*i
    ha = "right" if i%2==1 else "left"
    va = "bottom" if i%2==1 else "top"
    #ha="center"
    #va="center"
    alpha = 0.6 if i<54 else 0.4
    edgecolor = 'black' if i<54 else 'white'
    ax.annotate(title,fontsize=9.5, xy=(mdates.date2num(xdates[i]), wordTotal[i]), xycoords='data', xytext=(xOffset + xOffsets[i], yOffset + yOffsets[i]), textcoords='offset pixels', arrowprops=dict(facecolor='black', width=1, headwidth=7, shrink=0.08), ha=ha, va=va, bbox=dict(boxstyle="round",  fc=seriesColors[int(series[i])], alpha = alpha, ec=edgecolor),)



total_per_series = data.groupby(['series'])['words'].sum().tolist()

sort_idx = sorted(range(len(total_per_series)), key=lambda k: total_per_series[k], reverse=True)
total_per_series = sorted(total_per_series,reverse=True)
ordered_seriesLabels = [seriesLabels[i] for i in sort_idx]
ordered_colors = [seriesColors[i] for i in sort_idx]

x_pos = np.arange(len(seriesLabels))

fig, ax = plt.subplots()
bar_plot = plt.bar(x_pos, total_per_series, align='center', alpha=0.9, color=ordered_colors)

def autolabel(rects):
    for idx,rect in enumerate(bar_plot):
        ax.text(rect.get_x() + rect.get_width()/2., 20000,
                ordered_seriesLabels[idx],
                ha='center', va='bottom', rotation=90, fontsize=20, weight='bold')

autolabel(bar_plot)

ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: str(round(x/1000000.,2))+"M"))
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

barData = np.array([[0]*20]*10)
for point in rawBarData:
    barData[point[0]][point[1]-2004] = point[2] 


fig, ax = plt.subplots()
bottom = np.zeros(20)
ind = np.arange(20)    # the x locations for the groups
for elem, color in zip(barData, seriesColors):
    plt.bar(ind[1:], elem[1:], 0.8, bottom=bottom[1:], color=color, alpha=0.9)
    bottom += elem

ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: str(int(round(x/1000.)))+"k"))
ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: str(int(round(x+2004, 0)))))
plt.title("Published Words per year",fontsize=35)
plt.ylabel('Published Words',fontsize=25)
plt.xlabel('Year',fontsize=25)
ax.legend(legend_lines, seriesLabels, loc=2,fontsize=18)
plt.show()

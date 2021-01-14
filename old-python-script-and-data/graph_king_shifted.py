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
dataSando = pandas.read_csv('data.csv', names=colnames)
dataKing = pandas.read_csv('data_king.csv', names=colnames)
dataRothfuss = pandas.read_csv('data_rothfuss.csv', names=colnames)
dataMartin = pandas.read_csv('data_martin.csv', names=colnames)
dataJordan = pandas.read_csv('data_jordan.csv', names=colnames)
dataPrattchet = pandas.read_csv('data_prattchet.csv', names=colnames)
dataErikson = pandas.read_csv('data_erikson.csv', names=colnames)
legend_labels = [ "Stephen King","Robert Jordan","Terry Pratchett",  "George R. R. Martin",  "Steven Erikson","Brandon Sanderson", "Patrick Rothfuss",]

titlesSando = dataSando.titles.tolist()
yearsSando = dataSando.years.tolist()
monthsSando = dataSando.months.tolist()
wordsSando = dataSando.words.tolist()

titlesKing = dataKing.titles.tolist()
yearsKing = dataKing.years.tolist()
monthsKing = dataKing.months.tolist()
wordsKing = dataKing.words.tolist()

titlesRothfuss = dataRothfuss.titles.tolist()
yearsRothfuss = dataRothfuss.years.tolist()
monthsRothfuss = dataRothfuss.months.tolist()
wordsRothfuss = dataRothfuss.words.tolist()

titlesMartin = dataMartin.titles.tolist()
yearsMartin = dataMartin.years.tolist()
monthsMartin = dataMartin.months.tolist()
wordsMartin = dataMartin.words.tolist()

titlesJordan = dataJordan.titles.tolist()
yearsJordan = dataJordan.years.tolist()
monthsJordan = dataJordan.months.tolist()
wordsJordan = dataJordan.words.tolist()

titlesPrattchet = dataPrattchet.titles.tolist()
yearsPrattchet = dataPrattchet.years.tolist()
monthsPrattchet = dataPrattchet.months.tolist()
wordsPrattchet = dataPrattchet.words.tolist()

titlesErikson = dataErikson.titles.tolist()
yearsErikson = dataErikson.years.tolist()
monthsErikson = dataErikson.months.tolist()
wordsErikson = dataErikson.words.tolist()

colors = list(mcolors.TABLEAU_COLORS.items())
colors = [color[0] for color in colors]

#seriesColors =["#000000","#009292","#ff6db6", "#490092","#006ddb","#b66dff","#6db6ff", "#920000","#db6d00","#24ff24"]


xdatesSando = [datetime.datetime.strptime(str(int(year-yearsSando[0]+1974))+str(int(month)),'%Y%m') for year, month in zip(yearsSando, monthsSando)]
xdatesKing = [datetime.datetime.strptime(str(int(year-yearsKing[0]+1974))+str(int(month)),'%Y%m') for year, month in zip(yearsKing, monthsKing)]
xdatesRothfuss = [datetime.datetime.strptime(str(int(year-yearsRothfuss[0]+1974))+str(int(month)),'%Y%m') for year, month in zip(yearsRothfuss, monthsRothfuss)]
xdatesMartin = [datetime.datetime.strptime(str(int(year-yearsMartin[0])+1974)+str(int(month)),'%Y%m') for year, month in zip(yearsMartin, monthsMartin)]
xdatesJordan = [datetime.datetime.strptime(str(int(year-yearsJordan[0])+1974)+str(int(month)),'%Y%m') for year, month in zip(yearsJordan, monthsJordan)]
xdatesErikson = [datetime.datetime.strptime(str(int(year-yearsErikson[0])+1974)+str(int(month)),'%Y%m') for year, month in zip(yearsErikson, monthsErikson)]
xdatesPrattchet = [datetime.datetime.strptime(str(int(year-yearsPrattchet[0])+1974)+str(int(month)),'%Y%m') for year, month in zip(yearsPrattchet, monthsPrattchet)]



legend_lines = [Line2D([0], [0], color=color, lw=8) for i, color in enumerate(colors[:len(legend_labels)]) ]

fig = plt.figure()
ax = plt.subplot(111)

plt.plot(xdatesSando, np.cumsum(wordsSando),'o-', linewidth=4,markerfacecolor='w', markeredgewidth=2, markersize=7, color=colors[5])
plt.plot(xdatesKing, np.cumsum(wordsKing),'o-', linewidth=4,markerfacecolor='w', markeredgewidth=2, markersize=7, color=colors[0])
plt.plot(xdatesRothfuss, np.cumsum(wordsRothfuss),'o-', linewidth=4,markerfacecolor='w', markeredgewidth=2, markersize=7, color=colors[6])
plt.plot(xdatesMartin, np.cumsum(wordsMartin),'o-', linewidth=4,markerfacecolor='w', markeredgewidth=2, markersize=7, color=colors[3])
plt.plot(xdatesJordan, np.cumsum(wordsJordan),'o-', linewidth=4,markerfacecolor='w', markeredgewidth=2, markersize=7, color=colors[1])
plt.plot(xdatesPrattchet, np.cumsum(wordsPrattchet),'o-', linewidth=4,markerfacecolor='w', markeredgewidth=2, markersize=5, color=colors[2],zorder=9999)
plt.plot(xdatesErikson, np.cumsum(wordsErikson),'o-', linewidth=4,markerfacecolor='w', markeredgewidth=2, markersize=5, color=colors[4],zorder=9999)

plt.title('Publications of selected Authors',fontsize=35)
plt.ylabel('Cummulative number of words published',fontsize=25)
ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: str(int(round(x/1000000.)))+"M"))
plt.xlabel('Publication Year', fontsize=25)

ax.legend(legend_lines, legend_labels,prop={'size': 20})

xForFitSando = [i.toordinal() for i in xdatesSando]
zSando = np.polyfit(xForFitSando, np.cumsum(wordsSando), 1)
pSando = np.poly1d(zSando)
xdatesSando.append(datetime.date(2044,1,1))
xForFitSando = [i.toordinal() for i in xdatesSando]

xForFitKing = [i.toordinal() for i in xdatesKing]
zKing = np.polyfit(xForFitKing, np.cumsum(wordsKing), 1)
pKing = np.poly1d(zKing)
xdatesKing.append(datetime.date(2044,1,1))
xForFitKing = [i.toordinal() for i in xdatesKing]

xForFitRothfuss = [i.toordinal() for i in xdatesRothfuss]
zRothfuss = np.polyfit(xForFitRothfuss, np.cumsum(wordsRothfuss), 1)
pRothfuss = np.poly1d(zRothfuss)
xdatesRothfuss.append(datetime.date(2044,1,1))
xForFitRothfuss = [i.toordinal() for i in xdatesRothfuss]

xForFitMartin = [i.toordinal() for i in xdatesMartin]
zMartin = np.polyfit(xForFitMartin, np.cumsum(wordsMartin), 1)
pMartin = np.poly1d(zMartin)
xdatesMartin.append(datetime.date(2044,1,1))
xForFitMartin = [i.toordinal() for i in xdatesMartin]

xForFitJordan = [i.toordinal() for i in xdatesJordan]
zJordan = np.polyfit(xForFitJordan, np.cumsum(wordsJordan), 1)
pJordan = np.poly1d(zJordan)
xdatesJordan.append(datetime.date(2044,1,1))
xForFitJordan = [i.toordinal() for i in xdatesJordan]

xForFitPrattchet = [i.toordinal() for i in xdatesPrattchet]
zPrattchet = np.polyfit(xForFitPrattchet, np.cumsum(wordsPrattchet), 1)
pPrattchet = np.poly1d(zPrattchet)
xdatesPrattchet.append(datetime.date(2044,1,1))
xForFitPrattchet = [i.toordinal() for i in xdatesPrattchet]

xForFitErikson = [i.toordinal() for i in xdatesErikson]
zErikson = np.polyfit(xForFitErikson, np.cumsum(wordsErikson), 1)
pErikson = np.poly1d(zErikson)
xdatesErikson.append(datetime.date(2044,1,1))
xForFitErikson = [i.toordinal() for i in xdatesErikson]

l = matplotlib.dates.AutoDateLocator()
f = matplotlib.dates.AutoDateFormatter(l)
ax.xaxis.set_major_locator(l)
ax.xaxis.set_major_formatter(f)

plt.plot(xdatesSando,pSando(xForFitSando),"r--", color=colors[5])
plt.plot(xdatesKing,pKing(xForFitKing),"r--", color=colors[0])
plt.plot(xdatesRothfuss,pRothfuss(xForFitRothfuss),"r--", color=colors[6])
plt.plot(xdatesMartin,pMartin(xForFitMartin),"r--", color=colors[3])
plt.plot(xdatesJordan,pJordan(xForFitJordan),"r--", color=colors[1])
plt.plot(xdatesErikson,pErikson(xForFitErikson),"r--", color=colors[4])
plt.plot(xdatesPrattchet,pPrattchet(xForFitPrattchet),"r--", color=colors[2])

plt.grid()
ax.set_xlim([datetime.date(1974, 1, 1), datetime.date(2031, 1, 1)])
ax.set_ylim([0,12000000])

plt.show()

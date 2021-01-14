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
dataSando = pandas.read_csv('dataSando.csv', names=colnames)
dataKing = pandas.read_csv('data_king.csv', names=colnames)
dataRothfuss = pandas.read_csv('data_rothfuss.csv', names=colnames)
dataMartin = pandas.read_csv('data_martin.csv', names=colnames)
dataJordan = pandas.read_csv('data_jordan.csv', names=colnames)
dataPrattchet = pandas.read_csv('data_prattchet.csv', names=colnames)
dataErikson = pandas.read_csv('data_erikson.csv', names=colnames)
legend_labels = [ "Stephen King","Robert Jordan","Terry Pratchett",  "George R. R. Martin",  "Steven Erikson","Brandon Sanderson", "Patrick Rothfuss",]
legend_numbers = [607, 463, 398, 170, 629, 1013, 74]

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


xdatesSando = [datetime.datetime.strptime(str(int(year))+str(int(month)),'%Y%m') for year, month in zip(yearsSando, monthsSando)]
xdatesKing = [datetime.datetime.strptime(str(int(year))+str(int(month)),'%Y%m') for year, month in zip(yearsKing, monthsKing)]
xdatesRothfuss = [datetime.datetime.strptime(str(int(year))+str(int(month)),'%Y%m') for year, month in zip(yearsRothfuss, monthsRothfuss)]
xdatesMartin = [datetime.datetime.strptime(str(int(year))+str(int(month)),'%Y%m') for year, month in zip(yearsMartin, monthsMartin)]
xdatesJordan = [datetime.datetime.strptime(str(int(year))+str(int(month)),'%Y%m') for year, month in zip(yearsJordan, monthsJordan)]
xdatesPrattchet = [datetime.datetime.strptime(str(int(year))+str(int(month)),'%Y%m') for year, month in zip(yearsPrattchet, monthsPrattchet)]
xdatesErikson = [datetime.datetime.strptime(str(int(year))+str(int(month)),'%Y%m') for year, month in zip(yearsErikson, monthsErikson)]


legend_lines = [Line2D([0], [0], color=color, lw=8) for i, color in enumerate(colors[:len(legend_labels)]) ]

fig = plt.figure()
ax = plt.subplot(111)

plt.plot(xdatesKing, np.cumsum(wordsKing),'o-', linewidth=4,markerfacecolor='w', markeredgewidth=2, markersize=5, color=colors[0],zorder=9999)
plt.plot(xdatesMartin[:-1], np.cumsum(wordsMartin[:-1]),'o-', linewidth=4,markerfacecolor='w', markeredgewidth=2, markersize=5, color=colors[3],zorder=9999)
plt.plot(xdatesJordan, np.cumsum(wordsJordan),'o-', linewidth=4,markerfacecolor='w', markeredgewidth=2, markersize=5, color=colors[1],zorder=9999)
plt.plot(xdatesPrattchet, np.cumsum(wordsPrattchet),'o-', linewidth=4,markerfacecolor='w', markeredgewidth=2, markersize=5, color=colors[2],zorder=9999)
plt.plot(xdatesErikson, np.cumsum(wordsErikson),'o-', linewidth=4,markerfacecolor='w', markeredgewidth=2, markersize=5, color=colors[4],zorder=9999)
plt.plot(xdatesSando[1:], np.cumsum(wordsSando)[1:],'o-', linewidth=4,markerfacecolor='w', markeredgewidth=2, markersize=5, color=colors[5],zorder=9999)
plt.plot(xdatesRothfuss[:-1], np.cumsum(wordsRothfuss[:-1]),'o-', linewidth=4,markerfacecolor='w', markeredgewidth=2, markersize=5, color=colors[6],zorder=9999)

plt.title('Publications of selected Authors',fontsize=35)
plt.ylabel('Cummulative number of words published',fontsize=25)
ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: str(int(round(x/1000000.)))+"M"))
plt.xlabel('Publication Year', fontsize=25)

legends = ['{:<19}{:>5,d} words/day'.format(legend_labels[idx], legend_numbers[idx]) for idx in    range(len(legend_labels))]
ax.legend(legend_lines,legends,prop={'size': 16, 'family': 'monospace'})


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
print(pKing)
print(pJordan)
print(pPrattchet)
print(pMartin)
print(pErikson)
print(pSando)
print(pRothfuss)

plt.plot(xdatesSando,pSando(xForFitSando),"r--", color=colors[5])
plt.plot(xdatesKing,pKing(xForFitKing),"r--", color=colors[0])
plt.plot(xdatesRothfuss,pRothfuss(xForFitRothfuss),"r--", color=colors[6])
plt.plot(xdatesMartin,pMartin(xForFitMartin),"r--", color=colors[3])
plt.plot(xdatesJordan,pJordan(xForFitJordan),"r--", color=colors[1])
plt.plot(xdatesPrattchet,pPrattchet(xForFitPrattchet),"r--", color=colors[2])
plt.plot(xdatesErikson,pErikson(xForFitErikson),"r--", color=colors[4])

plt.grid()
ax.set_xlim([datetime.date(1974, 1, 1), datetime.date(2021, 3, 1)])
ax.set_ylim([0,12000000])

j=0
for i, (title, word) in enumerate(zip(titlesKing, wordsKing)):
    if word < 200000:
        continue
    yOffset = 20 
    xOffset = -50
    ha = "right"
    va = "bottom"
    ax.annotate(title, xy=(mdates.date2num(xdatesKing[i]), np.cumsum(wordsKing)[i]), xycoords='data', xytext=(xOffset , yOffset), textcoords='offset pixels', arrowprops=dict(facecolor='black', width=1, headwidth=4, headlength=4, shrink=0.08), ha=ha, va=va, bbox=dict(boxstyle="round",  fc=colors[0], alpha = 0.85),fontsize=7,zorder=99999)
    j+=1
j=0
for i, (title, word) in enumerate(zip(titlesRothfuss, wordsRothfuss)):
    if word < 230000:
        continue
    yOffset = -20
    xOffset =  40
    ha = "left"
    va = "top"
    ax.annotate(title, xy=(mdates.date2num(xdatesRothfuss[i]), np.cumsum(wordsRothfuss)[i]), xycoords='data', xytext=(xOffset , yOffset), textcoords='offset pixels', arrowprops=dict(facecolor='black', width=1, headwidth=4, headlength=4, shrink=0.08), ha=ha, va=va, bbox=dict(boxstyle="round",  fc=colors[6], alpha = 0.85),fontsize=7,zorder=99999)
    j+=1
for i, (title, word) in enumerate(zip(titlesMartin, wordsMartin)):
    if word < 230000:
        continue
    yOffset = -20
    xOffset = 40
    ha = "left"
    va = "top"
    ax.annotate(title, xy=(mdates.date2num(xdatesMartin[i]), np.cumsum(wordsMartin)[i]), xycoords='data', xytext=(xOffset , yOffset), textcoords='offset pixels', arrowprops=dict(facecolor='black', width=1, headwidth=4, headlength=4, shrink=0.08), ha=ha, va=va, bbox=dict(boxstyle="round",  fc=colors[3], alpha = 0.85),fontsize=7,zorder=99999)
for i, (title, word) in enumerate(zip(titlesJordan, wordsJordan)):
    if word < 290000:
        continue
    yOffset = 20
    xOffset = -40
    ha = "right"
    va = "bottom"
    ax.annotate(title, xy=(mdates.date2num(xdatesJordan[i]), np.cumsum(wordsJordan)[i]), xycoords='data', xytext=(xOffset , yOffset), textcoords='offset pixels', arrowprops=dict(facecolor='black', width=1, headwidth=4, headlength=4, shrink=0.08), ha=ha, va=va, bbox=dict(boxstyle="round",  fc=colors[1], alpha = 0.85),fontsize=7,zorder=99999)
    j+=1
j=0
for i, (title, word) in enumerate(zip(titlesSando, wordsSando)):
    if word < 230000 or i == 14 or i == 5: 
        continue
    yOffset = -10
    xOffset = 40
    ha ="left"
    va = "top"
    ax.annotate(title, xy=(mdates.date2num(xdatesSando[i]), np.cumsum(wordsSando)[i]), xycoords='data', xytext=(xOffset , yOffset), textcoords='offset pixels', arrowprops=dict(facecolor='black', width=1, headwidth=4, headlength=4, shrink=0.08), ha=ha, va=va, bbox=dict(boxstyle="round",  fc=colors[5], alpha = 0.85),fontsize=7,zorder=99999)
    j+=1
j=0
for i, (title, word) in enumerate(zip(titlesPrattchet, wordsPrattchet)):
    if word < 115000 and i != 2:
        continue
    yOffset = 60 if  i>40 else -15
    xOffset = -60 if i>40 else 40
    ha = "right" if i>40 else "left"
    va = "bottom" if i>40 else "top"
    ax.annotate(title, xy=(mdates.date2num(xdatesPrattchet[i]), np.cumsum(wordsPrattchet)[i]), xycoords='data', xytext=(xOffset , yOffset), textcoords='offset pixels', arrowprops=dict(facecolor='black', width=1, headwidth=4, headlength=4, shrink=0.08), ha=ha, va=va, bbox=dict(boxstyle="round",  fc=colors[2], alpha = 0.85),fontsize=7,zorder=99999)
    j+=1
j=0
for i, (title, word) in enumerate(zip(titlesErikson, wordsErikson)):
    if word < 380000:
        continue
    yOffset = -20
    xOffset = 20
    ha =  "left"
    va =  "top"
    ax.annotate(title, xy=(mdates.date2num(xdatesErikson[i]), np.cumsum(wordsErikson)[i]), xycoords='data', xytext=(xOffset , yOffset), textcoords='offset pixels', arrowprops=dict(facecolor='black', width=1, headwidth=4, headlength=4, shrink=0.08), ha=ha, va=va, bbox=dict(boxstyle="round",  fc=colors[4], alpha = 0.85),fontsize=7,zorder=99999)
    j+=1




plt.show()

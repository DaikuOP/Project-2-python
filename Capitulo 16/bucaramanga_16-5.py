import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'Project/chapter 16/data/bucaramanga_2023.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    date, tmin, tmax = header_row.index("DATE"), header_row.index("TMIN"), header_row.index("TMAX") 

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[date], '%Y-%m-%d')
        try:
            high = int(row[tmax])
            low = int(row[tmin])
        except ValueError:
            print(f"Datos faltantes para {current_date}")
            continue
        highs.append(high)
        dates.append(current_date)
        lows.append(low)
        station = str(row[0])


plt.style.use("ggplot")
fig, ax = plt.subplots(figsize = (15, 9), dpi = 100)

ax.plot(dates, highs, c = 'red', alpha = 0.5)
ax.plot(dates, lows, c = 'blue', alpha = 0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

#Station name in the title
title = station
plt.title('Temperatura maxima y minima en Bucaramanga en 2023\nregistrada en  por la estación ' + title, fontsize = 20)
plt.xlabel(' ', fontsize = '16')
fig.autofmt_xdate()
plt.ylabel("Temperatura (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.savefig('Bucarmanga.png')
plt.show()

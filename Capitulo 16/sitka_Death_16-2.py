import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'Project/chapter 16/data/sitka_weather_2018_simple.csv'
filename2 = 'Project/chapter 16/data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        highs.append(high)
        dates.append(current_date)
        lows.append(low)

with open(filename2) as m:
    reader2 = csv.reader(m)
    header_row2 = next(reader2)
    print(header_row2)

    for index2, column_header2 in enumerate(header_row2):
        print(index2, column_header2)


    dates2, highs2, lows2 = [], [], []
    for row2 in reader2:
        current_date2 = datetime.strptime(row2[2], '%Y-%m-%d')
        try:
            high2 = int(row2[4])
            low2 = int(row2[5])
        except ValueError:
            print(f"Datos faltantes para {current_date2}")
        highs2.append(high2)
        dates2.append(current_date2)
        lows2.append(low2)

plt.style.use("ggplot")
fig, ax = plt.subplots(figsize = (15, 9), dpi = 100)

ax.plot(dates, highs, c = 'red', alpha = 0.5)
ax.plot(dates, lows, c = 'blue', alpha = 0.5)
ax.plot(dates2, highs2, c = 'orange', alpha = 0.5)
ax.plot(dates2, lows2, c = 'green', alpha = 0.5)

plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
plt.fill_between(dates2, highs2, lows2, facecolor='orange', alpha=0.1)

plt.ylim(20, 130)

plt.title('Maxima y minima tempertatura diaria - 2018', fontsize = 20)
plt.xlabel(' ', fontsize = '16')
fig.autofmt_xdate()
plt.ylabel("Temperatura (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.savefig("Sitka-DeathValley.png")
plt.show()

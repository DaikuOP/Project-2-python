import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'Project/chapter 16/data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    dates, precipitation = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        prec = float(row[3])
        precipitation.append(prec)
        dates.append(current_date)
  

plt.style.use("ggplot")
fig, ax = plt.subplots(figsize = (15, 9), dpi = 100)

ax.plot(dates, precipitation, c = 'blue', alpha = 0.5)

plt.title('Precipitacion en 2018\n Sitka, Alaska', fontsize = 20)
plt.xlabel(' ', fontsize = '16')
fig.autofmt_xdate()
plt.tick_params(axis='both', which='major', labelsize=16)
plt.ylabel("Lluvia (m^3/s)", fontsize=16)


plt.savefig('sitka lluvia.png')
plt.show()

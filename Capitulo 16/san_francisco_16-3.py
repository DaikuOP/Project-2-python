import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'Project/chapter 16/data/san _francisco_2023.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[4])
        low = int(row[5])
        highs.append(high)
        dates.append(current_date)
        lows.append(low)

plt.style.use("ggplot")
fig, ax = plt.subplots(figsize = (15, 9), dpi = 100)

ax.plot(dates, highs, c = 'red', alpha = 0.5)
ax.plot(dates, lows, c = 'blue', alpha = 0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

plt.ylim(20, 130)

plt.title('Maxima y minima tempertatura en San Francisco - 2023', fontsize = 20)
plt.xlabel(' ', fontsize = '16')
fig.autofmt_xdate()
plt.ylabel("Temperatura (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.savefig('San francisco.png')
plt.show()

import csv
from matplotlib import pyplot
from datetime import datetime

filename = input("Filename: ")


# Get the dates, high, and low temperatures from file
with open(filename) as file:
    reader = csv.reader(file)
    header_row = next(reader)
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Plot the data
fig = pyplot.figure(dpi=128, figsize=(10, 6))
pyplot.plot(dates, highs, c='red', alpha=0.5)
pyplot.plot(dates, lows, c='blue', alpha=0.5)
pyplot.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
pyplot.title("Daily high and low temperatures - 2014", fontsize=14)
pyplot.xlabel("", fontsize=14)
fig.autofmt_xdate()
pyplot.ylabel("Temperature (F)", fontsize=10)
pyplot.tick_params(axis='both', which='major', labelsize=8)

pyplot.show()

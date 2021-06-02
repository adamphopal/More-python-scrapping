import csv
import numpy as np
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

with open('modified.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    sold_counter = Counter()

    for row in csv_reader:
        sold_counter.update(row['total sold'])

total_sold = []
popularity = []

for item in sold_counter.most_common():
    total_sold.append(item[0])
    popularity.append(item[1])

total_sold.reverse()
popularity.reverse()


plt.barh(total_sold, popularity)

plt.title("Most popular python books sold on ebay")
plt.ylabel("Total books sold")
plt.xlabel("Total Python ebay Books")

plt.tight_layout()


plt.show()

#print(total_sold)
#print(popularity)
    


#print(sold_counter.most_common())

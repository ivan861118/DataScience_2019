"""
131072
250419




"""


# =============

import csv

data = []

csv_list = ["1701_1.csv", "1702_1.csv", "1703_1.csv", "1704_1.csv", "1705_1.csv", "1706_1.csv",\
            "1707_1.csv", "1708_1.csv", "1709_1.csv", "1710_1.csv", "1711_1.csv", "1712_1.csv",\
            "1801_1.csv", "1802_1.csv", "1803_1.csv", "1804_1.csv", "1805_1.csv", "1806_1.csv",\
            "1807_1.csv", "1808_1.csv", "1809_1.csv", "1810_1.csv", "1811_1.csv", "1812_1.csv",\
            "1901_1.csv", "1902_1.csv", "1903_1.csv"]

for file in csv_list:

    with open(file, 'r') as csvFile:
        rows = csv.reader(csvFile)
        cur = []
        for i in rows:
            cur.append(i)

        data.append(cur)

print(data)

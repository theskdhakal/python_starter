# with open("./weather_data.csv","r") as data_file:
#
#     data=data_file.readlines()
#     print(data)

 # +++++++++++++++ using csv reader to read csv file++++++++++++++
#
# import csv
#
# with open("weather_data.csv") as data_file:
#     data=csv.reader(data_file)
#     temperature=[]
#     for row in data:
#         if row[1] != 'temp':
#          temperature.append(int(row[1]))
#     print(temperature)

# pandas______python data anaylis library

import pandas

data=pandas.read_csv("weather_data.csv")
print(type(data))
# print(data["temp"])
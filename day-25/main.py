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
# print(type(data))
# print(data["temp"])
#
# data_dict=data.to_dict()
# print(data_dict)
#
# temp_list=data["temp"].to_list()
# print(temp_list)
#
# average=sum(temp_list)/len(temp_list)
# print(f" Average temperature is : {average}")
#
# print(data["temp"].mean())

print(data['temp'].max())


# get data in column
# data["column name"]
# data.column-name

# get data in row
# data[data.attribute=="desired attribute"]

print(data[data["day"]=="Monday"])


#  find the row where temperature is maximum
print(data[data["temp"]==data.temp.max()])

#  find the condition of row where temperature is maximum
print(data[data["temp"]==data.temp.max()].condition)


monday=data[data.day=="Monday"]
print(monday["temp"])
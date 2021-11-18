#
# #Bad Way
#
# # with open("weather_data.csv", "r") as data:
# #     input = data.readlines()
# #     output = []
# #     for line in input:
# #         stripped_line = line.strip()
# #         output.append(stripped_line)
# #     print(output)
#
#
# #Bad Way 2
#
# # import csv
# #
# # with open("weather_data.csv", "r") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     print(data)
# #
# #     for row in data:
# #         if row[1].isnumeric():
# #             temperatures.append(int(row[1]))
# #     print(temperatures)
#
# #Much Better
# import pandas
# import pandas as pd
#
# data = pd.read_csv("weather_data.csv")
#
# # print(type(data))
# #
# # print(type(data["temp"]))
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data.to_dict("list")
# print(temp_list)
#
# print(type(temp_list)) # is still a dictionary
#
# temp_vals = temp_list["temp"]
# print(temp_vals)
#
# average = sum(temp_vals) / len(temp_vals)
# print(round(average))
#
#
# print(data)
# print("="*10)
# print(data["temp"].mean())
#
# # get data in columns
# print(data["condition"])
# print(data.condition)
#
# # get data in the rows
# print(data[data.day == "Monday"]) # this looks so strange
#
# max = data.temp.max()
# print(data[data.temp == max])
#
# monday = data[data.day == "Monday"]
#
# yes = monday.temp.mul(1.8)
# farh = yes + 32
#
# print(farh)
#
#
# # Create a dataframe from scratch
#
# data_dict = {
#     "students":["Any", "James", "Jamal"],
#     "scores":[76,95,44]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
import pandas
import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_count = len(data[data["Primary Fur Color"] == "Gray"])
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color":["Gray", "Cinnamon", "Black"],
    "Number of Squirrels":[grey_count, red_count, black_count]
}

dater = pandas.DataFrame(data_dict)
dater.to_csv("squirrel_counts.csv")

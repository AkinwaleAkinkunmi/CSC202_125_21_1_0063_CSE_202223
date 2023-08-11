# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)


# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# # print(data["temp"])
# data_dict = data.to_dict()
# print(data_dict)

#Working with Rows and Columns
# temp_list = data["temp"].to_list()
# print(len(temp_list))
#
# # average = sum(temp_list) / len(temp_list)
# # print(average)
# print(data["temp"].mean())
# print(data["temp"].max())
#
# print(data["Condition"])
# print(data.Condition)
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# #Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela",
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")


import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

pandas.Dataframe(data_dict)
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")


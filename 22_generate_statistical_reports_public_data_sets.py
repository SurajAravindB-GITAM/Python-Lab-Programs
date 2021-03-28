""" Design a Python script to generate statistical reports (Minimum, Maximum, Count, Average, Sum etc) on public datasets. """
import pandas as pd
file = r"C:\Python36\rakesh\marks.xlsx"
data = pd.read_excel(file,usecols = "D")
list1 = data.values.tolist()
details = []
for i in list1:
    for j in i:
        details.append(j)
print("The maximum marks is: ",max(details))
max_marks = details.count(max(details))
print("The minimum marks is: ",min(details))
min_marks = details.count(min(details))
max_marks = details.count(max(details))
print("count of min:",min_marks)
print("count of max:",max_marks)
print("Test written members:",len(details))
average_marks = sum(details)/len(details)
print(average_marks)

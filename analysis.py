import csv

with open('onlinefoods.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))

# Extract the age column into a separate list
age_column = [int(row[0]) for row in data[1:]]

print(f"The minimum age of people who ordered online is {min(age_column)}")
print(f"The maximum age of people who ordered online is {max(age_column)}")
print(f"The average age of people who ordered online is {sum(age_column) / len(age_column)}")

# Extract the feedback column into a separate list
feedback_column = [str(row[11]).strip() for row in data[1:]]

numRows = len(feedback_column)
num_positive = feedback_column.count("Positive")
num_negative = feedback_column.count("Negative")
pecent_positive = round((num_positive/numRows)*100,2)
percent_negative = round((num_negative/numRows)*100,2)

print(f"The number of people who left positive feedback is {num_positive} which is {pecent_positive}%")
print(f"The number of people who left negative feedback is {num_negative} which is {percent_negative}%")
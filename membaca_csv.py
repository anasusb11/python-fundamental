import csv
# open file default menggunakan close untuk melakukan penutupan
# users = open("test.csv", "r")
#OPTIONAL pake WITH BLOCK tidak perlu pake func close
with open("test.csv", "r") as users:
    user_csv = csv.reader(users, delimiter=",")

    for row in user_csv:
        print(f"Name: {row[0]}. Username: {row[1]}. Role: {row[2]}")

# users.close()